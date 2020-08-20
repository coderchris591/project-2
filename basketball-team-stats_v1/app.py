from constants import TEAMS, PLAYERS
import copy
import random


players = copy.deepcopy(PLAYERS)
teams = copy.deepcopy(TEAMS)
num_players_team = int(round(len(players) / len(teams)))



if __name__ == "__main__":

    def clean_data():
        for player in players:
            s = player['height'].split()
            for number in s:
                if number.isdigit():
                    heights = int(number)
        for player in players:
            if player['experience'] == 'YES':
                experience = True
            elif player['experience'] == 'NO':
                experience = False
    clean_data()

    player_list = []

    def balance_teams():
        for player in players:
            p = player['name']
            player_list.append(p)
            random.shuffle(player_list)
    balance_teams()


    def start():
        stars = '*'*37
        print('\n',stars,'\n', 'WELCOME TO THE BASKETBALL STATS TOOL!', '\n',stars)

        while True:
            try:
                choice = int(input(' \n 1) Display Team stats \n 2) Quit \n\n Enter an option >  '))
            except ValueError as e:
                print(' \nPlease choose 1 or 2')
            else:
                if choice == 1:
                    print('\n 1) Panthers \n\n 2) Bandits \n\n 3) Warriors')
                    try:
                        team_select = int(input('\nWhich team would you like to see?  '))
                    except ValueError as e:
                        print("\nPlease choose team 1, 2 or 3")
                    else:
                        if team_select > 3 or team_select < 1:
                            print("Please choose team 1, 2 or 3")
                        elif team_select == 1:
                            print(" \nTeam: Panthers \n\n Number of Players:", num_players_team, "\n\n Players:")
                            print(*player_list[0:6], sep=', ')
                        elif team_select == 2:
                            print(" \nTeam: Bandits \n\n Number of Players:", num_players_team, "\n\n Players:")
                            print(*player_list[6:12], sep=', ')
                        elif team_select == 3:
                            print(" \nTeam: Warriors \n\n Number of Players:", num_players_team, "\n\n Players:")
                            print(*player_list[12:18], sep=', ')
                    try:
                        cont = input('\nPress ENTER to continue...')
                    except SyntaxError as e:
                        pass
                elif choice == 2:
                    print('quitting...')
                    quit()
                else:
                    print('Oops, thats not a 1 or a 2 -- try again')
    start()
