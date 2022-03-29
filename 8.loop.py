members = ['ektjf77', 'duru']
for member in members:
    print('member', member)

members2 = [
    ['ektjf77', 'daegu', '학생'], 
    ['duru', 'seoul', 'dba']
]
print(members2[0][0])
for member in members2:
    print(member[0], member[1])

ektjf771 = ['ektjf77', 'deagu', '학생']
ektjf772 = {'name': 'ektjf77', 'city': 'deagu', 'job': '학생'} # 사전형
print(ektjf772['city'])
for name in ektjf772:
    print(ektjf772[name])

members3 = [
    {'name':'ektjf77', 'city':'deagu', 'job':'학생'}, 
    {'name':'duru', 'city':'seoul', 'job':'dba'}
]
for member in members3:
    print(member['name'])