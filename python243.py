#Python Program to read List of Dictionaries from File
# Importing the json module  
import json 
  
# Opening the json file  
with open('data.json') as json_file: 
    data = json.load(json_file) 
  
# Printing the data 
for i in data: 
    print(i) 