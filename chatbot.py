from flask import Flask,jsonify,request,json
import os.path
import datetime


now=datetime.datetime.now()
date=(now.strftime("%Y-%m-%d"))
time=(now.strftime("%H-%m-%s"))
app=Flask(__name__)



@app.route("/add-feeling/<emailId>",methods=["POST"])

def add_feelings(emailId):
	if os.path.isfile("data.json"):
		with open("data.json") as file:
			data=file.read()
			jsonData=json.loads(data)
		if emailId not in jsonData:
			jsonData[emailId]={}
		if date not in jsonData[emailId]:
			jsonData[emailId][date]=[]
		newfeeling={
		"name":request.json["name"],
		"feeling":request.json["feeling"],
		"time":time
		}		
		jsonData[emailId][date].append(newfeeling)
		with open("data.json","w") as file:
			json.dump(jsonData,file,indent=4,)
		return jsonify(newfeeling)
	return jsonify({"error":"no file"})



@app.route("/add-feeling/<emailId>/gbu_content",methods=["GET"])

def gbu_content(emailId):
	with open("data.json") as file:
		read=file.read()
		jsonData=json.loads(read)
	a=jsonData[emailId].keys()
	list1=[]
	for i in a:
		list1.append(i)
	data=[]
	for date in list1:
		for i in jsonData[emailId][date]:
			data.append(i["feeling"])
	return jsonify(data)



if __name__=="__main__":
	app.run(port=8000,debug=True)

