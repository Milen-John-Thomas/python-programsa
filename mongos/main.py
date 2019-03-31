import pymongo
from flask import Flask, jsonify, request
app = Flask(__name__)

def mongoInitialiser(database,col):
	d = {}
	client = pymongo.MongoClient("localhost:27017")
	db = client[database]
	collection = db[col]
	result = collection.find_one()
	for key in result.keys():
		if key == "_id":
			d[key] = str(result[key])
		else:
			d[key] = result[key]
	return d

def mongoLanguages(database,col):
	client = pymongo.MongoClient("localhost:27017")
	db = client[database]
	collection = db[col]
	result = collection.find_one({"name" : "lang"})
	return result

def addNew(database,col):
	client = pymongo.MongoClient("localhost:27017")
	db = client[database]
	collection = db[col]
	return collection


@app.route('/', methods=['GET'])
def index():
	return jsonify(mongoInitialiser('profile','pro_col'))


@app.route("/lang/<string:l>", methods=['GET'])
def lang(l):
	langs = [la for la in mongoLanguages('profile','pro_col')["lang"] if la["name"] == l]
	return jsonify(langs[0]["name"])

@app.route("/updatelang", methods=['POST'])
def addLang():
	newDict = {}
	name = request.json["name"]
	langs = [x for x in request.json["lang"]]
	newDict["name"] = name
	newDict["lang"] = langs
	col = addNew('profile','pro_col')
	col.insert_one(newDict)
	return jsonify(str(newDict))

if __name__=='__main__':
	app.run(debug=True)


