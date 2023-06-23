batsmen_strike_rates = [135, 120, 110, 125, 130]
average_strike_rate = sum(batsmen_strike_rates) / len(batsmen_strike_rates)

relative_performance_indices = []
for i, strike_rate in enumerate(batsmen_strike_rates):
    relative_performance_index = (strike_rate / average_strike_rate) * 100
    relative_performance_indices.append(relative_performance_index)

max_index = 0
max_relative_performance_index = relative_performance_indices[0]
for i, relative_performance_index in enumerate(relative_performance_indices):
    if relative_performance_index > max_relative_performance_index:
        max_index = i
        max_relative_performance_index = relative_performance_index

man_of_the_match_strike_rate = batsmen_strike_rates[max_index]

print("Relative Performance Indices for Batsmen:")
for i, relative_performance_index in enumerate(relative_performance_indices):
    print("Batsman", i+1, ":",relative_performance_index)

print("\nMan of the Match: Batsman", max_index+1, "with a strike rate of", man_of_the_match_strike_rate)


