# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2, 8)
# print(p.x)
# print(p.y)

'''

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
 
flinght = Flight(3)

people = ["Edgar", "TEst1", "Outro Test", "Genny"]
for person in people:
    success = flinght.add_passengers(person)
    if success:
        print(f"Added {person} to flight is successfully. ") 
    
    else:
        print(f"No available seats for {person}. ")

        '''

     