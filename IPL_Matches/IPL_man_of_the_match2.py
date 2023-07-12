def calculating_batsmen_strike_rate(file):
    file = open(file, "r")
    batsmen_strike_rates = {}
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "bat":
            runs = int(line[1])
            balls = int(line[2])
            fours = int(line[3])
            sixes = int(line[4])
            overs = balls // 6
            strike_rate = (runs / balls) * 100
            strike_rate = round(strike_rate, 2)
            player_name = line[-1]

            # Add the batsman data to the batsmen_strike_rates dictionary
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
        # Calculate a score based on a combination of criteria
        score = runs * strike_rate + fours * 4 + sixes * 6 + overs * 10
        sum_sr += strike_rate
        if score > max_score:
            max_score = score
            man_of_the_match_name = player_name
            max_sr = strike_rate

    average_strike_rate = sum_sr / len(batsmen_strike_rates)
    relative_performance_index_motm = (max_sr / average_strike_rate) * 100
    # print("\nPerformance Metrics for Batsmen")
    for player_name, stats in batsmen_strike_rates.items():
        strike_rate = stats["strike_rate"]
        runs = stats["runs"]
        fours = stats["fours"]
        sixes = stats["sixes"]
        overs = stats["overs"]
        # print("     ", player_name, "- Runs:", runs, ", Strike Rate:", strike_rate, ", Fours:", fours, ",Sixes:", sixes,
        # ", Overs Played:", overs)
    # return [man_of_the_match_name, max_score, round(relative_performance_index_motm, 1)]
    return max_score



# Bowlers
def getting_players(file_name):
    file = open(file_name, "r")
    economy_list = []
    bowler_name_list = []
    for each in file:
        if each[1] == "o":
            if each.__contains__("\n"):
                each.replace("\n", "")
            each = each.split(" ")
            economy = int(each[1]) / float(each[2])
            economy = economy.__round__(2)
            bowler_name = each[-2]
            if bowler_name.__contains__("\n"):
                bowler_name.replace("\n", "")
            if int(each[-1]) == 2 or int(each[-1]) > 2:
                economy_list.append(economy)
                bowler_name_list.append(bowler_name)
    return bowler_name_list, economy_list


def comparing_bowlers(bowler_name_list, economy_list):
    bowler_economy = economy_list
    average_economy = sum(bowler_economy) / len(bowler_economy)
    bowler_list = dict(zip(bowler_economy, bowler_name_list))
    bowler_economy = sorted(bowler_economy)
    best_economy = bowler_economy[0]
    points = (average_economy / best_economy) * 1000
    # print(points)
    return points, bowler_list[best_economy]


if "__main__" == __name__:
    print("_"*10, "Calculation", "_"*10)
    bowl = comparing_bowlers(getting_players()[0], getting_players()[1])
    bat = calculating_man_of_the_match(calculating_batsmen_strike_rate("Match 1"))
    if float(bowl) > float(bat):
        print("The man of the match is ", bowl)
    else:
        print("The man of the match is ", bat)

