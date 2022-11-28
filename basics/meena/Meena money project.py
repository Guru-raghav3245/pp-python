money = int(input("Enter amount - "))

if money / 500 > 0:
    quo = int(money / 500)
    print("Rs 500:", quo)
    hundred = money % 500

    if money / 100 > 0:
        hun = int(hundred / 100)
        print("Rs 100:", hun)
        fif = money % 100

        if money / 50 > 0:
            fifty = int(fif / 50)
            print("Rs 50:", fifty)
            tens = money % 50

            if money / 10 > 0:
                two = int(tens / 10)
                print("Rs 10:", two)
                ones = money % 10



