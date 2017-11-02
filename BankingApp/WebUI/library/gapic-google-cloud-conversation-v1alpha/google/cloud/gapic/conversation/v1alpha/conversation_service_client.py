# Copyright 2017, Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# EDITING INSTRUCTIONS
# This file was generated from the file
# https://github.com/google/googleapis/blob/master/google/cloud/conversation/v1alpha/conversation_service.proto,
# and updates to that file get reflected here through a refresh process.
# For the short term, the refresh process will only be runnable by Google engineers.
#
# The only allowed edits are to method and file documentation. A 3-way
# merge preserves those additions if the generated source changes.
"""Accesses the google.cloud.conversation.v1alpha ConversationService API."""

import collections
import json
import os
import pkg_resources
import platform

from google.gax import api_callable
from google.gax import config
from google.gax import path_template
import google.gax

from google.cloud.gapic.conversation.v1alpha import enums
from google.cloud.proto.conversation.v1alpha import context_pb2
from google.cloud.proto.conversation.v1alpha import conversation_service_pb2
from google.cloud.proto.conversation.v1alpha import detect_intent_pb2
from google.cloud.proto.conversation.v1alpha import entity_type_pb2
from google.cloud.proto.conversation.v1alpha import intent_pb2
from google.cloud.proto.conversation.v1alpha import session_entity_type_pb2


