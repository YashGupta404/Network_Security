from pymongo.mongo_client import MongoClient
import certifi

uri = "mongodb+srv://yashguptawork2005:6fO8lQBuYLQs0lXB@ac-1qzyqeu-shard-00-00.tv4zylh.mongodb.net/?retryWrites=true&w=majority"

# Replace <username> and <password> with your real MongoDB Atlas credentials
client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)