import json

with open('intents.txt') as f:
    lines = f.readlines()

intents = []
intent = {}

for line in lines:
    line = line.strip()
    if line.startswith('K:'):
        if intent:
            intents.append(intent)
        intent = {}
        intent['tag'] = line.replace('K:', '')
        intent['patterns'] = []  
        intent['responses'] = []
    elif line.startswith('U:'):
        intent['patterns'].append(line.replace('U:', '')) 
    elif line.startswith('A:'):
        intent['responses'].append(line.replace('A:', ''))

if intent:
    intents.append(intent)

with open('intents.json', 'w', encoding='utf-8') as f:
    json.dump({'intents': intents}, f, indent=4, ensure_ascii=False)
