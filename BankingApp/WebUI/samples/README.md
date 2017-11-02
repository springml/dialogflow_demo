<img src="https://avatars2.githubusercontent.com/u/2810941?v=3&s=96" alt="Google Cloud Platform logo" title="Google Cloud Platform" align="right" height="96" width="96"/>

# Google Cloud Conversation Engine API Python Samples

The [Cloud Conversation Engine](https://cloud.google.com/conversation/docs/) is
an enterprise-grade NLU platform that makes it easy for developers to design and
integrate conversational user interfaces into mobile apps, web applications,
devices, and bots.

This sample sets up an agent to handle pizza delivery conversations and shows
how to query intents.

## Table of Contents

*   [Setup](#setup)
*   [Samples](#samples)
    *   [Sample Agent](#sample-agent)
    *   [Detecting intents](#detecting-intents)
*   [Running the Tests](#running-the-tests)

## Prerequisite

1.  Install [Pip][pip].

1.  Change directory to the samples folder:

        cd samples

1.  Create a new Google Cloud project.

1.  Enable Cloud Conversation Engine API for your Google Cloud project by doing
    the following:

    *   Go to API Manager > Library.
    *   Search for "Cloud Conversation Engine API".
    *   Click the API in the search results, then click "ENABLE" button.

    If you don't see Cloud Conversation Engine API, please contact
    cloud-conversation-engine-users@googlegroups.com.

1.  Create an api.ai agent and associate it with the Google Cloud project with
    Cloud Conversation Engine API enabled:

    *   Go to https://api.ai. Log in or sign up.
    *   Create an agent.
    *   On the [create agent UI][create_agent], set Google project to the Google
        Cloud project with Cloud Conversation Engine API enabled.

    We recommend using the [sample agent](#sample-agent).

1.  Set the `GCLOUD_PROJECT` environment variable to the Google Project ID
    associated with the agent:

    Linux:

        export GCLOUD_PROJECT=your-project-id

    Windows:

        set GCLOUD_PROJECT=your-project-id

    Windows (PowerShell):

        $env:GCLOUD_PROJECT="your-project-id"

1.  Obtain service account authentication credentials.

    Cloud Conversation Engine requires using service accounts for
    authentication. Follow the instructions below to create a service account
    and use it for authentication:

    *   Go to API Manager -> Credentials
    *   Click "Create Credentials", and create a service account or [click
        here](https://console.cloud.google.com/project/_/apiui/credential/serviceaccount)
    *   Choose "Service Account key" in the pull down menu
    *   In the Service Account pulldown, choose "New service account"
    *   Choose name for "service account name" e.g., "cce-test-account"
    *   Choose role "Project > Owner" for service account
    *   Mark "JSON" as the key type
    *   Click "Create"
    *   Download the JSON for this service account, and set the
        `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to the
        file containing the JSON credentials. Set the
        `GOOGLE_APPLICATION_CREDENTIALS` environment variable:

    Linux:

        export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account_file.json

    Windows:

        set GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account_file.json

    Windows (PowerShell):

        $env:GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account_file.json"

    __Note for code running on GCE, GAE, or other environments:__

    On Google App Engine, the credentials should be found automatically.

    On Google Compute Engine, the credentials should be found automatically, but
    require that you create the instance with the correct scopes.

        gcloud compute instances create --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly" test-instance

    If you did not create the instance with the right scopes, you can still
    upload a JSON service account and set `GOOGLE_APPLICATION_CREDENTIALS` as
    described.

    Read more about [Google Cloud Platform Authentication][gcp_auth].

1.  Install dependencies in a virtualenv:

    ```shell
    cd ..
    source install_client_library.sh
    cd -
    ```

[pip]: https://pip.pypa.io
[auth_command]: https://cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/login
[create_agent]: https://api.ai/docs/agents#creating
[gcp_auth]: https://cloud.google.com/docs/authentication#projects_and_resources

## Samples

### Sample agent

The [Sample Agent](./SampleAgent.zip) zip file contains an agent for a pizza
ordering and delivery service. To use the sample agent, go to the [Export and
Import][export_and_import] tab of the agent settings page. Click "Restore from
zip" and upload the zip file.

Use the [intent detection samples](#detecting-intents) to test this agent.

[export_and_import]: https://api.ai/docs/agents#export

### Detecting intents

```
usage: python detect_intent.py [-h] [--project_id PROJECT_ID]
                        [--session_id SESSION_ID]
                        [--language_code LANGUAGE_CODE] [--encoding ENCODING]
                        [--sample_rate_hertz SAMPLE_RATE_HERTZ]
                        {text,event,audio,stream} inputs [inputs ...]

Cloud Conversation Engine API DetectIntent() Python sample.

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

positional arguments:
  {text,event,audio,stream}
                        Command to run.
  inputs                Inputs for the command.

optional arguments:
  -h, --help            show this help message and exit
  --project_id PROJECT_ID
                        Project/agent id. Defaults to the value of the
                        GCLOUD_PROJECT or GOOGLE_CLOUD_PROJECT environment
                        variables.
  --session_id SESSION_ID
                        Identifier of the DetectIntent session. Defaults to a
                        random UUID.
  --language_code LANGUAGE_CODE
                        Language code of the query. Defaults to "en-US".
  --encoding ENCODING   Encoding of the input audio. Defaults to
                        AUDIO_ENCODING_LINEAR16. See
                        https://cloud.google.com/speech/docs/basics#audio-
                        encodings.
  --sample_rate_hertz SAMPLE_RATE_HERTZ
                        Sample rate of the input audio. Only required if the
                        input audio is in raw format. See
                        https://cloud.google.com/speech/docs/basics#sample-
                        rates.
```

## Running the Tests

1.  Set **GCLOUD_PROJECT** and **GOOGLE_APPLICATION_CREDENTIALS** environment
    variables.

1.  Run the tests:

    ```shell
    python *_test.py
    ```
