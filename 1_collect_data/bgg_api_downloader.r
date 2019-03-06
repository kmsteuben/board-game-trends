install.packages("httr")
library(httr)
library(xml2)
library(XML)


url <- "https://www.boardgamegeek.com/xmlapi2/"

path <- "thing?id=013"

test <- GET("https://www.boardgamegeek.com/xmlapi2/hot?boardgame")

temp <- content(test, "parsed")



xml_hotlist <- cat(content(test, "text"), "\n")

http://www.informit.com/articles/article.aspx?p=2215520

read_xml(cat(content(test, "text"), "\n"))

