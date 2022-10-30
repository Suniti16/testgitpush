import pymongo
client = pymongo.MongoClient("mongodb+srv://sunitipapneja:f7syzq6yrn@gukku.isbg2ip.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name" : "sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1=client['monogotest']
coll=db1['test']
coll.insert_one(d)