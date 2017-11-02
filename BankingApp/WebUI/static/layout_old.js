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
  var queryInput, resultDiv, accessTokenInput;

  window.onload = init;

  function init() {
    queryInput = document.getElementById("q");
    resultDiv = document.getElementById("result");
    accessTokenInput = document.getElementById("access_token");
    var setAccessTokenButton = document.getElementById("set_access_token");

    queryInput.addEventListener("keydown", queryInputKeyDown);
    setAccessTokenButton.addEventListener("click", setAccessToken);
  }

  function setAccessToken() {
    document.getElementById("placeholder").style.display = "none";
    document.getElementById("main-wrapper").style.display = "block";
    window.init(accessTokenInput.value);
  }

  function queryInputKeyDown(event) {
    if (event.which !== ENTER_KEY_CODE) {
      return;
    }
    console.log("we made it here")
    console.log("sss")
    var value = queryInput.value;
    queryInput.value = "";

    createQueryNode(value);
    var responseNode = createResponseNode();

    var response = sendRequest2(value)

    var result_json = JSON.parse(response);
    var result = result_json.queryResult.fulfillment.text
    setResponseJSON(result_json);
    setResponseOnNode(result, responseNode);
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
    node.innerHTML = response ? response : "[empty response]";
    node.setAttribute('data-actual-response', response);
  }

  function setResponseJSON(response) {
    var node = document.getElementById("jsonResponse");
    node.innerHTML = JSON.stringify(response, null, 2);
  }

  function sendRequest2(value) {
    //alert("in send req")
    console.log("hey")
    var URL = "https://conversation.googleapis.com/v1alpha/projects/dialogflow-enterprise-demo/agents/NewAgent/sessions/2432423:detectIntent";
    //var URL = "https://conversation.googleapis.com/v1alpha/projects/dialogflow-enterprise-demo/agents/dialogflow-enterprise-demo/intents"

    var request = "{'query_input': {'text': {'text': ' " + value + "','language_code': 'en-US'}}}";
    //request = "{  'query_input': {    'text': {      'text': 'start stopwatch',      'language_code': 'en-US'    }  }}"
    
    var access_token = "ya29.c.El_xBMdiJwZcAaJtgI5kEEwrSDVSuCNngbqAxPehkY6HysUIE1u5x9ruw2vpU4h5zat6Aw_TW0MiIbtU4cZd2_guiiGVoErazMo2J0umkD2QuKZ8qgd2RWxoyiJj9dA7jQ";

    var xhttp = new XMLHttpRequest();


    xhttp.open("POST", URL, false);
    xhttp.setRequestHeader("Content-type", "application/json; charset=utf-8");
    xhttp.setRequestHeader("Authorization", "Bearer " + access_token);

    xhttp.send(request);
    console.log(xhttp.responseText)
    return xhttp.responseText;
    

  }

})();
