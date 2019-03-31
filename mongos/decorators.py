import pymongo

def mongo_initialize(func):
	def inner():
		d = {}
		client = pymongo.MongoClient("localhost:27017")
		db = client.profile
		collection = db.pro_col
		result = collection.find_one()
		for key in result.keys():
			if key == "_id":
				d[key] = str(result[key])
			else:
				d[key] = result[key]
		print(d)
		func()		
	return inner

@mongo_initialize
def taker():
	print("Taker fn")

taker()