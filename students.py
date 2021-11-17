# filter out active students from people.json

import json

f = open('people.json')
s = f.read()
f.close()
people = json.loads(s)

students = {
  '21': [],
  '22': [],
  '23': [],
  '24': [],
  '25': []
}

print('0/0', end='\r')
idx = 0

for person in people:
  print(f'{idx}/{len(people)}', end='\r')
  idx += 1

  email = person.get('email')
  if email is None: continue

  year = email.split('@')[0].split('.')[-1]

  if year.isnumeric() and year in students.keys():
    students[year].append(person)

print()
for year in students.keys():
  print(f'Class of {year}: {len(students[year])} entries')
