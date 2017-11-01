#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Cloud Conversation Engine API DetectIntent() Python sample.

See https://cloud.google.com/speech/docs/basics for a discussion of the similar
(not equal!) options for the Speech API.

Examples:
  python detect_intent.py -h
  python detect_intent.py text "Order a large pizza" "tuna" "1600 Amphitheatre Pkwy" "check"
  python detect_intent.py event order_pizza
  python detect_intent.py audio resources/pizza_order.wav \
      --sample_rate_hertz=22050
  python detect_intent.py stream resources/pizza_order.wav \
      --sample_rate_hertz=22050
"""

# [START import_libraries]
from google.cloud.gapic.conversation.v1alpha.conversation_service_client import ConversationServiceClient
from google.cloud.proto.conversation.v1alpha import detect_intent_pb2
import argparse
import os
import sys
import uuid
# [END import_libraries]


def _parse_args(unparsed_args):
    """Parsed the given commandline args."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project_id',
        help='Project/agent id. Defaults to the value of the GCLOUD_PROJECT or '
        'GOOGLE_CLOUD_PROJECT environment variables.')
    parser.add_argument(
        '--session_id',
        help='Identifier of the DetectIntent session. '
             'Defaults to a random UUID.')
    parser.add_argument(
        '--language_code',
        help='Language code of the query. Defaults to "en-US".',
        default='en-US')
    parser.add_argument(
        '--encoding',
        help='Encoding of the input audio. Defaults to '
            'AUDIO_ENCODING_LINEAR16. See '
            'https://cloud.google.com/speech/docs/basics#audio-encodings.',
        type=detect_intent_pb2.AudioEncoding.Value,
        default='AUDIO_ENCODING_LINEAR16')
    parser.add_argument(
        '--sample_rate_hertz',
        help='Sample rate of the input audio. Only required if the input '
            'audio is in raw format. See '
            'https://cloud.google.com/speech/docs/basics#sample-rates.',
        type=int,
        default=None)
    parser.add_argument(
        'command',
        choices=['text', 'event', 'audio', 'stream'],
        help='Command to run.')
    parser.add_argument('inputs', nargs='+', help='Inputs for the command.')
    args = parser.parse_args(unparsed_args)
    if args.command != 'text' and len(args.inputs) > 1:
        raise ValueError('Command {} needs exactly one input'.format(
            args.command))
    args.project_id = args.project_id or os.getenv('GCLOUD_PROJECT') or (
        os.getenv('GOOGLE_CLOUD_PROJECT'))
    if not args.project_id:
        raise ValueError(
            'Project/agent id. Defaults to the value of the GCLOUD_PROJECT or '
            'GOOGLE_CLOUD_PROJECT environment variables.')
    args.session_id = args.session_id or str(uuid.uuid4())
    return args


def _create_session_path(project_id, agent_id, session_id):
    # Agent ID must be the same as project ID for v1alpha.
    return ConversationServiceClient.session_path(
        project=project_id, agent=agent_id, session=session_id)


def _detect_text_intent(project_id, agent_id, session_id, text, language_code):
    """Returns the result of DetectIntent() with a text input."""
    session_path = _create_session_path(project_id, agent_id, session_id)
    query_input = detect_intent_pb2.QueryInput(
        text=(detect_intent_pb2.TextInput(
            text=text, language_code=language_code)))
    return (ConversationServiceClient().detect_intent(
                session=session_path, query_input=query_input)
            .query_result)


def _detect_event_intent(project_id, session_id, event):
    """Returns the result of DetectIntent() with an event name."""
    session_path = _create_session_path(project_id, session_id)
    query_input = detect_intent_pb2.QueryInput(
        event=detect_intent_pb2.EventInput(name=event))
    return (ConversationServiceClient().detect_intent(
                session=session_path, query_input=query_input)
            .query_result)


def _detect_audio_intent(project_id, session_id, audio_file_path,
                         language_code, encoding, sample_rate_hertz):
    """Returns the result of a DetectIntent() with an audio input."""
    with open(audio_file_path, 'rb') as audio_file:
        session_path = _create_session_path(project_id, session_id)
        query_input = detect_intent_pb2.QueryInput(
            audio_config=detect_intent_pb2.InputAudioConfig(
                audio_encoding=encoding,
                language_code=language_code,
                sample_rate_hertz=sample_rate_hertz))
        return (ConversationServiceClient().detect_intent(
                    session=session_path,
                    query_input=query_input,
                    input_audio=audio_file.read())
                .query_result)


