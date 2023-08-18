def add(*args): # to define unspecified number of arguements
                # args -> it is a tuple
    tot = 0
    for n in args:
        tot += n
    return tot

def calc(n, **kwargs): # to define unspecified number of KEYWORD arguements
                    # kwargs -> it is a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(add(1,2,3,4,5,6,7,8,9,10))
print(calc(1, add=3,multiply=5))


class Car():
    def __init__(self, **kw) -> None:
        self.make = kw["make"]
        self.model = kw.get("model") # The "get" method will check if a particular key exist, if not, will return empty
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT", seats=4)
print(my_car.make)