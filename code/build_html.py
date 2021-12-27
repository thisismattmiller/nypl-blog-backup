import json



data = json.load(open('posts_by_author.json'))

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
     <link rel="stylesheet" href="style.css">

  </head>
  <body>

  <h1 style="font-family:monospace">NYPL Blog -&gt; Archive.org</h1>
  <p>
  	Below are all the public NYPL blog posts by author, each one has been saved in internet archive as of 2021. You can find this data as <a href="https://github.com/thisismattmiller/nypl-blog-backup">json and code here</a>.
  </p>

  <hr>
"""

names = data.keys()
names = sorted(names)



for name in names:

	d = data[name]

	html = html + f"<div><h3>{d['name']} <a href=\"{d['url']}\">({d['number']})</a></h3>"

	if len(d['posts']) > 0:

		html = html + '<ol>'
		posts = sorted(d['posts'], key=lambda d: d['timestamp']) 
		for p in posts:
			if 'archive' in p:
				html = html + f"<li><a target=\"_blank\" href=\"{p['url']}\">Orginal</a><a target=\"_blank\" href=\"{p['archive']}\">Archive</a><span class=\"date\">{p['date']}</span><span class=\"title\">{p['title']}</span></li>"
			else:
				html = html + f"<li><a target=\"_blank\" href=\"{p['url']}\">Orginal</a> Could not Archive <span>{p['title']}</span></li>"

		html = html + '</ol>'
	else:


		html = html + '<div>No Posts Found</div>'



	html = html + '</div>\n'














html = html + """
  </body>
</html>"""


with open('index.html','w') as out:
	out.write(html)