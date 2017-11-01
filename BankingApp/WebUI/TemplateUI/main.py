from flask import Flask, request, render_template, jsonify
app = Flask(__name__, static_url_path='')
import os

@app.route('/')
def index():
	'''
	Home page
	'''

	return render_template('index.html')
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8000))
	app.run(debug=True, host='0.0.0.0', port=port)
