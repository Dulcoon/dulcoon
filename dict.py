dict1 = {
    'value' : 5
}

dict2 = {
    'value' : 3
}

print(f"Dict 1 = {dict1}")
print(f"Dict 2 = {dict2}")
if dict2['value'] >= dict1['value']:
    dict1 = dict2
    for i in range(dict1['value']):
        dict2['value'] += 1
else:
    for j in range(dict2['value']):
        dict2['value'] -= j
    dict1 = dict2
print(f"Dict 1 = {dict1}")
print(f"Dict 2 = {dict2}")
