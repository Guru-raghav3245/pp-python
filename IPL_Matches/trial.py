def calculating_batsmen_strike_rate(file):
    file = open(file, "r")
    batsmen_strike_rates = {}
    for line in file:
        line = line.strip().split(",")
        if line[0] == "bat":
            runs = int(line[2])  #
            balls = int(line[3])
            fours = int(line[4])
            sixes = int(line[5])
            overs = int(line[3]) // 6
            strike_rate = (runs / balls) * 100
            strike_rate = round(strike_rate, 2)
            player_name = line[1]

            batsmen_strike_rates.update({
                player_name: {
                    "strike_rate": strike_rate,
                    "runs": runs,
                    "fours": fours,
                    "sixes": sixes,
                    "overs": overs
                }
            })
    file.close()
    return batsmen_strike_rates


def calculating_man_of_the_match(batsmen_strike_rates):
    max_score = 0
    man_of_the_match_name = ""
    sum_sr = 0
    max_sr = 0
    for player_name, stats in batsmen_strike_rates.items():
        strike_rate = stats["strike_rate"]
        runs = stats["runs"]
        fours = stats["fours"]
        sixes = stats["sixes"]
        overs = stats["overs"]
        score = runs * strike_rate + fours * 4 + sixes * 6 + overs * 10
        sum_sr += strike_rate
        if score > max_score:
            max_score = score
            man_of_the_match_name = player_name
            max_sr = strike_rate

    average_strike_rate = sum_sr / len(batsmen_strike_rates)
    relative_performance_index_motm = (max_sr / average_strike_rate) * 100
    return man_of_the_match_name, max_score, round(relative_performance_index_motm, 1)


# Bowlers
def getting_players(file_name):
    file = open(file_name, "r")
    economy_list = []
    bowler_name_list = []
    for each in file:
        each = each.strip().split(",")
        if each[0] == "ball" and len(each) >= 4:
            if each[-1].endswith("\n"):
                each[-1] = each[-1][:-1]
            economy = int(each[2]) / float(each[3])
            economy = round(economy, 2)
            bowler_name = each[1]
            economy_list.append(economy)
            bowler_name_list.append(bowler_name)
    file.close()
    return bowler_name_list, economy_list



def comparing_bowlers(bowler_name_list, economy_list):
    bowler_economy = economy_list
    average_economy = sum(bowler_economy) / len(bowler_economy)
    bowler_list = dict(zip(bowler_economy, bowler_name_list))
    bowler_economy = sorted(bowler_economy)
    best_economy = bowler_economy[0]
    points = (average_economy / best_economy) * 1000
    return points, bowler_list[best_economy]


if __name__ == "__main__":
    print("_" * 10, "Calculation", "_" * 10)
    players = getting_players("Match 2")
    bowl = comparing_bowlers(players[0], players[1])
    bat = calculating_man_of_the_match(calculating_batsmen_strike_rate("Match 2"))
    if float(bowl[0]) > float(bat[1]):
        print("The man of the match is", bowl[1], "with a score of - ", round(bowl[0], 2))
    else:
        print("The man of the match is", bat[0], "with a score of - ", bat[1])
