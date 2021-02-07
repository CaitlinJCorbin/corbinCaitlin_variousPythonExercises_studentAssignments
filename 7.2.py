'''
Caitlin J. Corbin
Intro to Python
7.2
6/22/2020
'''
class Stock:
    def __init__(self, symbol, name, previous_price, current_price):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = current_price

def getName(self):
    return self.__name
def getSymbol(self):
    return self.__symbol
def getPreviousClosingPrice(self):
    return self.__previousClosingPrice
def getCurrentPrice(self):
    return self.__currentPrice
def getChangePercent(self):
    prev = self.__previousClosingPrice
    current = self.__currentPrice
    return(current - prev) / prev * 100
def setPreviousClosingPrice(self, previous_price):
    self.__previousClosingPrice = previous_price
def setCurrentPrice(self, current_price):
    self.__currentPrice = current_price

def main():
    fakecompany = Stock("ABCD", "TESTCOMP", 10.23, 45.67)