def _detect_audio_stream(project_id, session_id, audio_file_path,
                         language_code, encoding, sample_rate_hertz):
    """Returns the result of a streaming DetectIntent() with an audio input."""
    with open(audio_file_path, 'rb') as audio_file:

        def request_iterator():
            """Iterator that yields the streaming requests."""
            # 1st message: configuration.
            session_path = _create_session_path(project_id, session_id)
            query_input = detect_intent_pb2.StreamingQueryInput(
                audio_config=detect_intent_pb2.StreamingInputAudioConfig(
                    config=detect_intent_pb2.InputAudioConfig(
                        audio_encoding=encoding,
                        language_code=language_code,
                        sample_rate_hertz=sample_rate_hertz)))
            yield detect_intent_pb2.StreamingDetectIntentRequest(
                query_params=detect_intent_pb2.StreamingQueryParameters(
                    session=session_path),
                query_input=query_input)
            # Following messages: audio chunks. We just read the file in
            # fixed-size chunks. In reality you would split the user input by
            # time.
            while True:
                chunk = audio_file.read(4096)
                if not chunk:
                    break
                yield detect_intent_pb2.StreamingDetectIntentRequest(
                    input_audio=chunk)

        last_response = None
        for response in ConversationServiceClient().streaming_detect_intent(
                request_iterator()):
            last_response = response
            if response.HasField('recognition_result'):
                print('Intermediate transcript: "{}".'.format(
                    response.recognition_result.transcript))
        return last_response.query_result


# Format strings for _print_result.
RESULT_FORMAT = """Intent detection result:
  Query: "{result.query_text}"
  Response: "{result.fulfillment.text}"
  Intent: {intent}
  Parameters: '{parameters}'
  Output contexts:
{output_contexts}
"""
OUTPUT_CONTEXTS_FORMAT = """    {context_name}
      Lifespan: {lifespan_count}
      Parameters: '{parameters}'
"""


def _print_result(result):
    """Prints parts of a QueryResult in readable form."""
    print(RESULT_FORMAT.format(
        result=result,
        parameters=str(result.parameters).replace('\n', ''),
        intent=(result.HasField('intent') and 'detected "{}"'.format(
            result.intent.display_name) or 'not detected'),
        output_contexts=''.join(
            OUTPUT_CONTEXTS_FORMAT.format(
                context_name=ConversationServiceClient.
                match_context_from_context_name(context.name),
                lifespan_count=context.lifespan_count,
                parameters=str(context.parameters).replace('\n', '')
            ) for context in result.output_contexts)))


def run(unparsed_args):
    """Runs DetectIntent() with the given commands."""
    args = _parse_args(unparsed_args)
    # Functions for detecting intents.
    detect_functions = {
        'text':
            lambda single_input: _detect_text_intent(
                args.project_id, args.session_id, single_input,
                args.language_code),
        'event':
            lambda single_input: _detect_event_intent(
                args.project_id, args.session_id, single_input),
        'audio':
            lambda single_input: _detect_audio_intent(
                args.project_id, args.session_id, single_input,
                args.language_code, args.encoding,
                args.sample_rate_hertz),
        'stream':
            lambda single_input: _detect_audio_stream(
                args.project_id, args.session_id, single_input,
                args.language_code, args.encoding,
                args.sample_rate_hertz),
    }
    try:
        for single_input in args.inputs:
            _print_result(detect_functions[args.command](single_input))
    except Exception as exception:
        if 'usable-auth-library' in str(exception):
            # If you aren't using a service account that has the API enabled,
            # the error message refers to the strange project
            # 'usable-auth-library'.
            exception.args += ('Possible error reason: You aren\'t '
                'specifying the GOOGLE_APPLICATION_CREDENTIALS environment '
                'variable with a service account credential.',)
        raise


if __name__ == '__main__':
    run(sys.argv[1:])
