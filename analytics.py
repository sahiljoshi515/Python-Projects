import requests
import json
import pandas as pd
from urllib.request import urlopen
import sys

try:
	code = sys.argv[1]  #Get the code from User
except: 
	print('Please Enter a valid country code!')
	sys.exit()
try:
	with urlopen('https://api.covid19api.com/countries') as response:    #List of all countries 
		source = response.read()
	data = json.loads(source)
except:
	print('Server Down')
	sys.exit()                #if server down or no internet connection? Just end the program        



try:
	for i in range(len(data)):    #Iterate through the list to get to appropriate country code
		dic = data[i]
		for k in dic.values():
			if k == code:
				slug = dic['Slug']


		
	wait = 'https://api.covid19api.com/dayone/country/'    #Append the country_slug you want to see
	url = wait + slug
	response = requests.get(url)

	json_data = json.dumps(response.text)        #get the json data and then load it as a string
	parsed_json = (json.loads(json_data))

	df = pd.read_json(parsed_json)
	df.to_csv(slug+'.csv', index = None, header = True)    #Finally convert it into a csv_file




except NameError:
	print('Please Enter a valid country code!')   #Error handling!



