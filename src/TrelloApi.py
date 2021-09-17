import requests
from config import TrelloApiConfig

headers = {
  "Accept": "application/json"
}
query = {
  'key': TrelloApiConfig.KEY,
  'token': TrelloApiConfig.TOKEN,
}

#create new card
def createCard(ReqText):
  url = "https://api.trello.com/1/cards"
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