import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.jdsports.co.uk/")
txt = result.text
status = result.status_code

#print(txt, status)

soup = BeautifulSoup(result.content, 'lxml')

page_title = soup.title

page_body = soup.body

page_head = soup.head

print(page_title, page_body, page_head)

all_h1_tags = []

for element in soup.select('h1'):
    all_h1_tags.append(element.text)

print(all_h1_tags)

image_data = []

images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})

print(image_data)

all_links = []

links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

print(all_links)
