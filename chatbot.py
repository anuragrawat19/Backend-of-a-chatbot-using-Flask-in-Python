from flask import Flask,jsonify,request,json #Importing Flask to create web application
import os.path  #importing os.path for manipulating file and directories in  your system
import datetime # this module provides different function for dealing with date and time


now=datetime.datetime.now()
date=(now.strftime("%Y-%m-%d"))
time=(now.strftime("%H-%m-%s"))
app=Flask(__name__)# giving instance of flask class to variable app



@app.route("/add-feeling/<emailId>",methods=["POST"])# created an end point using post method 

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



@app.route("/add-feeling/<emailId>/gbu_content",methods=["GET"])#created and end point to get the feeelings 

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

