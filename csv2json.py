import csv 
import json 
import sys


def make_json(csvFilePath, jsonFilePath): 
	
	# create a dictionary 
	data = [] 
	
	with open(csvFilePath, encoding='utf-8') as csvf: 
		csvReader = csv.DictReader(csvf) 
		
		for rows in csvReader: 
			
			key = rows['DORK'] 
			data.append(rows)
                        #data[key] = rows 


	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=4)) 
		

csvFilePath = sys.argv[1]
jsonFilePath = sys.argv[2]

make_json(csvFilePath, jsonFilePath)
