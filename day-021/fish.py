class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhale.")

# Inheritance
# Fish class is inheriting the methods and attribs from Animal class
class Fish(Animal):
    def __init__(self) -> None:
        # Doing the code below will inherit from Animal class
        super().__init__()

    def breath(self):
        # Doing the code below will enable to override the method
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breath()