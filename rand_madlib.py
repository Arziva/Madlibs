from sample_madlibs import zombie, hungergames, hp, code
import random

if __name__  == "main":
    m = random.choice([hp,code,zombie,hungergames])
    m.madlib()