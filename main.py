from elosports.elo import Elo
import csv

"""
    General Outline:
    1. Get player information and store in a dictionary (name, player_id).
    2. Create Elo object, pass player_id's to object
        - Note, ELO will keep track of current ratings
    3. Create a second dictionary that holds peak ELO values, update after each 
       match
    4. Iterate through match data
"""

# Description: This function reads filename and stores the a tuple 
#              (name_last, name_first) in a dictionary where player_id is the 
#              key.
# Assumptions: Assumes that matches/tennis_atp/atp_players.csv exists (if no other
#              filename is given)
# Output:      Returns a dictionary where player_id is the key and the value is 
#              a tuple (first_name, last_name).
def getPlayerData(filename = 'matches/tennis_atp/atp_players.csv'):
    # create a dictionary to return the calling functiono
    playerDict = {}

    # open file
    with open(filename) as csvfile:
        # create an object that helps read the csv file
        readCSV = csv.reader(csvfile, delimiter=',')

        # 0 - player_id, 1 - name_first, 2 - name_last
        colIndex = [0, 1, 2]

        # read first line (header) of the csv 
        next(readCSV)
        for row in readCSV:
            # create a helper variable to store player_id, name_first, and 
            # name_last
            playerInfo = []
            for i in colIndex:
                # get player_id, name_first, name_last from csv
                playerInfo.append(row[i])
            # create a tuple to store name_first and name_last
            name = (row[1], row[2])

            # add an entry to playerDict where key = player_id and value = name
            playerDict[row[0]] = name
    return playerDict

# Description: This function initializes the Elo object located in elosports
#              and adds all of the players in playerData to it.
# Output:      Returns an Elo object.
def initEloCalculator(playerData, k = 20, g = 1, homefield = 0):
    tmp = Elo(k = k, g = g, homefield = homefield)
    for key in playerData:
        tmp.addPlayer(key)
    return tmp

def main():
    playerData = getPlayerData()
    eloCalculator = initEloCalculator(playerData)


if __name__ == '__main__':
    main()