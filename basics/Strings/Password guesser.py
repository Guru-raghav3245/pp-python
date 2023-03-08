import Password_checker
import Password_maker

def password_guessed(keyword, password):
    count = 0
    if Password_checker.password_checker(password) == 0:
        return "Not a strong password!"
    else:
        while True:
            if Password_maker.password_generator(keyword) != password:
                count += 1
                continue
            else:
                count += 1
                break
    return count
print(password_guessed("water", "Water^12"))