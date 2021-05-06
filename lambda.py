person = [
    {"name": "Edgar", "house": "Gamek"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Darco", "house": "Slythenrin"}
]

def f(person):
    return person["house"]

person.sort(key=f)
print(person)
