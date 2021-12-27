from bs4 import BeautifulSoup
import json
from datetime import datetime
import re


from selenium import webdriver

DRIVER_PATH = '/Users/m/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


authors={}

for x in range(3000,10000):

	url = f"https://www.nypl.org/blog/author/{x}"

	driver.get(url)

	soup=BeautifulSoup(driver.page_source,'html.parser')

	author_el = soup.find('h1',{'id':'page-title'})

	author_name = author_el.get_text().replace('Posts by ','').strip()
	

	posts_els = soup.findAll('div',{'class':'blog-post-preview'})

	posts = []

	for p in posts_els:

		title = p.find('h2').get_text().strip()
		# print(title)

		date = p.find('span',{'class':'blog-date'}).get_text().strip()
		timestamp = datetime.strptime(date, '%B %d, %Y')
		# print(timestamp)
		text = str(list(p.find('div',{'class':'teaser-text'}).children)[0]).strip()
		purl = 'https://www.nypl.org' + p.find('a')['href']


		# print(date)
		# print(text)
		# print(purl)

		posts.append({
			'title':title,
			'date':date,
			'timestamp': int(timestamp.timestamp()),
			'text':text,
			'url':purl
			})



	if len(posts) == 20:

		# they gotta lotaa posts
		do_next = True


		while do_next == True:

			

			pager_bottom = soup.find('div',{'class':'pager-bottom'})

			if pager_bottom != None:

				next_el = pager_bottom.find('a',text=re.compile(r'Next'))

				if next_el == None:
					break

				next_url = 'https://www.nypl.org' + next_el['href']

				driver.get(next_url)

				soup=BeautifulSoup(driver.page_source,'html.parser')

				posts_els = soup.findAll('div',{'class':'blog-post-preview'})

				for p in posts_els:

					title = p.find('h2').get_text().strip()
					# print(title)

					date = p.find('span',{'class':'blog-date'}).get_text().strip()
					timestamp = datetime.strptime(date, '%B %d, %Y')
					# print(timestamp)
					text = str(list(p.find('div',{'class':'teaser-text'}).children)[0]).strip()
					purl = 'https://www.nypl.org' + p.find('a')['href']

					posts.append({
						'title':title,
						'date':date,
						'timestamp': int(timestamp.timestamp()),
						'text':text,
						'url':purl
						})
			else:

				do_next = False





	print(x,'/','3000',author_name,f"{len(posts)} posts")

	if author_name == 'NYPL Staff' and len(posts) == 0:
		continue



	if author_name not in authors:
		authors[author_name] = {
			'name': author_name,
			'url' : url,
			'number': x,
			'posts': []
		}


	authors[author_name]['posts'] = authors[author_name]['posts'] + posts
	# print(authors)

	json.dump(authors,open('authors.json','w'),indent=2)

	# break


