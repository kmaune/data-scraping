import requests
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest
from parsers import *

seasons = ['2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015', '2013-2014', '2012-2013']
drafts = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012']

for season in seasons: 
	get_per_game_stats(season)
	get_advanced_stats(season)
	get_per_100_stats(season)

for draft in drafts:
	get_nba_drafts(draft)



	




	
