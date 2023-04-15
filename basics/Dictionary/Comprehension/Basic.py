# Learning dictionary with comprehension
speed = {"Jesko" : 312, "Speedtail" : 415, "Phantom": 150, "Vantage" : 251, "Centodieci" : 356}
memes = {"Sike" : 2011, "Yo, come check this out!": 2007, "Indian laugh": 2003, "Joe mama" : 2017}

speed_dict = {index: car for index, car in enumerate(speed, start=1)}
print(speed_dict)

index1 = []
car1 = []
for index, car_model in enumerate(speed, start=1):
    index1.append(index)
    car1.append(car_model)

speed_dict1 = dict(zip(index1, car1))
print(speed_dict1)



index2 = []
name2 = []
for index, name in enumerate(memes, start=1):
    index2.append(index)
    name2.append(name)

_dict1 = dict(zip(index2, name2))
print(_dict1)

_dict = {index: name for index, name in enumerate(memes, start=1)}
print(_dict)


speed300 = {}

for car_name in speed:
    if speed[car_name] > 300:
        speed300.update({car_name: speed[car_name]})
print(speed300)

speed3001 = {car_name: speed[car_name] for car_name in speed if speed[car_name] > 300}
print(speed3001)


speed["Centodieci"] = 1010101101
print(speed)