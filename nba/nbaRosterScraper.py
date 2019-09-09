"""
Code to scrape data on NBA team rosters for upcoming 2019-2020 season 
from https://www.basketball-reference.com. 

All roster data can be strored in individual team files or in 
a single nba wide file
"""

import argparse
import requests
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest


parser = argparse.ArgumentParser(description='Run experiments and generate figures')
parser.add_argument('--all', action='store_true', help='load all teams in one file (default)')
parser.add_argument('--individual', action='store_true', help='load each team into individual file')
args = parser.parse_args()




if not args.individual:
	with open('data/rosters/nba.csv', 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['Team', 'Player', 'Position', 'Experience']
		csv_writer.writerow(headers)


teams = ['ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 
'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

for team in teams:
	link_head = 'https://www.basketball-reference.com/teams/'
	link_end = '/2020.html'
	link = link_head + team + link_end
	#print(link)

	response = requests.get(link)

	soup = BeautifulSoup(response.text, 'html.parser')

	players = soup.find_all(attrs={"data-stat": "player"})
	positions = soup.find_all(attrs={"data-stat": "pos"})
	years_experience = soup.find_all(attrs={"data-stat": "years_experience"})

	if args.individual:

		folders = 'data/rosters/'
		filetype = '.csv'
		filepath = folders+team+filetype
		
		with open(filepath, 'w') as csv_file:
			csv_writer = writer(csv_file)
			headers = ['Player', 'Position', 'Experience']
			csv_writer.writerow(headers)

			for player, position, experience in zip_longest(players, positions, years_experience):
				if player.text == "Player":
					continue		
				csv_writer.writerow([player.text, position.text, experience.text])

	else:
		with open('data/rosters/nba.csv', 'a') as csv_file:
			csv_writer = writer(csv_file)
			for player, position, experience in zip_longest(players, positions, years_experience):
				if player.text == "Player":
					continue
				csv_writer.writerow([team, player.text, position.text, experience.text])



