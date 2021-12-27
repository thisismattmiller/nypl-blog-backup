import json
import waybackpy
import tqdm
import multiprocessing
import glob
from os.path import exists
import sys



def archive(file):



	data = json.load(open(file))
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

	counter = 0
	for post in data['posts']:


		if exists('STOP'):
			sys.exit()

		counter=counter+1

		sucess="sucessful"
		msg = ""

		if 'archive' in post:
			print("Skipping",data['name'], counter,'/',len(data['posts']))
			continue

		# see if it has been archived recently
		try:
			wayback = waybackpy.Url(post['url'], user_agent)
			lasturl = str(wayback.newest())

			if '/202112' in lasturl:
				print(data['name'], counter,'/',len(data['posts']), post['url'], sucess, "Had been archived in previoius attempt")
				post['archive'] = lasturl
				json.dump(data,open(file,'w'),indent=2)
				continue

		except Exception as e:
			#print(repr(e))
			pass



		try:
			wayback = waybackpy.Url(post['url'], user_agent)
			archive = wayback.save()
			aurl = archive.archive_url

			post['archive'] = aurl
		except Exception as e:

			sucess = "failed"
			msg = repr(e)
			# print("Error saving, skipping",data['name'],counter)



		print(data['name'], counter,'/',len(data['posts']), post['url'], sucess,msg)

		json.dump(data,open(file,'w'),indent=2)



if __name__ == "__main__":

	work = list(glob.glob('data_split/*.json'))

	for result in tqdm.tqdm(multiprocessing.Pool(10).imap_unordered(archive, work), total=len(work)):	

		pass






# print(work)


# xxx=xxxxx




# data = json.load(open('authors_final.json'))

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'


# for name in data:

# 	print(name)
# 	counter = 0
# 	for post in data[name]['posts']:

# 		counter=counter+1

# 		print(counter,'/',len(data[name]['posts']), post['url'])

# 		if 'archive' in post:
# 			continue

# 		try:
# 			wayback = waybackpy.Url(post['url'], user_agent)
# 			archive = wayback.save()
# 			aurl = archive.archive_url

# 			post['archive'] = aurl
# 		except: 
# 			print("Error saving, skipping",counter)




# 		json.dump(data,open('authors_final.json','w'),indent=2)


