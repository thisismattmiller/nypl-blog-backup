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

		if 'archive' not in post:
			print("Skipping",data['name'], counter,'/',len(data['posts']))
			continue

		if 'oldestArchive' in post:
			print("Skipping",data['name'], counter,'/',len(data['posts']))
			continue

		# see if it has been archived recently
		try:
			wayback = waybackpy.Url(post['url'], user_agent)
			lasturl = str(wayback.oldest())

			print(data['name'], counter,'/',len(data['posts']), post['url'])
			print(lasturl)
			post['oldestArchive'] = lasturl
			json.dump(data,open(file,'w'),indent=2)

		except Exception as e:

			print(file,repr(e))
			print(data)
			pass



		json.dump(data,open(file,'w'),indent=2)



if __name__ == "__main__":

	work = list(glob.glob('data_split/*.json'))

	for result in tqdm.tqdm(multiprocessing.Pool(2).imap_unordered(archive, work), total=len(work)):	

		pass