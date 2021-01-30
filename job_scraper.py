import requests
from bs4 import BeautifulSoup

URL = 'https://uk.indeed.com/jobs?q=web+developer&l=devon'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="resultsCol")

jobs = results.find_all('div', id = 'pj_ef4ab5c5b2eef673')

for job in jobs:
	title = job.find('h2', class_='title')
    company= job.find('div', class_='company')
    location = job.find('div', class_='location')
	print(title)
	print(company)
	print(location)
	print()