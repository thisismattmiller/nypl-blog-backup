import json
import glob


# data1 = json.load(open('authors_1.json'))
# data2 = json.load(open('authors.json'))


# for key in data2:

# 	if key in data1:

# 		data1[key]['posts'] = data1[key]['posts'] + data2[key]['posts']

# 	else:


# 		data1[key] = data2[key]



# json.dump(data1,open('authors_final.json','w'),indent=2)


# split
# data = json.load(open('authors_final.json'))

# for key in data:

# 	json.dump(data[key],open(f"data_split/{data[key]['number']}.json",'w'),indent=2)


# back together

authors = {}
for file in glob.glob('data_split/*.json'):

	data = json.load(open(file))

	authors[data['name']] = data


json.dump(authors,open('posts_by_author.json','w'),indent=2)