import random
import time
from players import *


def simulate_duel(player1, player2):
    p1_aim = player1["aim"]
    p2_aim = player2["aim"]
    difference = abs(p1_aim - p2_aim)

    if p1_aim > p2_aim:
        p1_aim = p1_aim + difference
    else:
        p2_aim = p2_aim + difference

    total = p1_aim + p2_aim

    p1_prob = round(((p1_aim / total) * 100),1)
    p2_prob = 100 - p1_prob

    # FOR DISPLAYING A PLAYER'S DUEL WIN PROBABILITY
    '''print(f'{player1["name"]}: {p1_prob}% \n'
          f'{player2["name"]}: {p2_prob}%')'''

    x = random.randint(1, 1000) / 10
    '''print(x)'''

    if x <= p1_prob:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1

    return [winner,loser]


class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

        self.team1_players_dicts = team1["players"]
        self.team2_players_dicts = team2["players"]

        self.round_num = 1
        self.t1_score = 0
        self.t2_score = 0

        self.match_stats = []


    def get_team_info(self):
        teams = [self.team1, self.team2]

        for team in teams:
            print(team["name"])
            players = ''

            for player in team["players"]:
                players = players + f'{player["name"]} '

            players = players + f'\n'
            print(players)


    def create_stats_dict(self):
        for player in self.team1_players_dicts + self.team2_players_dicts:
            player_name = player["name"]
            self.match_stats.append({"name": player_name, "kills": 0, "deaths": 0})


    def show_stats(self):
        sorted_stats = sorted(self.match_stats, key=lambda x: x["kills"], reverse=True)
        for stats_dict in sorted_stats:
            name = stats_dict["name"]
            kills = stats_dict["kills"]
            deaths = stats_dict["deaths"]
            print(f'{name}: {kills}K {deaths}D')


    def update_stats(self, player_add_kill, player_add_death):
        for player_stats_dict in self.match_stats:
            if player_add_kill["name"] == player_stats_dict["name"]:
                player_stats_dict["kills"] += 1

            if player_add_death["name"] == player_stats_dict["name"]:
                player_stats_dict["deaths"] += 1


    def simulate_match(self):
        self.create_stats_dict()

        while self.t1_score < 13 and self.t2_score < 13:
            self.simulate_round()
            '''time.sleep(2)'''
            print(f'{self.team1["name"]} {self.t1_score} - {self.t2_score} {self.team2["name"]} \n')

        if self.t1_score == 13:
            print(f'{self.team1["name"]} has won the match! \n')
        elif self.t2_score == 13:
            print(f'{self.team2["name"]} has won the match! \n')

        self.show_stats()


    def simulate_round(self):
        team1_alive_players = list(self.team1_players_dicts)
        team2_alive_players = list(self.team2_players_dicts)

        while len(team1_alive_players) > 0 and len(team2_alive_players) > 0:
            team1_player = random.choice(team1_alive_players)
            team2_player = random.choice(team2_alive_players)

            duel_result = simulate_duel(team1_player, team2_player)
            duel_winner = duel_result[0]
            duel_loser = duel_result[1]

            # FOR DELAY BETWEEN KILLS
            '''time.sleep(0.5)'''
            print(f'{duel_winner["name"]} has killed {duel_loser["name"]}')
            self.update_stats(duel_winner, duel_loser)

            if duel_winner == team1_player:
                team2_alive_players.remove(duel_loser)
            elif duel_winner == team2_player:
                team1_alive_players.remove(duel_loser)

        '''time.sleep(0.5)'''
        if len(team1_alive_players) == 0:
            print(f'{self.team2["name"]} has won the round! \n')
            self.t2_score = self.t2_score + 1

        elif len(team2_alive_players) == 0:
            print(f'{self.team1["name"]} has won the round! \n')
            self.t1_score = self.t1_score + 1

        self.round_num = self.round_num + 1

        # FOR CHECKING WHO IS STILL ALIVE
        '''print(f'TEAM 1: \n'
              f'{team1_alive_players} \n'
              f'\n'
              f'TEAM 2: \n'
              f'{team2_alive_players}')'''


match = Match(Titans, TheFireNation)
match.simulate_match()









