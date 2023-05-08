import Password_checker
import Password_maker

def password_guessed(keyword, password):
    count = 0
    if Password_checker.password_checker(password) == 0:
        return "Not a strong password!"
    else:
        while True:
            sike = Password_maker.password_generator(keyword)
            if sike != password:
                count += 1
                print(count, sike)
            elif sike == password:
                print("Ok")
                count += 1
                break

            if count > 100000:
                print("It is a damn super password")
                break
    return count


#print(password_guessed("water", "Water^12"))