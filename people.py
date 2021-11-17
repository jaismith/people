import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

ROOT = 'https://api.dartmouth.edu/api/'
JWT_ENDPOINT = ROOT + 'jwt'
PPL_ENDPOINT = ROOT + 'people'
KEY = os.getenv('DART_API_KEY')

def get_jwt() -> str:
  r = requests.post(JWT_ENDPOINT, headers={'Authorization': KEY})
  return r.json()['jwt']

def get_page(page: int, jwt: str) -> list:
  r = requests.get(PPL_ENDPOINT, headers={'Authorization': f'Bearer {jwt}'},
    params={'page': page})
  return r.json()

def get_all_people() -> list:
  jwt = get_jwt()

  people= []
  page = 0

  done = False

  while not done:
    page_people = get_page(page, jwt)
    people.extend(page_people)

    print(f'Page {page} fetched, {len(people)} total entries retrieved.')

    if page_people == []:
      done = True

    page += 1

  return people

people = get_all_people()
f = open('people.json', 'w')
f.write(json.dumps(people))
f.close()
