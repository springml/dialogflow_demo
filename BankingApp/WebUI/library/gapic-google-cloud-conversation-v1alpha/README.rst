Python Client for Cloud Conversation Engine API (`Alpha`_)
==================================================================================================

`Cloud Conversation Engine API`_: Cloud Conversation Engine is an enterprise-grade NLU platform that makes it
easy for developers to design and integrate conversational user interfaces
into mobile apps, web applications, devices, and bots.

- `Client Library Documentation`_
- `Product Documentation`_

.. _Alpha: https://github.com/GoogleCloudPlatform/google-cloud-python/blob/master/README.rst
.. _Cloud Conversation Engine API: https://cloud.google.com/conversation
.. _Client Library Documentation: https://googlecloudplatform.github.io/google-cloud-python/stable/conversation-usage
.. _Product Documentation:  https://cloud.google.com/conversation

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable the Cloud Conversation Engine API.`_
3. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable the Cloud Conversation Engine API.:  https://cloud.google.com/conversation
.. _Setup Authentication.: https://googlecloudplatform.github.io/google-cloud-python/stable/google-cloud-auth

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install gapic-google-cloud-conversation-v1alpha


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install gapic-google-cloud-conversation-v1alpha

Preview
~~~~~~~

ConversationServiceClient
^^^^^^^^^^^^^^^^^^^^^^

.. code:: py

  from google.cloud.gapic.conversation.v1alpha import conversation_service_client
  from google.cloud.proto.conversation.v1alpha import detect_intent_pb2
  client = conversation_service_client.ConversationServiceClient()
  session = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
  query_input = detect_intent_pb2.QueryInput()
  response = client.detect_intent(session, query_input)

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud Conversation Engine API
   API to see other available methods on the client.
-  Read the `Cloud Conversation Engine API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `repository’s main README`_ to see the full list of Cloud
   APIs that we cover.

.. _Cloud Conversation Engine API Product documentation:  https://cloud.google.com/conversation
.. _repository’s main README: https://github.com/GoogleCloudPlatform/google-cloud-python/blob/master/README.rst