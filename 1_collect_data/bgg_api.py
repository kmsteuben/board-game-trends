from boardgamegeek import BGGClient
# see https://lcosmin.github.io/boardgamegeek/ for documentation

bgg = BGGClient()
hot = bgg.hot_items("boardgame")

hot.items

hot.items[1].rank

hot.items[1].thumbnail

ex_id = hot.items[1].id

g = bgg.game(game_id = ex_id)

dir(g)

# see https://boardgamegeek.com/browse/boardgame for list of top 100 board games
# can use this list to get rank:name and then use above to get info on that game

import pandas as pd

hot_games = pd.read_html("https://boardgamegeek.com/browse/boardgame")[3]
top100 = pd.read_html("https://boardgamegeek.com/browse/boardgame", header = 0)[5]
list(top100) # gets column names

print(tables[3]) #gives hottest games

# Can do same for these pages to get more than top 100
# https://boardgamegeek.com/browse/boardgame/page/2
top200 = pd.read_html("https://boardgamegeek.com/browse/boardgame/page/2", header = 0)[5]

# Function to create dataframe of top x00 games
def create_top_x00(x):
	top_games = pd.read_html("https://boardgamegeek.com/browse/boardgame", header = 0)[5]
	for page in range(2,x+1):
	    temp = pd.read_html("https://boardgamegeek.com/browse/boardgame/page/" + str(page), header = 0)[5]
        top_games = pd.concat([top_games, temp])
		len(top_games)
	return top_games