Top_Speed = {"Jesko": 330, "Aventador": 218, "Supra": 155, "Tesla S": 200, "Rimac Nivera": 256, "Valkrie": 249,
             "Speedtail": 250, "Venom": 300,}

def topspeed(car, speed):
    car = car.title()
    speed = int(speed)
    if Top_Speed.get(car) == speed:
        print("You are correct!")
    else:
        print("You are not correct!:(")

print(topspeed("venom", 300))
