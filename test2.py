import json
from pprint import pprint

json_data=open('food.json')
data = json.load(json_data)
json_data.close()


## note: keys for each data item in array
## [u'portions', u'description', u'tags', u'nutrients', u'group', u'id', u'manufacturer']

proteinArray = []

for item in data:
	proteinVal = None
	caloricVal = None

	for aspect in item['nutrients']:

		if aspect['description'] == 'Protein':
			proteinVal = aspect['value']

		if aspect['description'] == 'Energy':
			caloricVal = aspect['value']

	if not caloricVal == None and caloricVal > 0 and not proteinVal == None:
		# print proteinVal, type(proteinVal)
		# print caloricVal, type(caloricVal)
		if proteinVal/caloricVal >= .05:
			proteinArray.append(item)

print len(proteinArray)

