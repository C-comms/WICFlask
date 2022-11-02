from flask import Flask

app = Flask(__name__)
@app.route('/')	
#routeDecorator
def hello_world():
	return 'rvce.edu.in'

#Main driver Function
if __name__ == '__main__':
	#run() method of Flask class runs in application on local server
	app.run(debug=True) 
	
app.route('/rv')
def hello():
	return 'Suhas Sensei'
	app.add_url_rule('/','rvce',rvce)