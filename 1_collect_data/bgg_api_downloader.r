install.packages("httr")
library(httr)


url <- "https://www.boardgamegeek.com/xmlapi2/"

path <- "thing?id=013"

test4 <- GET("https://www.boardgamegeek.com/xmlapi2/hot?boardgame")

View(test)
