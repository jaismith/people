# filter out active students from people.json

import json
from itertools import chain

f = open('out/people.json')
s = f.read()
f.close()
people = json.loads(s)

students = {
  '21': [],
  '22': [],
  '23': [],
  '24': [],
  '25': [],
  'UG': [],
}

print('0/0', end='\r')
idx = 0

for person in people:
  print(f'{idx}/{len(people)}', end='\r')
  idx += 1

  email = person.get('email')
  if email is None: continue

  year = email.split('@')[0].split('.')[-1]

  if year in students.keys():
    students[year].append(person)

print()
for year in students.keys():
  print(f'Class of {year}: {len(students[year])} entries')

f = open('out/students.txt', 'w')
emails = (student.get('email') for student in chain(*students.values()))
f.write('\n'.join(emails))
