import json



data = json.load(open('posts_by_author.json'))

total = 0
not_prev = 0

for name in data:

	for p in data[name]['posts']:

		total +=1

		if 'oldestArchive' in p:

			if '202112' in p['oldestArchive']:

				not_prev+=1


print(total,not_prev,not_prev/total*100)
