#%% Time Series about budget and use every year from 2548 to 2562 
#%% Connect MongoDB
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://supakornbabe:babe3000@cluster0-txdl5.gcp.mongodb.net/test?retryWrites=true")
db = client.stat_for_application
# Issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)

#%% Get Budget_by_year from mongo
import json
data = db.budget_by_year
dataList = data.find()
year = []
use = []
budget = []
for i in dataList:
    # print(i['Year'])
    year.append(str(i['Year']))
    use.append(float(str(i['Use']).replace(',','')))
    budget.append(float(str(i['Budget']).replace(',','')))


print("year: "+str(year))
print("name: 'Use',")
print("data: "+str(use))
print("name: 'Budget',")
print("data: "+str(budget))


# name: 'Installation',
#         data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
