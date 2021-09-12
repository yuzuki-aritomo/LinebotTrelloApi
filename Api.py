
import requests
import json

url = "https://api.trello.com/1/cards"
s = "members/user90898878"
headers = {
  "Accept": "application/json"
}

#追加するカードの名前
card_name = "test add"

query = {
  'key': '4a622c5834edd8afcb884ffd870cbcd8',
  'token': 'bd4be36f22d5220491c82668dff1b3084e6e3a87495566841c536bc29e85b4a3',
}

def createCard(ReqText):
  query['name'] = ReqText
  query['idList'] = '5f329cbc131beb79fc75c28e'
  response = ""
  try:
    response = requests.request(
      "POST",
      url,
      headers=headers,
      params=query,
    )
    return True
  except:
    #ログに出力
    with open('log.json', mode='wt', encoding='utf-8') as file:
      json.dump(json.loads(response.text), file, sort_keys=True, indent=4, separators=(",", ": "))
    return False