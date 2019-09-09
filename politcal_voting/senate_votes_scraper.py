import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
import re


BASE_URL = 'https://www.govtrack.us/congress/votes#chamber[]=1'

chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get(BASE_URL)
innerHTML = driver.execute_script("return document.body.innerHTML") 

soup = BeautifulSoup(innerHTML, 'lxml')

votes = soup.find_all('a', href=re.compile(r"^/congress/votes/116-2019/"))

vote_id = 0
with open('data/senate_votes.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['Count', 'Vote', 'Vote ID']
	csv_writer.writerow(headers)
	for vote in votes:
		href = vote['href']
		split_vote = href.split('/')
		csv_writer.writerow([vote_id, vote.text, split_vote[len(split_vote)-1]])
		vote_id += 1

