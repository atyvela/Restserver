from flask import Flask, request jsonify
import requests, json

app = Flask(__name__)
url = "http://0.0.0.0:5000"
list = ["1","2","3","4"]
IPs2 = []
bad_packets = "0"
good_packets = "0"
@app.route('/')
def index():
	return "Hello"
	
	
@app.route('/list/', methods=['GET','POST'])
def get_tasks():
	if request.method == 'GET':
		return jsonify(list)
	if request.method == 'POST':
		IPs2 = request.json
		for i in IPs2:
			if i not in list:
				list.append(i)
				
				
@app.route('/unity/', methods=['PUT'])
def post_ip():
	if request.method == 'PUT':
		ip = request.json
		if ip not in list:
			list.append(str(ip))
			
			
			
@app.route('/badpkts/', methods=['GET','POST'])
def post_bad_pkts():
	if request.method == 'GET':
		return jsonify(bad_packets)
	if request.method == 'POST':
		bad_packets = request.json
		
		
		
@app.route('/goodpkts/', methods=['GET', 'POST'])
def post_good_pkts():
	if request.method == 'GET':
		return jsonify(good_packets)
	if request.method == 'POST':
		good_packets = request.json
	
	
	
if __name__ == '__main__':
	app.run(host="0.0.0.0", port = 5000,debug=True)
