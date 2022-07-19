#string concatenation

student = ""

print("The best coder is: " + student)
print("The best coder is:{}".format(student))
print(f"The best coder is:{student}")

adj = input("Adjective:")
verb1 = input("verb1:")
verb2 = input("verb2:")

string = f"The world is so {adj}! \
    It makes me super {verb1} and {verb2}"

print(string)

from sample_madlibs import zombie, hungergames, hp, code
import random

if __name__  == "main":
    m = random.choice([hp,code,zombie,hungergames])
    m.madlib()