import functools


class Athlete:

    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.silver = 0
        self.copper = 0

    def add_medal(self, medal):
        if medal == 1:
            self.gold += 1
        elif medal == 2:
            self.silver += 1
        elif medal == 3:
            self.copper += 1
        else:
            print("ERROR : ILLEGAL INPUT!")

    def get_gold(self):
        return self.gold

    def get_silver(self):
        return self.silver

    def get_copper(self):
        return self.copper

    def get_medal(self):
        return self.gold + self.silver + self.copper

class Country:

    def __init__(self, name):
        self.name = name
        self.athletes = []
        self.gold = 0
        self.silver = 0
        self.copper = 0
        self.medal = 0

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def calc_all(self):
        for index in self.athletes:
            self.gold += index.get_gold()
            self.silver += index.get_silver()
            self.copper += index.get_copper()
            self.medal += index.get_medal()

    def get_gold(self):
        return self.gold

    def get_silver(self):
        return self.silver

    def get_copper(self):
        return self.copper

    def get_medal(self):
        return self.medal

    def get_name(self):
        return str(self.name)

def cmp_gold(country1, country2):
    if country1.get_gold() < country2.get_gold():
        return 1
    elif country1.get_gold() > country2.get_gold():
        return -1
    else:
        return 1 if country1.get_name() > country2.get_name() else -1

def cmp_medal(country1, country2):
    if country1.get_medal() < country2.get_medal():
        return 1
    elif country1.get_medal() > country2.get_medal():
        return -1
    else:
        return 1 if country1.get_name() > country2.get_name() else -1

def output(countries):
    for index in countries:
        print(str(index.get_name()) + " " +
              str(index.get_gold()) + " " +
              str(index.get_silver()) + " " +
              str(index.get_copper()))

def print_():
    str = "-----"
    print(str)
if __name__ == '__main__':
    n = int(input())
    arr = []
    countries = {}
    athletes = {}

    # input countries
    for i in range(0, n):
        arr = input().split(" ")
        country = Country(arr[0])
        countries[arr[0]] = country
        for j in range(1, len(arr)):
            athlete = Athlete(arr[j])
            athletes[arr[j]] = athlete
            country.add_athlete(athlete)

    # input medals
    m = int(input())
    for i in range(0, m):
        arr = input().split(" ")
        athletes[arr[0]].add_medal(int(arr[1]))

    # dict -> list
    for index in countries.values():
        index.calc_all()

    country_list = list(countries.values())
    # sort in gold
    country_list.sort(key=functools.cmp_to_key(cmp_gold))
    """
    for index in country_list:
        print(str(index.get_name()) + " " +
              str(index.get_gold()) + " " +
              str(index.get_silver()) + " " +
              str(index.get_copper()))
    """
    output(country_list)
    print_()
    # sort in medal
    country_list.sort(key=functools.cmp_to_key(cmp_medal))
    """
    for index in country_list:
        print(str(index.get_name()) + " " +
              str(index.get_gold()) + " " +
              str(index.get_silver()) + " " +
              str(index.get_copper()))
    """
    output(country_list)

