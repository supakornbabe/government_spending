import requests
import json
import sys

token = "92634b5ae477bfb3f8672162e754a59d"
start = 6040
stop = 100000
year = 2561
url = "https://govspendingapi.data.go.th/api/service/bbgfproject"


def get_with_offset(offset, file):
    params = {
        'budget_end': '1000000000000',
        'min_code': '15000',
        'offset': offset,
        'user_token': token,
        'year': year,
        # 'prov_code': '03100000'
    }

    res = requests.get(url, params)
    data = res.json()
    for i in data['result']:
        print(json.dumps(i, ensure_ascii=False), file=file)
    if len(data['result']) < 20:
        print("Year " + str(year)+" finish")
        sys.exit(1)


if __name__ == "__main__":
    for i in range(start, stop+1, 20):
        filename = '../data/'+str(year)+'/'+str(i)+'.json'
        with open(filename,'w') as f:
            # f = open(filename, 'w')
            print(i)
            get_with_offset(i, f)
