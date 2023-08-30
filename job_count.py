import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/jobs/search?keywords=data%20analyst&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

response = requests.get(url)

print(response)

soup = BeautifulSoup(response.content, 'html.parser')

job_title = soup.find('h3', class_='base-search-card__title').text.strip()

print(job_title)

def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')
    return 

print(response)
print(page_number)
    
if page_number < 25:
    page_number = page_number + 25
    linkedin_scraper(webpage, page_number)
    linkedin_scraper('https://www.linkedin.com/jobs/search?keywords=data%20analyst&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0', 0)