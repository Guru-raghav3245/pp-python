def calculating_batsmen_strike_rate():
    file = open("IPL_man_of_the_match", "r")
    batsmen = {}
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "bat":
            runs = int(line[1])
            balls = int(line[2])
            strike_rate = (runs / balls) * 100
            strike_rate = round(strike_rate, 2)
            player_name = line[3]
            print(player_name, "Strike Rate:", strike_rate)
            batsmen[player_name] = strike_rate
    file.close()
    return batsmen

def calculating_man_of_the_match(batsmen_strike_rates):
    ans = []
    average_strike_rate = sum(batsmen_strike_rates.values()) / len(batsmen_strike_rates)

    relative_performance_indices = []
    for i, strike_rate in enumerate(batsmen_strike_rates.values()):
        relative_performance_index = (strike_rate / average_strike_rate) * 100
        relative_performance_indices.append(relative_performance_index)

    max_index = 0
    max_relative_performance_index = relative_performance_indices[0]
    for i, relative_performance_index in enumerate(relative_performance_indices):
        if relative_performance_index > max_relative_performance_index:
            max_index = i
            max_relative_performance_index = relative_performance_index

    batsmen_names = list(batsmen_strike_rates.keys())
    man_of_the_match_name = batsmen_names[max_index]
    man_of_the_match_strike_rate = batsmen_strike_rates[man_of_the_match_name]

    print("\nRelative Performance Indices for Batsmen")
    for i, relative_performance_index in enumerate(relative_performance_indices):
        relative_performance_index = round(relative_performance_index, 2)
        print("     ", batsmen_names[i], ":", relative_performance_index)

    print("\nMan of the Match:", man_of_the_match_name, "with a strike rate of", man_of_the_match_strike_rate)
    ans.append(man_of_the_match_name)
    ans.append(man_of_the_match_strike_rate)
    return ans


if __name__ == "__main__":
    print("_"*10, "Man of the Match", "_"*10)
    print(calculating_man_of_the_match(calculating_batsmen_strike_rate()))










# Bowling
def getting_players():
    file = open("Input for ipl", "r")
    batsmen = {}
    economy_list = []
    bowler_name_list = []
    for each in file:
        if each[1] == "o":
            if each.__contains__("\n"):
                each.replace("\n", "")
            each = each.split(" ")
            economy = int(each[1]) / float(each[2])
            economy = economy.__round__(2)
            print(economy, "This is economy")
            bowler_name = each[-1]
            if bowler_name.__contains__("\n"):
                bowler_name.replace("\n", "")
            economy_list.append(economy)
            bowler_name_list.append(bowler_name)
    return batsmen, bowler_name_list, economy_list


def comparing(bowler_name_list, economy_list):
    bowler_economy = economy_list
    average_economy = sum(bowler_economy) / len(bowler_economy)

    relative_performance_indices = []
    for i, economy in enumerate(bowler_economy):
        relative_performance_index = (average_economy / economy) * 100
        relative_performance_indices.append(relative_performance_index)
    bowlers = dict(zip(bowler_name_list, relative_performance_indices))
    bowler_name_list = dict(sorted(bowlers.items(), key=lambda x: x[1], reverse=True))
    print("Relative Performance Indices for Batsmen:")
    best_bowler = ""
    best_economy = 0
    for i, name in enumerate(bowler_name_list):
        x = name
        if name.__contains__("\n"):
            x = name.replace("\n", "")
        bowler_name_list[name] = bowler_name_list[name].__round__(2)
        print(x, ":", bowler_name_list[name])
        if i == 0:
            best_bowler = name
            best_economy = bowler_name_list[name]
            best_economy = best_economy.__round__(2)

    print("The best bowler is ", best_bowler, "with an economy of ", best_economy)
    x = [best_bowler, best_economy]
    return x

