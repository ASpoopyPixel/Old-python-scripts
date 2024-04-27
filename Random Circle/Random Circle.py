import random
import math

def main():
    radius = random.uniform(1, 100)
    area = calculateArea(radius)
    print('Your randomly generated radius is:', format(radius, '.2f'))
    print('Your area is:', format(area, '.2f'))

def calculateArea(getRadius):
    area = math.pi * getRadius ** 2
    return area

main()
    
