import ipdb 

class Human:
    # class attributes 
    population = 0 #all the people who have ever existed
    living = 0 
    extinct = True 
    num_in_space = 0

    def __init__(self, age=0, height=1, weight=8, name=''):
        Human.add_person()
        self.age = age 
        self.height = height
        self.weight = weight 
        self.name = name
        #instance attributes 

    #instance methods
    def is_legal(self):
        return self.age >= 18
    def say_hello(self):
        return f'Hi my name is {self.name}'
    def tall_enough(self):
        return self.height > 60

    #class methods
    @classmethod 
    def go_to_space(cls):
        cls.num_in_space += 1
    @classmethod 
    def add_person(cls):
        Human.population += 1
        Human.living += 1
        Human.extinct = False 
    @classmethod 
    def remove_person(cls, num=1):
        cls.living -= num
        if(cls.living == 0):
            cls.extinct = True

#instances of Human class 
human1 = Human(age=30, height=68, weight=154, name="Alice")
human2 = Human(age=25, height=64, weight=121, name="Bob")
human3 = Human(age=40, height=71, weight=176, name="Charlie")
human4 = Human(age=35, height=67, weight=143, name="Diana")
human5 = Human(age=28, height=65, weight=132, name="Eve")


ipdb.set_trace()

