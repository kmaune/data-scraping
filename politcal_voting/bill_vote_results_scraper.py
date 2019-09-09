import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
import re
import pandas as pd


BASE_URL = 'https://www.govtrack.us/congress/votes/116-2019/'
chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

votes = pd.read_csv('data/senate_votes.csv')

for index, vote_info in votes.iterrows():
	vote_id = vote_info['Vote ID']
	url = BASE_URL + vote_id

	driver.get(url)
	innerHTML = driver.execute_script("return document.body.innerHTML") 
	soup = BeautifulSoup(innerHTML, 'lxml')

	tables = soup.find_all("table", {"class": "stats"})
	overview_table = tables[0]
	table_data = overview_table.findAll('td')

	overview = []
	for data in table_data:
		text = data.text;
		text = text.strip()
		if(text.find('%') != -1):
			continue
		overview.append(text)

	filename = 'data/vote_overview/{bill}_overview.csv'.format(
		bill = vote_id
	)
	with open(filename, 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['Yea (All)', 'Yea (R)', 'Yea (D)', 'Yea (I)',
		'Nay (All)', 'Nay (R)', 'Nay (D)', 'Nay (I)', 'No Vote (All)',
		'No Vote (R)', 'No Vote (D)', 'No Vote (I)']

		csv_writer.writerow(headers)
		csv_writer.writerow(overview)



	vote_containers = soup.find_all("div", {"id": "vote-details-all"})
	vote_container_all = vote_containers[0]
	vote_tables = vote_container_all.findAll('table')

	individual_data = []
	x = 1

	filename = 'data/vote_results/{bill}_results.csv'.format(
		bill = vote_id
	)
	with open(filename, 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['State', 'Party', 'Name', 'Vote' ]
		csv_writer.writerow(headers)
		for vote_table in vote_tables:
			table_rows = vote_table.findAll('tr')
			for table_row in table_rows:
				td = table_row.findAll('td')
				if(len(td) != 5):
					continue
				vote = td[0].text.strip()
				state = td[1].text.strip()
				party = td[2].text.strip()
				name = td[3].text.strip()
				individual_data = [state, party, name, vote]
				csv_writer.writerow(individual_data)








		