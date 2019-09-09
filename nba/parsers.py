import requests
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest

BASE_URL = "https://www.basketball-reference.com"

def get_per_game_stats(season="2018-2019"):
	season_end_year = season.split("-")[1]

	url = "{BASE_URL}/leagues/NBA_{season_end_year}_per_game.html".format(
			BASE_URL = BASE_URL,
			season_end_year = season_end_year
		)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	players = soup.find_all(attrs={"data-stat": "player"})
	teams = soup.find_all(attrs={"data-stat": "team_id"})
	games = soup.find_all(attrs={"data-stat": "g"})
	games_started = soup.find_all(attrs={"data-stat": "gs"})
	minutes = soup.find_all(attrs={"data-stat": "mp_per_g"})
	points = soup.find_all(attrs={"data-stat": "pts_per_g"})
	assists = soup.find_all(attrs={"data-stat": "ast_per_g"})
	field_goals = soup.find_all(attrs={"data-stat": "fg_per_g"})
	fg_attempts = soup.find_all(attrs={"data-stat": "fga_per_g"})
	fg_pct = soup.find_all(attrs={"data-stat": "fg_pct"})
	threes = soup.find_all(attrs={"data-stat": "fg3_per_g"})
	three_attempts = soup.find_all(attrs={"data-stat": "fg3a_per_g"})
	three_pct = soup.find_all(attrs={"data-stat": "fg3_pct"})
	eFG_pct = soup.find_all(attrs={"data-stat": "efg_pct"})
	free_throws = soup.find_all(attrs={"data-stat": "ft_per_g"})
	ft_attemps = soup.find_all(attrs={"data-stat": "fta_per_g"})
	ft_pct = soup.find_all(attrs={"data-stat": "ft_pct"})
	offensive_rebounds = soup.find_all(attrs={"data-stat": "orb_per_g"})
	defensive_rebounds = soup.find_all(attrs={"data-stat": "drb_per_g"})
	steals = soup.find_all(attrs={"data-stat": "stl_per_g"})
	blocks = soup.find_all(attrs={"data-stat": "blk_per_g"})
	turnovers = soup.find_all(attrs={"data-stat": "tov_per_g"})
	personal_fouls = soup.find_all(attrs={"data-stat": "pf_per_g"})

	filepath = 'data/player_stats/{season}_per_game.csv'.format(
			season=season
		)

	with open(filepath, 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['Player', 'Team', 'GP', 'GS', 'MPG', 'PTS', 'AST', 
				   'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'eFG%', 'FT',
				   'FTA','FT%', 'ORB', 'DRB', 'STL', 'BLK', 'TOV', 'PF']

		csv_writer.writerow(headers)

		for (player, tm, g, gs, mpg, pts, ast, fg, fga, fgp, 
			tp, tpa, tpp, efg, ft, fta, ftp, orb, drb, stl, 
			blk, tov, pf) in zip_longest(players, teams, games, 
			games_started, minutes, points, assists, field_goals, 
			fg_attempts, fg_pct, threes, three_attempts, three_pct,
			eFG_pct, free_throws, ft_attemps, ft_pct, offensive_rebounds,
			defensive_rebounds, steals, blocks, turnovers, personal_fouls):

			if player.text == 'Player':
				continue

			csv_writer.writerow([player.text, tm.text, g.text, gs.text, 
				mpg.text, pts.text, ast.text, fg.text, fga.text, fgp.text,
				tp.text, tpa.text, tpp.text, efg.text, ft.text, fta.text,
				ftp.text, orb.text, drb.text, stl.text, blk.text, tov.text,
				pf.text])

	return

def get_advanced_stats(season="2018-2019"):
	season_end_year = season.split("-")[1]

	url = "{BASE_URL}/leagues/NBA_{season_end_year}_advanced.html".format(
		BASE_URL = BASE_URL,
		season_end_year = season_end_year
	)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')


	players = soup.find_all(attrs={"data-stat": "player"})
	teams = soup.find_all(attrs={"data-stat": "team_id"})
	games = soup.find_all(attrs={"data-stat": "g"})
	minutes = soup.find_all(attrs={"data-stat": "mp"})
	PERs = soup.find_all(attrs={"data-stat": "per"})
	ts_pct = soup.find_all(attrs={"data-stat": "ts_pct"})
	three_rates = soup.find_all(attrs={"data-stat": "fg3a_per_fga_pct"})
	ft_rates = soup.find_all(attrs={"data-stat": "fta_per_fga_pct"})
	orb_pct = soup.find_all(attrs={"data-stat": "orb_pct"})
	drb_pct = soup.find_all(attrs={"data-stat": "drb_pct"})
	trb_pct = soup.find_all(attrs={"data-stat": "trb_pct"})
	ast_pct = soup.find_all(attrs={"data-stat": "ast_pct"})
	stl_pct = soup.find_all(attrs={"data-stat": "stl_pct"})
	blk_pct = soup.find_all(attrs={"data-stat": "blk_pct"})
	tov_pct = soup.find_all(attrs={"data-stat": "tov_pct"})
	usg_pct = soup.find_all(attrs={"data-stat": "usg_pct"})
	offensive_winshares = soup.find_all(attrs={"data-stat": "ows"})
	defensive_winshares = soup.find_all(attrs={"data-stat": "dws"})
	winshares = soup.find_all(attrs={"data-stat": "ws"})
	winshares_per48 = soup.find_all(attrs={"data-stat": "ws_per_48"})	
	obpms = soup.find_all(attrs={"data-stat": "obpm"})
	dbpms = soup.find_all(attrs={"data-stat": "dbpm"})
	bpms = soup.find_all(attrs={"data-stat": "bpm"})
	vorps = soup.find_all(attrs={"data-stat": "vorp"})


	filepath = 'data/player_stats/{season}_advanced.csv'.format(
			season=season
		)

	with open(filepath, 'w') as csv_file:
		csv_writer = writer(csv_file)

		headers = ['Player', 'Team', 'GP', 'MP', 'PER', 'TS%', 
					'3PAr', 'FTr', 'ORB%','DRB%', 'TRB%', 'AST%', 
					'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 
					'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']

		csv_writer.writerow(headers)

		for (player, tm, g, mp, per, ts, tpar, ftr, orb, drb, trb, 
			ast, stl, blk, tov, usg, ows, dws, ws, ws_per, obpm,
			dbpm, bpm, vorp) in zip_longest(players, teams, games, 
			minutes, PERs, ts_pct, three_rates, ft_rates, orb_pct, 
			drb_pct, trb_pct, ast_pct, stl_pct, blk_pct, tov_pct, 
			usg_pct, offensive_winshares, defensive_winshares, 
			winshares, winshares_per48, obpms, dbpms, bpms, vorps):


			if player.text == 'Player':
				continue

			csv_writer.writerow([player.text, tm.text, g.text, mp.text,
				per.text, ts.text, tpar.text, ftr.text, orb.text, 
				drb.text, trb.text, ast.text, stl.text, blk.text, tov.text, 
				usg.text, ows.text, dws.text, ws.text, ws_per.text, 
				obpm.text, dbpm.text, bpm.text, vorp.text])

		return


def get_per_100_stats(season="2018-2019"):
	pass
	season_end_year = season.split("-")[1]

	url = "{BASE_URL}/leagues/NBA_{season_end_year}_per_poss.html".format(
			BASE_URL = BASE_URL,
			season_end_year = season_end_year
		)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	players = soup.find_all(attrs={"data-stat": "player"})
	teams = soup.find_all(attrs={"data-stat": "team_id"})
	games = soup.find_all(attrs={"data-stat": "g"})
	minutes = soup.find_all(attrs={"data-stat": "mp"})
	points = soup.find_all(attrs={"data-stat": "pts_per_poss"})
	assists = soup.find_all(attrs={"data-stat": "ast_per_poss"})
	field_goals = soup.find_all(attrs={"data-stat": "fg_per_poss"})
	fg_attempts = soup.find_all(attrs={"data-stat": "fga_per_poss"})
	fg_pct = soup.find_all(attrs={"data-stat": "fg_pct"})
	threes = soup.find_all(attrs={"data-stat": "fg3_per_poss"})
	three_attempts = soup.find_all(attrs={"data-stat": "fg3a_per_poss"})
	three_pct = soup.find_all(attrs={"data-stat": "fg3_pct"})
	free_throws = soup.find_all(attrs={"data-stat": "ft_per_poss"})
	ft_attemps = soup.find_all(attrs={"data-stat": "fta_per_poss"})
	ft_pct = soup.find_all(attrs={"data-stat": "ft_pct"})
	offensive_rebounds = soup.find_all(attrs={"data-stat": "orb_per_poss"})
	defensive_rebounds = soup.find_all(attrs={"data-stat": "drb_per_poss"})
	steals = soup.find_all(attrs={"data-stat": "stl_per_poss"})
	blocks = soup.find_all(attrs={"data-stat": "blk_per_poss"})
	turnovers = soup.find_all(attrs={"data-stat": "tov_per_poss"})
	personal_fouls = soup.find_all(attrs={"data-stat": "pf_per_poss"})
	ortgs = soup.find_all(attrs={"data-stat": "off_rtg"})
	drtgs = soup.find_all(attrs={"data-stat": "def_rtg"})

	filepath = 'data/player_stats/{season}_per100.csv'.format(
			season=season
		)

	with open(filepath, 'w') as csv_file:
		csv_writer = writer(csv_file)

		headers = ['Player', 'Team', 'GP', 'MP', 'PTS', 'AST', 
				   'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA',
				   'FT%', 'ORB', 'DRB', 'STL', 'BLK', 'TOV', 'PF', 'ORtg', 'DRtg']

		csv_writer.writerow(headers)

		for (player, tm, g, mp, pts, ast, fg, fga, fgp, 
			tp, tpa, tpp, ft, fta, ftp, orb, drb, stl, 
			blk, tov, pf, ortg, drtg) in zip_longest(players,
			teams, games, minutes, points, assists, field_goals, 
			fg_attempts, fg_pct, threes, three_attempts, three_pct,
			free_throws, ft_attemps, ft_pct, offensive_rebounds, 
			defensive_rebounds, steals, blocks, turnovers, 
			personal_fouls, ortgs, drtgs):

			if player.text == 'Player':
				continue

			csv_writer.writerow([player.text, tm.text, g.text, mp.text,
				pts.text, ast.text, fg.text, fga.text, fgp.text, 
				tp.text, tpa.text, tpp.text, ft.text, fta.text, 
				ftp.text, orb.text, drb.text, stl.text, blk.text, 
				tov.text, pf.text, ortg.text, drtg.text])	


	return


def get_nba_drafts(year='2018'):
	url = "{BASE_URL}/draft/NBA_{year}.html".format(
			BASE_URL = BASE_URL,
			year = year
		)

	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'html.parser')

	picks = soup.find_all(attrs={'data-stat': 'pick_overall'})
	teams = soup.find_all(attrs={'data-stat': 'team_id'})
	players = soup.find_all(attrs={'data-stat': 'player'})
	years = soup.find_all(attrs={'data-stat': 'seasons'})

	filepath = 'data/drafts/{year}_draft.csv'.format(
		year = year
	)

	with open(filepath, 'w') as csv_file:
		csv_writer = writer(csv_file)
		headers = ['Pick Number', 'Team', 'Player', 'NBA Seasons']

		csv_writer.writerow(headers)

		for pick, team, player, experience in zip_longest(picks, teams, players, years):

			if player.text == 'Player':
				continue

			csv_writer.writerow([pick.text, team.text, player.text, experience.text])

	return 













