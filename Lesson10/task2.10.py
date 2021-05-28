# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
class Dog :
    Agefactor = 7

    def __init__(self, dog_age) :
        self.dog_age = dog_age

    def human_age(self) :
        self.human_age = self.dog_age * self.Agefactor
        print(f'The dog’s age in human equivalent is {self.human_age}')


my_dog = Dog(float(input('Hove old is your dog ?\n')))
my_dog.human_age()
