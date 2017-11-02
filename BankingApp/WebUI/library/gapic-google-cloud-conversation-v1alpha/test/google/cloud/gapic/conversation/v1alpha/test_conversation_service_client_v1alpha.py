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
"""Unit tests."""

import mock
import unittest

from google.gax import errors

from google.cloud.gapic.conversation.v1alpha import conversation_service_client
from google.cloud.proto.conversation.v1alpha import context_pb2
from google.cloud.proto.conversation.v1alpha import detect_intent_pb2
from google.cloud.proto.conversation.v1alpha import entity_type_pb2
from google.cloud.proto.conversation.v1alpha import intent_pb2
from google.cloud.proto.conversation.v1alpha import session_entity_type_pb2
from google.protobuf import empty_pb2


class CustomException(Exception):
    pass


class TestConversationServiceClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_detect_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        session = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        query_input = detect_intent_pb2.QueryInput()

        # Mock response
        response_id = 'responseId1847552473'
        expected_response = detect_intent_pb2.DetectIntentResponse(
            response_id=response_id)
        grpc_stub.DetectIntent.return_value = expected_response

        response = client.detect_intent(session, query_input)
        self.assertEqual(expected_response, response)

        grpc_stub.DetectIntent.assert_called_once()
        args, kwargs = grpc_stub.DetectIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = detect_intent_pb2.DetectIntentRequest(
            session=session, query_input=query_input)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_detect_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        session = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        query_input = detect_intent_pb2.QueryInput()

        # Mock exception response
        grpc_stub.DetectIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.detect_intent, session,
                          query_input)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_streaming_detect_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        query_params = detect_intent_pb2.StreamingQueryParameters()
        query_input = detect_intent_pb2.StreamingQueryInput()
        request = detect_intent_pb2.StreamingDetectIntentRequest(
            query_params=query_params, query_input=query_input)
        requests = [request]

        # Mock response
        response_id = 'responseId1847552473'
        expected_response = detect_intent_pb2.StreamingDetectIntentResponse(
            response_id=response_id)
        grpc_stub.StreamingDetectIntent.return_value = iter(
            [expected_response])

        response = client.streaming_detect_intent(requests)
        resources = list(response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response, resources[0])

        grpc_stub.StreamingDetectIntent.assert_called_once()
        args, kwargs = grpc_stub.StreamingDetectIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_requests = args[0]
        self.assertEqual(1, len(actual_requests))
        actual_request = list(actual_requests)[0]
        self.assertEqual(request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_streaming_detect_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        query_params = detect_intent_pb2.StreamingQueryParameters()
        query_input = detect_intent_pb2.StreamingQueryInput()
        request = detect_intent_pb2.StreamingDetectIntentRequest(
            query_params=query_params, query_input=query_input)
        requests = [request]

        # Mock exception response
        grpc_stub.StreamingDetectIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.streaming_detect_intent,
                          requests)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_entity_types(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')

        # Mock response
        expected_response = entity_type_pb2.ListEntityTypesResponse()
        grpc_stub.ListEntityTypes.return_value = expected_response

        response = client.list_entity_types(parent)
        self.assertEqual(expected_response, response)

        grpc_stub.ListEntityTypes.assert_called_once()
        args, kwargs = grpc_stub.ListEntityTypes.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.ListEntityTypesRequest(
            parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_entity_types_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')

        # Mock exception response
        grpc_stub.ListEntityTypes.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.list_entity_types, parent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')

        # Mock response
        name_2 = 'name2-1052831874'
        display_name = 'displayName1615086568'
        expected_response = entity_type_pb2.EntityType(
            name=name_2, display_name=display_name)
        grpc_stub.GetEntityType.return_value = expected_response

        response = client.get_entity_type(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetEntityType.assert_called_once()
        args, kwargs = grpc_stub.GetEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.GetEntityTypeRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.GetEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_entity_type, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        entity_type = entity_type_pb2.EntityType()

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        expected_response = entity_type_pb2.EntityType(
            name=name, display_name=display_name)
        grpc_stub.CreateEntityType.return_value = expected_response

        response = client.create_entity_type(parent, entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateEntityType.assert_called_once()
        args, kwargs = grpc_stub.CreateEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.CreateEntityTypeRequest(
            parent=parent, entity_type=entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        entity_type = entity_type_pb2.EntityType()

        # Mock exception response
        grpc_stub.CreateEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_entity_type, parent,
                          entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        entity_type = entity_type_pb2.EntityType()

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        expected_response = entity_type_pb2.EntityType(
            name=name, display_name=display_name)
        grpc_stub.UpdateEntityType.return_value = expected_response

        response = client.update_entity_type(entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateEntityType.assert_called_once()
        args, kwargs = grpc_stub.UpdateEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.UpdateEntityTypeRequest(
            entity_type=entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        entity_type = entity_type_pb2.EntityType()

        # Mock exception response
        grpc_stub.UpdateEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_entity_type,
                          entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')

        client.delete_entity_type(name)

        grpc_stub.DeleteEntityType.assert_called_once()
        args, kwargs = grpc_stub.DeleteEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.DeleteEntityTypeRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[AGENT]', '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.DeleteEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_entity_type, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entity_types(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        entity_types = []

        # Mock response
        expected_response = entity_type_pb2.BatchUpdateEntityTypesResponse()
        grpc_stub.BatchUpdateEntityTypes.return_value = expected_response

        response = client.batch_update_entity_types(parent, entity_types)
        self.assertEqual(expected_response, response)

        grpc_stub.BatchUpdateEntityTypes.assert_called_once()
        args, kwargs = grpc_stub.BatchUpdateEntityTypes.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchUpdateEntityTypesRequest(
            parent=parent, entity_types=entity_types)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entity_types_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        entity_types = []

        # Mock exception response
        grpc_stub.BatchUpdateEntityTypes.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.batch_update_entity_types,
                          parent, entity_types)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_create_entities(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[AGENT]',
                                         '[ENTITY_TYPE]')
        entities = []

        client.batch_create_entities(parent, entities)

        grpc_stub.BatchCreateEntities.assert_called_once()
        args, kwargs = grpc_stub.BatchCreateEntities.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchCreateEntitiesRequest(
            parent=parent, entities=entities)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_create_entities_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[AGENT]',
                                         '[ENTITY_TYPE]')
        entities = []

        # Mock exception response
        grpc_stub.BatchCreateEntities.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.batch_create_entities,
                          parent, entities)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entities(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[AGENT]',
                                         '[ENTITY_TYPE]')
        entities = []

        client.batch_update_entities(parent, entities)

        grpc_stub.BatchUpdateEntities.assert_called_once()
        args, kwargs = grpc_stub.BatchUpdateEntities.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchUpdateEntitiesRequest(
            parent=parent, entities=entities)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entities_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[AGENT]',
                                         '[ENTITY_TYPE]')
        entities = []

        # Mock exception response
        grpc_stub.BatchUpdateEntities.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.batch_update_entities,
                          parent, entities)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_entities(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[AGENT]',
                                         '[ENTITY_TYPE]')
        entities = []

        client.batch_delete_entities(parent, entities)

        grpc_stub.BatchDeleteEntities.assert_called_once()
        args, kwargs = grpc_stub.BatchDeleteEntities.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchDeleteEntitiesRequest(
            parent=parent, entities=entities)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_entities_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[AGENT]',
                                         '[ENTITY_TYPE]')
        entities = []

        # Mock exception response
        grpc_stub.BatchDeleteEntities.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.batch_delete_entities,
                          parent, entities)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_intents(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')

        # Mock response
        expected_response = intent_pb2.ListIntentsResponse()
        grpc_stub.ListIntents.return_value = expected_response

        response = client.list_intents(parent)
        self.assertEqual(expected_response, response)

        grpc_stub.ListIntents.assert_called_once()
        args, kwargs = grpc_stub.ListIntents.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.ListIntentsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_intents_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')

        # Mock exception response
        grpc_stub.ListIntents.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.list_intents, parent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[AGENT]', '[INTENT]')

        # Mock response
        name_2 = 'name2-1052831874'
        display_name = 'displayName1615086568'
        priority = -1165461084
        is_fallback = False
        ml_enabled = False
        expected_response = intent_pb2.Intent(
            name=name_2,
            display_name=display_name,
            priority=priority,
            is_fallback=is_fallback,
            ml_enabled=ml_enabled)
        grpc_stub.GetIntent.return_value = expected_response

        response = client.get_intent(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetIntent.assert_called_once()
        args, kwargs = grpc_stub.GetIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.GetIntentRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[AGENT]', '[INTENT]')

        # Mock exception response
        grpc_stub.GetIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_intent, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        intent = intent_pb2.Intent()

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        priority = -1165461084
        is_fallback = False
        ml_enabled = False
        expected_response = intent_pb2.Intent(
            name=name,
            display_name=display_name,
            priority=priority,
            is_fallback=is_fallback,
            ml_enabled=ml_enabled)
        grpc_stub.CreateIntent.return_value = expected_response

        response = client.create_intent(parent, intent)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateIntent.assert_called_once()
        args, kwargs = grpc_stub.CreateIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.CreateIntentRequest(
            parent=parent, intent=intent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        intent = intent_pb2.Intent()

        # Mock exception response
        grpc_stub.CreateIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_intent, parent,
                          intent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        intent = intent_pb2.Intent()

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        priority = -1165461084
        is_fallback = False
        ml_enabled = False
        expected_response = intent_pb2.Intent(
            name=name,
            display_name=display_name,
            priority=priority,
            is_fallback=is_fallback,
            ml_enabled=ml_enabled)
        grpc_stub.UpdateIntent.return_value = expected_response

        response = client.update_intent(intent)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateIntent.assert_called_once()
        args, kwargs = grpc_stub.UpdateIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.UpdateIntentRequest(intent=intent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        intent = intent_pb2.Intent()

        # Mock exception response
        grpc_stub.UpdateIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_intent, intent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[AGENT]', '[INTENT]')

        client.delete_intent(name)

        grpc_stub.DeleteIntent.assert_called_once()
        args, kwargs = grpc_stub.DeleteIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.DeleteIntentRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[AGENT]', '[INTENT]')

        # Mock exception response
        grpc_stub.DeleteIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_intent, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[AGENT]',
                                               '[SESSION]', '[ENTITY_TYPE]')

        # Mock response
        name_2 = 'name2-1052831874'
        expected_response = session_entity_type_pb2.SessionEntityType(
            name=name_2)
        grpc_stub.GetSessionEntityType.return_value = expected_response

        response = client.get_session_entity_type(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.GetSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.GetSessionEntityTypeRequest(
            name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[AGENT]',
                                               '[SESSION]', '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.GetSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_session_entity_type,
                          name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        session_entity_type = session_entity_type_pb2.SessionEntityType()

        # Mock response
        name = 'name3373707'
        expected_response = session_entity_type_pb2.SessionEntityType(
            name=name)
        grpc_stub.CreateSessionEntityType.return_value = expected_response

        response = client.create_session_entity_type(parent,
                                                     session_entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.CreateSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.CreateSessionEntityTypeRequest(
            parent=parent, session_entity_type=session_entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        session_entity_type = session_entity_type_pb2.SessionEntityType()

        # Mock exception response
        grpc_stub.CreateSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_session_entity_type,
                          parent, session_entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        session_entity_type = session_entity_type_pb2.SessionEntityType()

        # Mock response
        name = 'name3373707'
        expected_response = session_entity_type_pb2.SessionEntityType(
            name=name)
        grpc_stub.UpdateSessionEntityType.return_value = expected_response

        response = client.update_session_entity_type(session_entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.UpdateSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.UpdateSessionEntityTypeRequest(
            session_entity_type=session_entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        session_entity_type = session_entity_type_pb2.SessionEntityType()

        # Mock exception response
        grpc_stub.UpdateSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_session_entity_type,
                          session_entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[AGENT]',
                                               '[SESSION]', '[ENTITY_TYPE]')

        client.delete_session_entity_type(name)

        grpc_stub.DeleteSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.DeleteSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.DeleteSessionEntityTypeRequest(
            name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[AGENT]',
                                               '[SESSION]', '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.DeleteSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_session_entity_type,
                          name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_contexts(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')

        # Mock response
        expected_response = context_pb2.ListContextsResponse()
        grpc_stub.ListContexts.return_value = expected_response

        response = client.list_contexts(parent)
        self.assertEqual(expected_response, response)

        grpc_stub.ListContexts.assert_called_once()
        args, kwargs = grpc_stub.ListContexts.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.ListContextsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_contexts_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')

        # Mock exception response
        grpc_stub.ListContexts.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.list_contexts, parent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[AGENT]', '[SESSION]',
                                   '[CONTEXT]')

        # Mock response
        name_2 = 'name2-1052831874'
        lifespan_count = 1178775510
        expected_response = context_pb2.Context(
            name=name_2, lifespan_count=lifespan_count)
        grpc_stub.GetContext.return_value = expected_response

        response = client.get_context(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetContext.assert_called_once()
        args, kwargs = grpc_stub.GetContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.GetContextRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[AGENT]', '[SESSION]',
                                   '[CONTEXT]')

        # Mock exception response
        grpc_stub.GetContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_context, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        context = context_pb2.Context()

        # Mock response
        name = 'name3373707'
        lifespan_count = 1178775510
        expected_response = context_pb2.Context(
            name=name, lifespan_count=lifespan_count)
        grpc_stub.CreateContext.return_value = expected_response

        response = client.create_context(parent, context)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateContext.assert_called_once()
        args, kwargs = grpc_stub.CreateContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.CreateContextRequest(
            parent=parent, context=context)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        context = context_pb2.Context()

        # Mock exception response
        grpc_stub.CreateContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_context, parent,
                          context)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        context = context_pb2.Context()

        # Mock response
        name = 'name3373707'
        lifespan_count = 1178775510
        expected_response = context_pb2.Context(
            name=name, lifespan_count=lifespan_count)
        grpc_stub.UpdateContext.return_value = expected_response

        response = client.update_context(context)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateContext.assert_called_once()
        args, kwargs = grpc_stub.UpdateContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.UpdateContextRequest(context=context)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        context = context_pb2.Context()

        # Mock exception response
        grpc_stub.UpdateContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_context, context)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[AGENT]', '[SESSION]',
                                   '[CONTEXT]')

        client.delete_context(name)

        grpc_stub.DeleteContext.assert_called_once()
        args, kwargs = grpc_stub.DeleteContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.DeleteContextRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[AGENT]', '[SESSION]',
                                   '[CONTEXT]')

        # Mock exception response
        grpc_stub.DeleteContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_context, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_create_contexts(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        contexts = []

        # Mock response
        expected_response = context_pb2.BatchCreateContextsResponse()
        grpc_stub.BatchCreateContexts.return_value = expected_response

        response = client.batch_create_contexts(parent, contexts)
        self.assertEqual(expected_response, response)

        grpc_stub.BatchCreateContexts.assert_called_once()
        args, kwargs = grpc_stub.BatchCreateContexts.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.BatchCreateContextsRequest(
            parent=parent, contexts=contexts)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_create_contexts_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')
        contexts = []

        # Mock exception response
        grpc_stub.BatchCreateContexts.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.batch_create_contexts,
                          parent, contexts)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_all_contexts(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')

        client.delete_all_contexts(parent)

        grpc_stub.DeleteAllContexts.assert_called_once()
        args, kwargs = grpc_stub.DeleteAllContexts.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.DeleteAllContextsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_all_contexts_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = conversation_service_client.ConversationServiceClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[AGENT]', '[SESSION]')

        # Mock exception response
        grpc_stub.DeleteAllContexts.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_all_contexts, parent)
