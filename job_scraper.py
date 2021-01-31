import requests
from bs4 import BeautifulSoup

URL = 'https://www.reed.co.uk/jobs/web-developer-jobs-in-devon'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='server-results')

jobs = results.find_all('article', class_='job-result')

print('Found ', len(jobs), ' jobs! \n')

for job in jobs:
    title = job.find('h3', class_='title')
    company = job.find('a', class_='gtmJobListingPostedBy')
    location = job.find(
        'li', class_='location')
    salary = job.find('li', class_='salary')
    link = job.find('a')['href']
    print('Title is:', title.text.strip())
    print('Company is:', company.text.strip())
    print('Location is:', location.text.strip())
    print('Salary:', salary.text.strip())
    #print('Apply here:', link)
    print()
