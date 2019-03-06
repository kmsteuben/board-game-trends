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

