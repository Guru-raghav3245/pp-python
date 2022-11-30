# Given a series of numbers in a sequence from a starting number to end number
# Only one number in the sequence is missing
# Find the missing number

# TIP - This is a Math problem, so solve it first
# You should be able to summarize the approach you are making
# Run some tests manually on paper to ensure that your logic works

# The Coding part will be easy once you can figure out the math
my_sequence = [-5, -4, -3, -2, -1, 0, 2]

if my_sequence[0] - my_sequence[1] == my_sequence[2] - my_sequence[3]:
    for t in range(4):
        if (my_sequence[t]) - (my_sequence[t + 1]) != (my_sequence[t + 2]) - (my_sequence[t + 3]):
            if (my_sequence[t] + 1) - (my_sequence[t + 1]) != (my_sequence[t + 2]) - (my_sequence[t + 3]):
                if (my_sequence[t]) - (my_sequence[t] + 1) != (my_sequence[t + 2]) - (my_sequence[t + 3]):
                    if (my_sequence[t] + 1) - (my_sequence[t + 1]) != (my_sequence[t + 2] + 1) - (my_sequence[t + 3]):
                        if (my_sequence[t]) - (my_sequence[t + 1]) != (my_sequence[t + 2]) - (my_sequence[t + 3] + 1):
                            print("I cant find it, sorry")
                        else:
                            print("    ")