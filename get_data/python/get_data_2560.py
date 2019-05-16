import requests
import json

token = "402751371d8d559f36046d26b9f964d8"
start = 0
stop = 100000
year = 2560
url = "https://govspendingapi.data.go.th/api/service/bbgfproject"


def get_with_offset(offset, file):
    params = {
        'budget_end': '1000000000000',
        'min_code': '15000',
        'offset': offset,
        'user_token': '402751371d8d559f36046d26b9f964d8',
        'year': year,
        'prov_code': '03100000'
    }

    res = requests.get(url, params)
    data = res.json()
    for i in data['result']:
        print(json.dumps(i, ensure_ascii=False), file=file)
    if len(data['result']) < 20:
        print("Year " + str(year)+" finish")


if __name__ == "__main__":
    for i in range(start, stop+1, 20):
        filename = '../data/'+str(year)+'/'+str(i)+'.txt'
        f = open(filename, 'w')
        print(i)
        get_with_offset(i, f)
