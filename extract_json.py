import json

# with open('D:/Documents/IIT/3rd year/deep learning/cw p2/yelp dataset/yelp_academic_dataset_review.json', 'r') as file:
#     data = json.load(file)

# print ("done")

with open('D:/Documents/IIT/3rd year/deep learning/cw p2/yelp dataset/yelp_academic_dataset_review.json', 'r', encoding='utf-8') as file:
    data = file.read()


# JSON string
j_string = '{"name": "Bob", "languages": "English"}'
 
# deserializes into dict and returns dict.
y = json.loads(j_string)
 
print("JSON string = ", y)
print()
 
# JSON file
f = open ('data.json', "r")
 
# Reading from file
data = json.loads(f.read())
 
# Iterating through the json list
for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()