class ConversationServiceClient(object):
    """
    This service defines the Cloud Conversation Engine API. The Cloud
    Conversation Engine API is a natural language understanding platform that you
    can use to design and integrate a conversational user interface into your
    # application.

    Conversation API
    """

    SERVICE_ADDRESS = 'conversation.googleapis.com'
    """The default address of the service."""

    DEFAULT_SERVICE_PORT = 443
    """The default port of the service."""

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _ALL_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    _AGENT_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agents/{agent}')
    _ENTITY_TYPE_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agents/{agent}/entityTypes/{entity_type}')
    _INTENT_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agents/{agent}/intents/{intent}')
    _SESSION_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agents/{agent}/sessions/{session}')
    _CONTEXT_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agents/{agent}/sessions/{session}/contexts/{context}'
    )
    _SESSION_ENTITY_TYPE_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agents/{agent}/sessions/{session}/entityTypes/{entity_type}'
    )

    @classmethod
    def agent_path(cls, project, agent):
        """Returns a fully-qualified agent resource name string."""
        return cls._AGENT_PATH_TEMPLATE.render({
            'project': project,
            'agent': agent,
        })

    @classmethod
    def entity_type_path(cls, project, agent, entity_type):
        """Returns a fully-qualified entity_type resource name string."""
        return cls._ENTITY_TYPE_PATH_TEMPLATE.render({
            'project':
            project,
            'agent':
            agent,
            'entity_type':
            entity_type,
        })

    @classmethod
    def intent_path(cls, project, agent, intent):
        """Returns a fully-qualified intent resource name string."""
        return cls._INTENT_PATH_TEMPLATE.render({
            'project': project,
            'agent': agent,
            'intent': intent,
        })

    @classmethod
    def session_path(cls, project, agent, session):
        """Returns a fully-qualified session resource name string."""
        return cls._SESSION_PATH_TEMPLATE.render({
            'project': project,
            'agent': agent,
            'session': session,
        })

    @classmethod
    def context_path(cls, project, agent, session, context):
        """Returns a fully-qualified context resource name string."""
        return cls._CONTEXT_PATH_TEMPLATE.render({
            'project': project,
            'agent': agent,
            'session': session,
            'context': context,
        })

    @classmethod
    def session_entity_type_path(cls, project, agent, session, entity_type):
        """Returns a fully-qualified session_entity_type resource name string."""
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.render({
            'project':
            project,
            'agent':
            agent,
            'session':
            session,
            'entity_type':
            entity_type,
        })

    @classmethod
    def match_project_from_agent_name(cls, agent_name):
        """Parses the project from a agent resource.

        Args:
          agent_name (string): A fully-qualified path representing a agent
            resource.

        Returns:
          A string representing the project.
        """
        return cls._AGENT_PATH_TEMPLATE.match(agent_name).get('project')

    @classmethod
    def match_agent_from_agent_name(cls, agent_name):
        """Parses the agent from a agent resource.

        Args:
          agent_name (string): A fully-qualified path representing a agent
            resource.

        Returns:
          A string representing the agent.
        """
        return cls._AGENT_PATH_TEMPLATE.match(agent_name).get('agent')

    @classmethod
    def match_project_from_entity_type_name(cls, entity_type_name):
        """Parses the project from a entity_type resource.

        Args:
          entity_type_name (string): A fully-qualified path representing a entity_type
            resource.

        Returns:
          A string representing the project.
        """
        return cls._ENTITY_TYPE_PATH_TEMPLATE.match(entity_type_name).get(
            'project')

    @classmethod
    def match_agent_from_entity_type_name(cls, entity_type_name):
        """Parses the agent from a entity_type resource.

        Args:
          entity_type_name (string): A fully-qualified path representing a entity_type
            resource.

        Returns:
          A string representing the agent.
        """
        return cls._ENTITY_TYPE_PATH_TEMPLATE.match(entity_type_name).get(
            'agent')

    @classmethod
    def match_entity_type_from_entity_type_name(cls, entity_type_name):
        """Parses the entity_type from a entity_type resource.

        Args:
          entity_type_name (string): A fully-qualified path representing a entity_type
            resource.

        Returns:
          A string representing the entity_type.
        """
        return cls._ENTITY_TYPE_PATH_TEMPLATE.match(entity_type_name).get(
            'entity_type')

    @classmethod
    def match_project_from_intent_name(cls, intent_name):
        """Parses the project from a intent resource.

        Args:
          intent_name (string): A fully-qualified path representing a intent
            resource.

        Returns:
          A string representing the project.
        """
        return cls._INTENT_PATH_TEMPLATE.match(intent_name).get('project')

    @classmethod
    def match_agent_from_intent_name(cls, intent_name):
        """Parses the agent from a intent resource.

        Args:
          intent_name (string): A fully-qualified path representing a intent
            resource.

        Returns:
          A string representing the agent.
        """
        return cls._INTENT_PATH_TEMPLATE.match(intent_name).get('agent')

    @classmethod
    def match_intent_from_intent_name(cls, intent_name):
        """Parses the intent from a intent resource.

        Args:
          intent_name (string): A fully-qualified path representing a intent
            resource.

        Returns:
          A string representing the intent.
        """
        return cls._INTENT_PATH_TEMPLATE.match(intent_name).get('intent')

    @classmethod
    def match_project_from_session_name(cls, session_name):
        """Parses the project from a session resource.

        Args:
          session_name (string): A fully-qualified path representing a session
            resource.

        Returns:
          A string representing the project.
        """
        return cls._SESSION_PATH_TEMPLATE.match(session_name).get('project')

    @classmethod
    def match_agent_from_session_name(cls, session_name):
        """Parses the agent from a session resource.

        Args:
          session_name (string): A fully-qualified path representing a session
            resource.

        Returns:
          A string representing the agent.
        """
        return cls._SESSION_PATH_TEMPLATE.match(session_name).get('agent')

    @classmethod
    def match_session_from_session_name(cls, session_name):
        """Parses the session from a session resource.

        Args:
          session_name (string): A fully-qualified path representing a session
            resource.

        Returns:
          A string representing the session.
        """
        return cls._SESSION_PATH_TEMPLATE.match(session_name).get('session')

    @classmethod
    def match_project_from_context_name(cls, context_name):
        """Parses the project from a context resource.

        Args:
          context_name (string): A fully-qualified path representing a context
            resource.

        Returns:
          A string representing the project.
        """
        return cls._CONTEXT_PATH_TEMPLATE.match(context_name).get('project')

    @classmethod
    def match_agent_from_context_name(cls, context_name):
        """Parses the agent from a context resource.

        Args:
          context_name (string): A fully-qualified path representing a context
            resource.

        Returns:
          A string representing the agent.
        """
        return cls._CONTEXT_PATH_TEMPLATE.match(context_name).get('agent')

    @classmethod
    def match_session_from_context_name(cls, context_name):
        """Parses the session from a context resource.

        Args:
          context_name (string): A fully-qualified path representing a context
            resource.

        Returns:
          A string representing the session.
        """
        return cls._CONTEXT_PATH_TEMPLATE.match(context_name).get('session')

    @classmethod
    def match_context_from_context_name(cls, context_name):
        """Parses the context from a context resource.

        Args:
          context_name (string): A fully-qualified path representing a context
            resource.

        Returns:
          A string representing the context.
        """
        return cls._CONTEXT_PATH_TEMPLATE.match(context_name).get('context')

    @classmethod
    def match_project_from_session_entity_type_name(cls,
                                                    session_entity_type_name):
        """Parses the project from a session_entity_type resource.

        Args:
          session_entity_type_name (string): A fully-qualified path representing a session_entity_type
            resource.

        Returns:
          A string representing the project.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('project')

    @classmethod
    def match_agent_from_session_entity_type_name(cls,
                                                  session_entity_type_name):
        """Parses the agent from a session_entity_type resource.

        Args:
          session_entity_type_name (string): A fully-qualified path representing a session_entity_type
            resource.

        Returns:
          A string representing the agent.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('agent')

    @classmethod
    def match_session_from_session_entity_type_name(cls,
                                                    session_entity_type_name):
        """Parses the session from a session_entity_type resource.

        Args:
          session_entity_type_name (string): A fully-qualified path representing a session_entity_type
            resource.

        Returns:
          A string representing the session.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('session')

    @classmethod
    def match_entity_type_from_session_entity_type_name(
            cls, session_entity_type_name):
        """Parses the entity_type from a session_entity_type resource.

        Args:
          session_entity_type_name (string): A fully-qualified path representing a session_entity_type
            resource.

        Returns:
          A string representing the entity_type.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('entity_type')

    def __init__(self,
                 service_path=SERVICE_ADDRESS,
                 port=DEFAULT_SERVICE_PORT,
                 channel=None,
                 credentials=None,
                 ssl_credentials=None,
                 scopes=None,
                 client_config=None,
                 app_name=None,
                 app_version='',
                 lib_name=None,
                 lib_version='',
                 metrics_headers=()):
        """Constructor.

        Args:
          service_path (string): The domain name of the API remote host.
          port (int): The port on which to connect to the remote host.
          channel (:class:`grpc.Channel`): A ``Channel`` instance through
            which to make calls.
          credentials (object): The authorization credentials to attach to
            requests. These credentials identify this application to the
            service.
          ssl_credentials (:class:`grpc.ChannelCredentials`): A
            ``ChannelCredentials`` instance for use with an SSL-enabled
            channel.
          scopes (list[string]): A list of OAuth2 scopes to attach to requests.
          client_config (dict):
            A dictionary for call options for each method. See
            :func:`google.gax.construct_settings` for the structure of
            this data. Falls back to the default config if not specified
            or the specified config is missing data points.
          app_name (string): The name of the application calling
            the service. Recommended for analytics purposes.
          app_version (string): The version of the application calling
            the service. Recommended for analytics purposes.
          lib_name (string): The API library software used for calling
            the service. (Unless you are writing an API client itself,
            leave this as default.)
          lib_version (string): The API library software version used
            for calling the service. (Unless you are writing an API client
            itself, leave this as default.)
          metrics_headers (dict): A dictionary of values for tracking
            client library metrics. Ultimately serializes to a string
            (e.g. 'foo/1.2.3 bar/3.14.1'). This argument should be
            considered private.

        Returns:
          A ConversationServiceClient object.
        """
        # Unless the calling application specifically requested
        # OAuth scopes, request everything.
        if scopes is None:
            scopes = self._ALL_SCOPES

        # Initialize an empty client config, if none is set.
        if client_config is None:
            client_config = {}

        # Initialize metrics_headers as an ordered dictionary
        # (cuts down on cardinality of the resulting string slightly).
        metrics_headers = collections.OrderedDict(metrics_headers)
        metrics_headers['gl-python'] = platform.python_version()

        # The library may or may not be set, depending on what is
        # calling this client. Newer client libraries set the library name
        # and version.
        if lib_name:
            metrics_headers[lib_name] = lib_version

        # Finally, track the GAPIC package version.
        metrics_headers['gapic'] = pkg_resources.get_distribution(
            'gapic-google-cloud-conversation-v1alpha', ).version

        # Load the configuration defaults.
        default_client_config = json.loads(
            pkg_resources.resource_string(
                __name__, 'conversation_service_client_config.json').decode())
        defaults = api_callable.construct_settings(
            'google.cloud.conversation.v1alpha.ConversationService',
            default_client_config,
            client_config,
            config.STATUS_CODE_NAMES,
            metrics_headers=metrics_headers, )
        self.conversation_service_stub = config.create_stub(
            conversation_service_pb2.ConversationServiceStub,
            channel=channel,
            service_path=service_path,
            service_port=port,
            credentials=credentials,
            scopes=scopes,
            ssl_credentials=ssl_credentials)

        self._detect_intent = api_callable.create_api_call(
            self.conversation_service_stub.DetectIntent,
            settings=defaults['detect_intent'])
        self._streaming_detect_intent = api_callable.create_api_call(
            self.conversation_service_stub.StreamingDetectIntent,
            settings=defaults['streaming_detect_intent'])
        self._list_entity_types = api_callable.create_api_call(
            self.conversation_service_stub.ListEntityTypes,
            settings=defaults['list_entity_types'])
        self._get_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.GetEntityType,
            settings=defaults['get_entity_type'])
        self._create_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.CreateEntityType,
            settings=defaults['create_entity_type'])
        self._update_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.UpdateEntityType,
            settings=defaults['update_entity_type'])
        self._delete_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.DeleteEntityType,
            settings=defaults['delete_entity_type'])
        self._batch_update_entity_types = api_callable.create_api_call(
            self.conversation_service_stub.BatchUpdateEntityTypes,
            settings=defaults['batch_update_entity_types'])
        self._batch_create_entities = api_callable.create_api_call(
            self.conversation_service_stub.BatchCreateEntities,
            settings=defaults['batch_create_entities'])
        self._batch_update_entities = api_callable.create_api_call(
            self.conversation_service_stub.BatchUpdateEntities,
            settings=defaults['batch_update_entities'])
        self._batch_delete_entities = api_callable.create_api_call(
            self.conversation_service_stub.BatchDeleteEntities,
            settings=defaults['batch_delete_entities'])
        self._list_intents = api_callable.create_api_call(
            self.conversation_service_stub.ListIntents,
            settings=defaults['list_intents'])
        self._get_intent = api_callable.create_api_call(
            self.conversation_service_stub.GetIntent,
            settings=defaults['get_intent'])
        self._create_intent = api_callable.create_api_call(
            self.conversation_service_stub.CreateIntent,
            settings=defaults['create_intent'])
        self._update_intent = api_callable.create_api_call(
            self.conversation_service_stub.UpdateIntent,
            settings=defaults['update_intent'])
        self._delete_intent = api_callable.create_api_call(
            self.conversation_service_stub.DeleteIntent,
            settings=defaults['delete_intent'])
        self._get_session_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.GetSessionEntityType,
            settings=defaults['get_session_entity_type'])
        self._create_session_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.CreateSessionEntityType,
            settings=defaults['create_session_entity_type'])
        self._update_session_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.UpdateSessionEntityType,
            settings=defaults['update_session_entity_type'])
        self._delete_session_entity_type = api_callable.create_api_call(
            self.conversation_service_stub.DeleteSessionEntityType,
            settings=defaults['delete_session_entity_type'])
        self._list_contexts = api_callable.create_api_call(
            self.conversation_service_stub.ListContexts,
            settings=defaults['list_contexts'])
        self._get_context = api_callable.create_api_call(
            self.conversation_service_stub.GetContext,
            settings=defaults['get_context'])
        self._create_context = api_callable.create_api_call(
            self.conversation_service_stub.CreateContext,
            settings=defaults['create_context'])
        self._update_context = api_callable.create_api_call(
            self.conversation_service_stub.UpdateContext,
            settings=defaults['update_context'])
        self._delete_context = api_callable.create_api_call(
            self.conversation_service_stub.DeleteContext,
            settings=defaults['delete_context'])
        self._batch_create_contexts = api_callable.create_api_call(
            self.conversation_service_stub.BatchCreateContexts,
            settings=defaults['batch_create_contexts'])
        self._delete_all_contexts = api_callable.create_api_call(
            self.conversation_service_stub.DeleteAllContexts,
            settings=defaults['delete_all_contexts'])

    # Service calls
    def detect_intent(self,
                      session,
                      query_input,
                      query_params=None,
                      input_audio=None,
                      options=None):
        """
        Processes a natural language query and returns structured, actionable data
        as a result. This method is not idempotent, because it may cause contexts
        and session entity types to be updated, which in turn might affect
        results of future queries.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import detect_intent_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> session = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
          >>> query_input = detect_intent_pb2.QueryInput()
          >>> response = client.detect_intent(session, query_input)

        Args:
          session (string): Required. The name of the session this query is sent to.
            Format of the session name:
            ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session ID>``.
            It's up to the API caller to choose an appropriate session ID. It can be
            a random number or some type of user identifier (preferably hashed).
            The length of the session ID must not exceed 36 characters.
          query_input (:class:`google.cloud.proto.conversation.v1alpha.detect_intent_pb2.QueryInput`): Required. The input specification. It can be set to:

            1.  an audio config
            ::

                which instructs the speech recognizer how to process the speech audio,

            2.  a conversational query in the form of text, or

            3.  an event that specifies which intent to trigger.
          query_params (:class:`google.cloud.proto.conversation.v1alpha.detect_intent_pb2.QueryParameters`): Optional. The parameters of this query.
          input_audio (bytes): Optional. The natural language speech audio to be processed. This field
            should be populated iff ``query_input`` is set to an input audio config.
            A single request can contain up to 1 minute of speech audio data.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.detect_intent_pb2.DetectIntentResponse` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = detect_intent_pb2.DetectIntentRequest(
            session=session,
            query_input=query_input,
            query_params=query_params,
            input_audio=input_audio)
        return self._detect_intent(request, options)

    def streaming_detect_intent(self, requests, options=None):
        """
        Processes a natural language query in audio format in a streaming fashion
        and returns structured, actionable data as a result. This method is only
        available via the gRPC API (not REST).

        EXPERIMENTAL: This method interface might change in the future.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import detect_intent_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> query_params = detect_intent_pb2.StreamingQueryParameters()
          >>> query_input = detect_intent_pb2.StreamingQueryInput()
          >>> request = detect_intent_pb2.StreamingDetectIntentRequest(query_params=query_params, query_input=query_input)
          >>> requests = [request]
          >>> for element in client.streaming_detect_intent(requests):
          >>>     # process element
          >>>     pass

        Args:
          requests (iterator[:class:`google.cloud.proto.conversation.v1alpha.detect_intent_pb2.StreamingDetectIntentRequest`]): The input objects.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          iterator[:class:`google.cloud.proto.conversation.v1alpha.detect_intent_pb2.StreamingDetectIntentResponse`].

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        return self._streaming_detect_intent(requests, options)

    def list_entity_types(self, parent, language_code=None, options=None):
        """
        Lists all entity types in the specified agent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.agent_path('[PROJECT]', '[AGENT]')
          >>> response = client.list_entity_types(parent)

        Args:
          parent (string): Required. The name of the agent to list entity types from.
            Format: ``projects/<Project ID>/agents/<Agent ID>``.
          language_code (string): Optional. The language to list entity synonyms for. If not specified,
            the agent's default language is used.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.ListEntityTypesResponse` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.ListEntityTypesRequest(
            parent=parent, language_code=language_code)
        return self._list_entity_types(request, options)

    def get_entity_type(self, name, language_code=None, options=None):
        """
        Retrieves the specified entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')
          >>> response = client.get_entity_type(name)

        Args:
          name (string): Required. The name of the entity type to retrieve.
            Format: ``projects/<Project ID>/agents/<Agent
            ID>/entitityTypes/<Entity Type ID>``.
          language_code (string): Optional. The language to list entity synonyms for. If not specified,
            the agent's default language is used.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.GetEntityTypeRequest(
            name=name, language_code=language_code)
        return self._get_entity_type(request, options)

    def create_entity_type(self,
                           parent,
                           entity_type,
                           language_code=None,
                           options=None):
        """
        Creates a new entity type in the specified agent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import entity_type_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.agent_path('[PROJECT]', '[AGENT]')
          >>> entity_type = entity_type_pb2.EntityType()
          >>> response = client.create_entity_type(parent, entity_type)

        Args:
          parent (string): Required. The name of the agent to create a new entity type in.
            Format: ``projects/<Project ID>/agents/<Agent ID>``.
          entity_type (:class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType`): Required. The entity resource to create. ``EntityType.name`` must be
            empty.
          language_code (string): Optional.  The language of entity synonyms defined in ``entity_type``. If not
            specified, the agent's default language is used.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.CreateEntityTypeRequest(
            parent=parent,
            entity_type=entity_type,
            language_code=language_code)
        return self._create_entity_type(request, options)

    def update_entity_type(self, entity_type, language_code=None,
                           options=None):
        """
        Updates the specified entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import entity_type_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> entity_type = entity_type_pb2.EntityType()
          >>> response = client.update_entity_type(entity_type)

        Args:
          entity_type (:class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType`): Required. The entity type to update.
          language_code (string): Optional. The language of entity synonyms defined in ``entity_type``. If not
            specified, the agent's default language is assumed.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.UpdateEntityTypeRequest(
            entity_type=entity_type, language_code=language_code)
        return self._update_entity_type(request, options)

    def delete_entity_type(self, name, options=None):
        """
        Deletes the specified entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')
          >>> client.delete_entity_type(name)

        Args:
          name (string): Required. The name of the entity type to delete.
            Format: ``projects/<Project ID>/agents/<Agent
            ID>/entityTypes/<Entity Type ID>``.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.DeleteEntityTypeRequest(name=name)
        self._delete_entity_type(request, options)

    def batch_update_entity_types(self,
                                  parent,
                                  entity_types,
                                  language_code=None,
                                  options=None):
        """
        Updates or creates multiple entity types in the specified agent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.agent_path('[PROJECT]', '[AGENT]')
          >>> entity_types = []
          >>> response = client.batch_update_entity_types(parent, entity_types)

        Args:
          parent (string): Required. The name of the agent to update or create entity types in.
            Format: ``projects/<Project ID>/agents/<Agent ID>``.
          entity_types (list[:class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType`]): Required. The collection of entity types to update or create.
          language_code (string): Optional. The language of entity synonyms defined in ``entity_types``. If not
            specified, the agent's default language is assumed.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.BatchUpdateEntityTypesResponse` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.BatchUpdateEntityTypesRequest(
            parent=parent,
            entity_types=entity_types,
            language_code=language_code)
        return self._batch_update_entity_types(request, options)

    def batch_create_entities(self,
                              parent,
                              entities,
                              language_code=None,
                              options=None):
        """
        Creates multiple new entities in the specified entity type (extends the
        existing collection of entries).

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')
          >>> entities = []
          >>> client.batch_create_entities(parent, entities)

        Args:
          parent (string): Required. The name of the entity type to create entities in.
            Format: ``projects/<Project ID>/agents/<Agent
            ID>/entityTypes/<Entity Type ID>``.
          entities (list[:class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType.Entity`]): Required. The collection of entities to create.
          language_code (string): Optional. The language of entity synonyms defined in ``entities``. If not
            specified, the agent's default language is assumed.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.BatchCreateEntitiesRequest(
            parent=parent, entities=entities, language_code=language_code)
        self._batch_create_entities(request, options)

    def batch_update_entities(self,
                              parent,
                              entities,
                              language_code=None,
                              options=None):
        """
        Updates entities in the specified entity type (replaces the existing
        collection of entries).

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')
          >>> entities = []
          >>> client.batch_update_entities(parent, entities)

        Args:
          parent (string): Required. The name of the entity type to update the entities in.
            Format: ``projects/<Project ID>/agents/<Agent
            ID>/entityTypes/<Entity Type ID>``.
          entities (list[:class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType.Entity`]): Required. The collection of new entities to replace the existing entities.
          language_code (string): Optional. The language of entity synonyms defined in ``entities``. If not
            specified, the agent's default language is assumed.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.BatchUpdateEntitiesRequest(
            parent=parent, entities=entities, language_code=language_code)
        self._batch_update_entities(request, options)

    def batch_delete_entities(self, parent, entities, options=None):
        """
        Deletes entities in the specified entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')
          >>> entities = []
          >>> client.batch_delete_entities(parent, entities)

        Args:
          parent (string): Required. The name of the entity type to delete entries for.
            Format: ``projects/<Project ID>/agents/<Agent
            ID>/entityTypes/<Entity Type ID>``.
          entities (list[:class:`google.cloud.proto.conversation.v1alpha.entity_type_pb2.EntityType.Entity`]): Required. The collection of entities to delete. Only the canonical ``value``
            must be filled in.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = entity_type_pb2.BatchDeleteEntitiesRequest(
            parent=parent, entities=entities)
        self._batch_delete_entities(request, options)

    def list_intents(self, parent, language_code=None, options=None):
        """
        Lists all intents in the specified agent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.agent_path('[PROJECT]', '[AGENT]')
          >>> response = client.list_intents(parent)

        Args:
          parent (string): Required. The name of the agent to list intents from.
            Format: ``projects/<Project ID>/agents/<Agent ID>``.
          language_code (string): Optional. The language to list training phrases, parameters and rich
            messages for. If not specified, the agent's default language is used.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.intent_pb2.ListIntentsResponse` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = intent_pb2.ListIntentsRequest(
            parent=parent, language_code=language_code)
        return self._list_intents(request, options)

    def get_intent(self,
                   name,
                   intent_view=None,
                   language_code=None,
                   options=None):
        """
        Retrieves the specified intent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.intent_path('[PROJECT]', '[AGENT]', '[INTENT]')
          >>> response = client.get_intent(name)

        Args:
          name (string): Required. The name of the intent to retrieve.
            Format: ``projects/<Project ID>/agents/<Agent ID>/intents/<Intent ID>``.
          intent_view (enum :class:`google.cloud.gapic.conversation.v1alpha.enums.IntentView`): Optional. The resource view to apply to the returned intent.
          language_code (string): Optional. The language to list training phrases, parameters and rich
            messages for. If not specified, the agent's default language is used.
            `More than a dozen languages <https://api.ai/docs/reference/language>`_
            are currently supported.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.intent_pb2.Intent` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = intent_pb2.GetIntentRequest(
            name=name, intent_view=intent_view, language_code=language_code)
        return self._get_intent(request, options)

    def create_intent(self,
                      parent,
                      intent,
                      language_code=None,
                      intent_view=None,
                      options=None):
        """
        Creates a new intent in the specified agent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import intent_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.agent_path('[PROJECT]', '[AGENT]')
          >>> intent = intent_pb2.Intent()
          >>> response = client.create_intent(parent, intent)

        Args:
          parent (string): Required. The name of the agent to create the intent in.
            Format: ``projects/<Project ID>/agents/<Agent ID>``.
          intent (:class:`google.cloud.proto.conversation.v1alpha.intent_pb2.Intent`): Required. The intent to create.
          language_code (string): Optional. The language of training phrases, parameters and rich messages
            in ``intent``. If not specified, the agent's default language is assumed.
          intent_view (enum :class:`google.cloud.gapic.conversation.v1alpha.enums.IntentView`): Optional. The resource view to apply to the returned intent.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.intent_pb2.Intent` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = intent_pb2.CreateIntentRequest(
            parent=parent,
            intent=intent,
            language_code=language_code,
            intent_view=intent_view)
        return self._create_intent(request, options)

    def update_intent(self,
                      intent,
                      language_code=None,
                      intent_view=None,
                      options=None):
        """
        Updates the specified intent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import intent_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> intent = intent_pb2.Intent()
          >>> response = client.update_intent(intent)

        Args:
          intent (:class:`google.cloud.proto.conversation.v1alpha.intent_pb2.Intent`): Required. The intent to update.
          language_code (string): Optional. The language of training phrases, parameters and rich messages
            in ``intent``. If not specified, the agent's default language is assumed.
          intent_view (enum :class:`google.cloud.gapic.conversation.v1alpha.enums.IntentView`): Optional. The resource view to apply to the returned intent.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.intent_pb2.Intent` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = intent_pb2.UpdateIntentRequest(
            intent=intent,
            language_code=language_code,
            intent_view=intent_view)
        return self._update_intent(request, options)

    def delete_intent(self, name, options=None):
        """
        Deletes the specified intent.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.intent_path('[PROJECT]', '[AGENT]', '[INTENT]')
          >>> client.delete_intent(name)

        Args:
          name (string): Required. The name of the intent to delete.
            Format: ``projects/<Project ID>/agents/<Agent ID>/intents/<Intent ID>``.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = intent_pb2.DeleteIntentRequest(name=name)
        self._delete_intent(request, options)

    def get_session_entity_type(self, name, options=None):
        """
        Retrieves the specified session entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.session_entity_type_path('[PROJECT]', '[AGENT]', '[SESSION]', '[ENTITY_TYPE]')
          >>> response = client.get_session_entity_type(name)

        Args:
          name (string): Required. The name of the session entity type to retrieve.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session
            ID>/entityTypes/<Entity Type Display Name>``.
            ``Entity Type Name`` must be the display name of the entity type and cannot
            be the entity type ID.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.session_entity_type_pb2.SessionEntityType` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = session_entity_type_pb2.GetSessionEntityTypeRequest(
            name=name)
        return self._get_session_entity_type(request, options)

    def create_session_entity_type(self,
                                   parent,
                                   session_entity_type,
                                   options=None):
        """
        Creates a new session entity type in the specified session.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import session_entity_type_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
          >>> session_entity_type = session_entity_type_pb2.SessionEntityType()
          >>> response = client.create_session_entity_type(parent, session_entity_type)

        Args:
          parent (string): Required. The name of the session to create a new entity type in.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session ID>``.
          session_entity_type (:class:`google.cloud.proto.conversation.v1alpha.session_entity_type_pb2.SessionEntityType`): Required. The session entity type to create.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.session_entity_type_pb2.SessionEntityType` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = session_entity_type_pb2.CreateSessionEntityTypeRequest(
            parent=parent, session_entity_type=session_entity_type)
        return self._create_session_entity_type(request, options)

    def update_session_entity_type(self, session_entity_type, options=None):
        """
        Updates the specified session entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import session_entity_type_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> session_entity_type = session_entity_type_pb2.SessionEntityType()
          >>> response = client.update_session_entity_type(session_entity_type)

        Args:
          session_entity_type (:class:`google.cloud.proto.conversation.v1alpha.session_entity_type_pb2.SessionEntityType`): Required. The session entity type to update.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.session_entity_type_pb2.SessionEntityType` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = session_entity_type_pb2.UpdateSessionEntityTypeRequest(
            session_entity_type=session_entity_type)
        return self._update_session_entity_type(request, options)

    def delete_session_entity_type(self, name, options=None):
        """
        Deletes the specified session entity type.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.session_entity_type_path('[PROJECT]', '[AGENT]', '[SESSION]', '[ENTITY_TYPE]')
          >>> client.delete_session_entity_type(name)

        Args:
          name (string): Required. The name of the session entity type to delete.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session
            ID>/entityTypes/<Entity Type Display Name>``.
            ``Entity Type Name`` must be the display name of the entity type and cannot
            be the entity type ID.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = session_entity_type_pb2.DeleteSessionEntityTypeRequest(
            name=name)
        self._delete_session_entity_type(request, options)

    def list_contexts(self, parent, options=None):
        """
        Lists contexts which are active in the specified session.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
          >>> response = client.list_contexts(parent)

        Args:
          parent (string): Required. The name of the session that contains the active contexts.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session ID>``.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.context_pb2.ListContextsResponse` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.ListContextsRequest(parent=parent)
        return self._list_contexts(request, options)

    def get_context(self, name, options=None):
        """
        Retrieves the specified context.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.context_path('[PROJECT]', '[AGENT]', '[SESSION]', '[CONTEXT]')
          >>> response = client.get_context(name)

        Args:
          name (string): Required. The name of the context to retrieve.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session
            ID>/contexts/<Context ID>``.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.context_pb2.Context` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.GetContextRequest(name=name)
        return self._get_context(request, options)

    def create_context(self, parent, context, options=None):
        """
        Creates a new context in the specified session.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import context_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
          >>> context = context_pb2.Context()
          >>> response = client.create_context(parent, context)

        Args:
          parent (string): Required. The name of the session to create a new context in.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session ID>``.
          context (:class:`google.cloud.proto.conversation.v1alpha.context_pb2.Context`): Required. The context to create.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.context_pb2.Context` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.CreateContextRequest(
            parent=parent, context=context)
        return self._create_context(request, options)

    def update_context(self, context, options=None):
        """
        Updates the specified context.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> from google.cloud.proto.conversation.v1alpha import context_pb2
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> context = context_pb2.Context()
          >>> response = client.update_context(context)

        Args:
          context (:class:`google.cloud.proto.conversation.v1alpha.context_pb2.Context`): Required. The context to update.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.context_pb2.Context` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.UpdateContextRequest(context=context)
        return self._update_context(request, options)

    def delete_context(self, name, options=None):
        """
        Deletes the specified context.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> name = client.context_path('[PROJECT]', '[AGENT]', '[SESSION]', '[CONTEXT]')
          >>> client.delete_context(name)

        Args:
          name (string): Required. The name of the context to delete.
            Format: \"projects/<Project ID>/agents/<Agent ID>/sessions/<Session
            ID>/contexts/<Context ID>\".
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.DeleteContextRequest(name=name)
        self._delete_context(request, options)

    def batch_create_contexts(self, parent, contexts, options=None):
        """
        Creates multiple new contexts in the specified session.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
          >>> contexts = []
          >>> response = client.batch_create_contexts(parent, contexts)

        Args:
          parent (string): Required. The name of the session to create the new contexts in.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session ID>``.
          contexts (list[:class:`google.cloud.proto.conversation.v1alpha.context_pb2.Context`]): Required. The collection of contexts to create.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Returns:
          A :class:`google.cloud.proto.conversation.v1alpha.context_pb2.BatchCreateContextsResponse` instance.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.BatchCreateContextsRequest(
            parent=parent, contexts=contexts)
        return self._batch_create_contexts(request, options)

    def delete_all_contexts(self, parent, options=None):
        """
        Deletes all active context in the specified session.

        Example:
          >>> from google.cloud.gapic.conversation.v1alpha import conversation_service_client
          >>> client = conversation_service_client.ConversationServiceClient()
          >>> parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
          >>> client.delete_all_contexts(parent)

        Args:
          parent (string): Required. The name of the session to delete all contexts from.
            Format: ``projects/<Project ID>/agents/<Agent ID>/sessions/<Session ID>``.
          options (:class:`google.gax.CallOptions`): Overrides the default
            settings for this call, e.g, timeout, retries etc.

        Raises:
          :exc:`google.gax.errors.GaxError` if the RPC is aborted.
          :exc:`ValueError` if the parameters are invalid.
        """
        # Create the request object.
        request = context_pb2.DeleteAllContextsRequest(parent=parent)
        self._delete_all_contexts(request, options)
