import requests

url = "http://localhost:8765"

def check_connection():
  try:
    requests.get(url)
    return True
  except:
    return False

def anki_request(payload):
  if(check_connection()):
    response = requests.post(url, json=payload)
    result = response.json()
    return result

def get_decks_name():
  payload = {
    "action": "deckNames",
    "version": 6
  }

  result = anki_request(payload)
  return result['result']

def get_cards_id(deck_name):
  payload = {
    "action": "findNotes",
    "version": 6,
    "params": {
        "query": f"deck:{deck_name}"
    }
  }

  result = anki_request(payload)
  return result['result']

def get_cards(note_id):
  payload = {
    "action": "notesInfo",
    "version": 6,
    "params": {
        "notes": note_id
    }
  }
  
  result = anki_request(payload)
  return result['result']