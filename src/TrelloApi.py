import requests
from config import TrelloApiConfig
import json

headers = {
  "Accept": "application/json"
}
query = {
  'key': TrelloApiConfig.KEY,
  'token': TrelloApiConfig.TOKEN,
}

#create new card
def createCard(ReqText):
  try:
    ReqText = ReqText + '\n'
    name, desc = ReqText.split('\n', 1)
    query['idList'] = '5f329cbc131beb79fc75c28e'
    query['name'] = name
    query['desc'] = desc
    url = "https://api.trello.com/1/cards"
    requests.request(
      "POST",
      url,
      headers=headers,
      params=query,
    )
    return True
  except Exception as e:
    with open('log/log.json', mode='wt', encoding='utf-8') as file:
      file.write(str(e))
    return False

#get cards from board
def getCards():
  board_id = '5f329cbc131beb79fc75c28e'
  url = "https://api.trello.com/1/lists/"+ board_id +"/cards"
  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query,
    )
  print(response)
  print(response.text)
  re = json.loads(response.text)
  ans = re[0]['name'] + re[1]['name']
  return ans