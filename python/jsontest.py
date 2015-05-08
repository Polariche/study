"""""""""""""""""""""""""""""""""""""""""""""
[]s are for lists
{}s are for dictionaries
"""""""""""""""""""""""""""""""""""""""""""""
import json

#input
with open('sample.json') as data_file:
	json_data = json.load(data_file)


wordlist = json_data[""]

#output - modifing the json file
with open('sample.json', 'w') as outfile:
	json.dump(json_data,outfile,sort_keys=True,indent=4)
