import random


def primary():
    # print("Keep it logically awesome.")

    noList = ['N', 'n', 'NO', 'no', 'No']
    yesList = ['Y', 'y', 'YES', 'yes', 'Yes']
    while True:
        inp = input('Add a new quote? (Y/N): ')
        if inp in noList:
            break
        elif inp in yesList:
            f = open("quotes.txt", 'a')
            nextQuote = input('New quote: ')
            nextQuote = nextQuote + '\n'
            f.write(nextQuote)
            f.close()
        else:
            print('Input not recognised!')

    f = open("quotes.txt", 'r')
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    rnd1 = rnd
    while rnd1 == rnd:
        rnd1 = random.randint(0, last)
    q0 = quotes[rnd]
    q1 = quotes[rnd1].strip()
    print(q0, q1)


if __name__ == "__main__":
    primary()
