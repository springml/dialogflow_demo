/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
(function() {
  "use strict";

  var ENTER_KEY_CODE = 13;
  var queryInput, resultDiv;
  var sessionid = Date.now();
  window.onload = init;

  function init() {
    queryInput = document.getElementById("q");
    resultDiv = document.getElementById("result");
    queryInput.addEventListener("keydown", queryInputKeyDown);

  
  }

  function queryInputKeyDown(event) {
    if (event.which !== ENTER_KEY_CODE) {
      return;
    }

    var value = queryInput.value;
    queryInput.value = "";
    

    createQueryNode(value);
    var responseNode = createResponseNode();

    var response = sendRequest(value, sessionid)
    var result_json = JSON.parse(response);

    
    
    if (document.getElementById('jsonResponse') != null){
	     console.log('displaying payload')
	     setResponseJSON(atob(result_json["object"]));
	}
  
    setResponseOnNode(result_json["text"], responseNode);
  }

  function createQueryNode(query) {
    var node = document.createElement('div');
    node.className = "clearfix left-align left card-panel green accent-1";
    node.innerHTML = query;
    resultDiv.appendChild(node);
  }

  function createResponseNode() {
    var node = document.createElement('div');
    node.className = "clearfix right-align right card-panel blue-text text-darken-2 hoverable";
    node.innerHTML = "...";
    resultDiv.appendChild(node);
    return node;
  }

  function setResponseOnNode(response, node) {

    node.innerHTML = response ? response : "";
    node.setAttribute('data-actual-response', response);
  }

  function setResponseJSON(response) {
    var node = document.getElementById("jsonResponse");
    node.innerHTML = response ? response: ""
    //node.innerHTML = JSON.stringify(response, null, 2);
  }
  function DLPRequest(value){

    var request = {"items": [{"type": "text/plain", "value": "My ss number is 445-99-2233"} ], "replaceConfigs": [{"replaceWith": "[REDACTED]", "infoType": {"name": "US_SOCIAL_SECURITY_NUMBER"} } ], "inspectConfig": {"infoTypes": [], "minLikelihood": "LIKELIHOOD_UNSPECIFIED", "maxFindings": 0, "includeQuote": true } }
    var xhttp = new XMLHttpRequest();
    var access_token = "ya29.c.El_3BCYVDwQGbNsaFpq0E9-2GjfnOKNVLLsMkcWy4fsLdvBm57gxKwjWsSuV54fhIi2kGBFJU7ypxB55ckUoKqHwPJchf_K1fDW5Byl7bl-gEjdygRyFPnsvz_ue5wLWGQ";
    var URL =  "https://dlp.googleapis.com/v2beta1/content:redact";

    xhttp.open("GET", URL, false);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + access_token);
    
    xhttp.send(request);


    return  xhttp.responseText;

  }
  function sendRequest(value, sessionid) {
    //alert("in send req")

    var URL = "/run_test_intent?input_string=" + value + "&sessionid=" + sessionid
   //var URL = "https://conversation.googleapis.com/v1alpha/projects/dialogflow-enterprise-demo/agents/dialogflow-enterprise-demo/intents"

    //var request = "{'query_input': {'text': {'text': ' " + value + "','language_code': 'en-US'}}}";
    //request = "{  'query_input': {    'text': {      'text': 'start stopwatch',      'language_code': 'en-US'    }  }}"
    
    

    var xhttp = new XMLHttpRequest();


    xhttp.open("GET", URL, false);
    //xhttp.setRequestHeader("Content-type", "application/json; charset=utf-8");
    //xhttp.setRequestHeader("Authorization", "Bearer " + access_token);
    
    xhttp.send();

    return  xhttp.responseText;
    

  }

})();
