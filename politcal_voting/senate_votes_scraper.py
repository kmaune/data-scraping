import argparse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
import re
import math
import time

parser = argparse.ArgumentParser(description='Scrape Senate Vote Information')
parser.add_argument('--all', action='store_true', help='Scrape and save data for all sessions')
parser.add_argument('--year', type=int,  help='Specify the year of the data desired')
parser.add_argument('--session', type=int, help='Specify the session of the data desired')
parser.add_argument('--start_year', type=int, help='Specify the starting year of the data desired')
parser.add_argument('--end_year', type=int,  help='Specify the ending year of the data desired')
args = parser.parse_args()



BASE_URL = 'https://www.govtrack.us/congress/votes#'
BASE_SESSION = 225 
BASE_YEAR = 1941
BASE_CONGRESS = 77
chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
#driver.get('https://www.govtrack.us/congress/votes#')

#If user specified all data is wanted
if args.all or (args.year == None and args.session == None and (args.start_year == None or args.end_year == None)):
	for session in range(225, 304):
		current_year = BASE_YEAR + session - BASE_SESSION
		current_congress = BASE_CONGRESS + math.floor((session-BASE_SESSION)/2)


		url = '{BASE_URL}session={session}&chamber[]=1'.format(
			BASE_URL = BASE_URL,
			session= str(session)
		)
		driver.get(url)
		time.sleep(1)
		innerHTML = driver.execute_script("return document.body.innerHTML") 
		soup = BeautifulSoup(innerHTML, 'lxml')
		congress_info = '/congress/votes/{congress_num}-{congress_year}/'.format(
				congress_num = str(current_congress),
				congress_year = str(current_year)
			)

		votes = soup.find_all('a', href=re.compile(r"^%s"%congress_info))
		vote_id = 0

		with open('data/senate/vote_lists/{year}_senate_votes.csv'.format(year=str(current_year)), 'w') as csv_file:
			csv_writer = writer(csv_file)
			headers = ['Count', 'Vote', 'Vote ID']
			csv_writer.writerow(headers)
			for vote in votes:
				href = vote['href']
				split_vote = href.split('/')
				csv_writer.writerow([vote_id, vote.text, split_vote[len(split_vote)-1]])
				vote_id += 1
		driver.get('https://www.google.com')
	driver.quit()


elif args.year:
	print("Year")
	if args.year < 1941 or args.year > 2019:
		raise SystemExit('Error: Year Invalid, must be in range [1941, 2019]')

	current_year = args.year
	current_session = BASE_SESSION + (current_year-BASE_YEAR)
	current_congress = BASE_CONGRESS + math.floor((current_year-BASE_YEAR)/2)


	url = '{BASE_URL}session={session}&chamber[]=1'.format(
			BASE_URL = BASE_URL,
			session= str(current_session)
		)
	driver.get(url)
	innerHTML = driver.execute_script("return document.body.innerHTML") 
	soup = BeautifulSoup(innerHTML, 'lxml')

	congress_info = '/congress/votes/{congress_num}-{congress_year}/'.format(
			congress_num = str(current_congress),
			congress_year = str(current_year)
		)
	votes = soup.find_all('a', href=re.compile(r"^%s"%congress_info))
	vote_id = 0

	with open('data/senate/vote_lists/{year}_senate_votes.csv'.format(year=str(current_year)), 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['Count', 'Vote', 'Vote ID']
		csv_writer.writerow(headers)
		for vote in votes:
			href = vote['href']
			split_vote = href.split('/')
			csv_writer.writerow([vote_id, vote.text, split_vote[len(split_vote)-1]])
			vote_id += 1
	driver.quit()


elif args.session:
	print("Session")
	if args.session < 225 or args.session > 303:
		raise SystemExit('Error: Session Invalid, must be in range [225, 303]')

	current_session = args.session
	current_year = BASE_YEAR + (current_session - BASE_SESSION)
	current_congress = BASE_CONGRESS + math.floor((current_session-BASE_SESSION)/2)

	url = '{BASE_URL}session={session}&chamber[]=1'.format(
			BASE_URL = BASE_URL,
			session= str(current_session)
		)
	driver.get(url)
	innerHTML = driver.execute_script("return document.body.innerHTML") 
	soup = BeautifulSoup(innerHTML, 'lxml')
	congress_info = '/congress/votes/{congress_num}-{congress_year}/'.format(
			congress_num = str(current_congress),
			congress_year = str(current_year)
		)
	votes = soup.find_all('a', href=re.compile(r"^%s"%congress_info))
	vote_id = 0

	with open('data/senate/vote_lists/{year}_senate_votes.csv'.format(year=str(current_year)), 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['Count', 'Vote', 'Vote ID']
		csv_writer.writerow(headers)
		for vote in votes:
			href = vote['href']
			split_vote = href.split('/')
			csv_writer.writerow([vote_id, vote.text, split_vote[len(split_vote)-1]])
			vote_id += 1
	driver.quit()


else:
	if args.start_year < 1941 or args.start_year > 2019:
		raise SystemExit('Error: Start Year Invalid, must be in range [1941, 2019]')
	if args.end_year < 1941 or args.end_year > 2019:
		raise SystemExit('Error: End Year Invalid, must be in range [1941, 2019]')
	if args.start_year > args.end_year:
		raise SystemExit('Error: Start Year must be <= End Year')
	if args.start_year == None or args.end_year == None:
		raise SystemExit('Error: Both Start Year and End Year must be specified')

	current_year = args.start_year
	end_year = args.end_year
	current_session = BASE_SESSION + (current_year-BASE_YEAR)
	current_congress = BASE_CONGRESS + math.floor((current_year-BASE_YEAR)/2)

	while current_year <= end_year:
		url = '{BASE_URL}session={session}&chamber[]=1'.format(
				BASE_URL = BASE_URL,
				session= str(current_session)
			)

		driver.get(url)
		time.sleep(2)

		innerHTML = driver.execute_script("return document.body.innerHTML") 
		soup = BeautifulSoup(innerHTML, 'lxml')

		congress_info = '/congress/votes/{congress_num}-{congress_year}/'.format(
				congress_num = str(current_congress),
				congress_year = str(current_year)
			)
		votes = soup.find_all('a', href=re.compile(r"^%s"%congress_info))
		vote_id = 0

		with open('data/senate/vote_lists/{year}_senate_votes.csv'.format(year=str(current_year)), 'w') as csv_file:
			csv_writer = writer(csv_file)
			headers = ['Count', 'Vote', 'Vote ID']
			csv_writer.writerow(headers)
			for vote in votes:
				href = vote['href']
				split_vote = href.split('/')
				csv_writer.writerow([vote_id, vote.text, split_vote[len(split_vote)-1]])
				vote_id += 1

		driver.get('https://www.google.com')
		current_year += 1
		current_session += 1;
		current_congress = BASE_CONGRESS + math.floor((current_year-BASE_YEAR)/2)
	driver.quit()



	
