import requests
from bs4 import BeautifulSoup

url = 'https://www.49ers.com/team/injury-report/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

injury_table = soup.find('table', class_ = 'd3-o-table d3-o-table--row-striping')

#print(injury_table)

injuryMatrix = []
for tbody in injury_table.find_all('tbody'):

    player = tbody.find_all('tr')
    for i in range(len(player)):
        column = player[i].find_all('td')
        temp = []
        for j in range(len(column)):

            if(j==0):
                #print(column[i])

                newSoup = BeautifulSoup(str(column[j]), 'html.parser')
                playerHTML = newSoup.find('span', class_ = 'd3-o-player-roster__player-name')


                for ahref in playerHTML.find_all('a'):
                    print("player name: " + ahref.text.strip())
                    temp.append(ahref.text.strip())
            else:
                print(column[j].text)
                temp.append(column[j].text.strip())

        injuryMatrix.append(temp)
        #print(temp)

print(injuryMatrix)