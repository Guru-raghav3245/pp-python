lsit1 = {'Kohli': 158.73, 'Plessis': 151.06, 'Maxwell': 166.67, 'Bracewell': 100.0}
def strike_rate(batsmen_strike_rates):
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

    print("Relative Performance Indices for Batsmen:")
    for i, relative_performance_index in enumerate(relative_performance_indices):
        relative_performance_index = round(relative_performance_index, 2)
        print(batsmen_names[i], ":", relative_performance_index)

    print("\nMan of the Match:", man_of_the_match_name, "with a strike rate of", man_of_the_match_strike_rate)
    return ""

print(strike_rate(lsit1))