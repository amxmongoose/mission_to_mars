import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_dict

#news_text = scraped_dict.find({})["news_text"]

for doc in db.find_all():
    print(doc["news_text"].strip())
    print(doc["news_title"].strip())
    print(doc["facts"])
    print(doc["hemisphere_images"])

print(db.mars["news_text"])