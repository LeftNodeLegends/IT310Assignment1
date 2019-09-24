#Pip Installed matplotlib

import random
import matplotlib.pyplot as plt


birthdays = []
counter = 0
chance = []
xaxis = []
yaxis = []


#Creates graph from data in checkDuplicate function
def graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Number of people')
    plt.ylabel('Percentage')
    plt.title('Chances of Duplicate Birthdays in a Group of People')
    plt.show()


def checkDuplicate(birthday, c, length):
    birthday.sort()
    for i in range(length - 1):
        if birthday[i] == birthday[i+1]:
            c += 1
            chance.append(1)
            break
    birthday.clear()


def main():
    x = 5
    while x <= 50:
        for n in range(1000):
            for y in range(x):
                birthdays.append(random.randrange(365))
            checkDuplicate(birthdays, counter, x)
        percent = "{0:.0%}".format(len(chance)/1000)
        print("With a pool of", x, "people, there's a", percent, "chance of having duplicate"
                                                                                            " birthdays")
        xaxis.append(x)
        yaxis.append(percent)
        x += 1

        chance.clear()

main()
graph(xaxis, yaxis)
