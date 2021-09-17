import requests

url = "https://api.trello.com/1/cards"
headers = {
  "Accept": "application/json"
}
query = {
  'key': '4a622c5834edd8afcb884ffd870cbcd8',
  'token': 'bd4be36f22d5220491c82668dff1b3084e6e3a87495566841c536bc29e85b4a3',
}

#create new card
def createCard(ReqText):
  print(ReqText)
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