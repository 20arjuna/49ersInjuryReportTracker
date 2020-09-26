import requests
from bs4 import BeautifulSoup

url = 'https://www.49ers.com/team/injury-report/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

injury_table = soup.find('table', class_ = 'd3-o-table d3-o-table--row-striping')

#print(injury_table)

for tbody in injury_table.find_all('tbody'):
    for player in tbody.find_all('tr'):
        column = player.find_all('td')
        for i in range(len(column)):
            if(i==0):
                #print(column[i])

                newSoup = BeautifulSoup(str(column[i]), 'html.parser')
                playerHTML = newSoup.find('span', class_ = 'd3-o-player-roster__player-name')


                for ahref in playerHTML.find_all('a'):
                    print("player name: " + ahref.text.strip())
            else:
                print(column[i].text)
