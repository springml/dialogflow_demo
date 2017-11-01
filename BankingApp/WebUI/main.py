from flask import Flask, request, render_template, jsonify
app = Flask(__name__, static_url_path='')
import os 
from detect_intent import _detect_text_intent
import base64 
import random

@app.route('/')
def index():
	'''
	Home page
	'''

	return render_template('index.html')

@app.route('/run_test_intent')
def detect_test():
	#print _detect_text_intent("dialogflow-enterprise-demo", "NewAgent", "b83b2284-7a36-46f7-b220-e33ed3d78722", request.args["input_string"], "en-US").fulfillment.text
	result = _detect_text_intent("dialogflow-enterprise-demo", "NewAgent", request.args["sessionid"], request.args["input_string"], "en-US")
	result= '{"text": "%s", "object": "%s"}' %(result.fulfillment.text.encode('ascii', 'ignore'), base64.b64encode(str(result).encode('ascii', 'ignore')))
	return result 
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8000))
	app.run(debug=True, host='0.0.0.0', port=port)