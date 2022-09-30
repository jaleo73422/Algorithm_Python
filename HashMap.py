# Creating dictionaries
dict_1 ={'Dave': '001', 'Ava': '002', 'Joe': '003'}

print("==== dict_1 ====")
print(dict_1)
print(type(dict_1))

dict_2 = dict(Dave = '001', Ava = '002', Joe = '003')

print()
print("==== dict_2 ====")
print(dict_2)
print(type(dict_2))

# Accessing values
dict_3 = {'Dave': '001', 'Ava': '002', 'Joe': '003'}

print()
print("==== dict_3 ====")
print(dict_3['Dave'])
print(type(dict_3['Dave']))

print(dict_3.keys())
print(dict_3.values())
print(dict_3.get('Dave'))

# Updating values
dict_4 = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
dict_4['Dave'] = '004'   # updating the value of Dave
dict_4['Chris'] = '005'  # adding a key-value pair

print()
print("==== dict_4 ====")
print(dict_4)

# Deleting element
print()
print("==== dict_5 ====")

dict_5 = {'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
print(dict_5)
del dict_5['Dave']  # removes key-value pair of 'Dave'
print(dict_5)
dict_5.pop('Ava')   # removes the value of 'Ava'
print(dict_5)
dict_5.popitem()    # removes the last inserted item
print(dict_5)