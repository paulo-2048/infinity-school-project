
class Sale:
    def __init__(self, idCode, name, price, category):
        self.__idCode = idCode
        self.__name = name
        self.__price = price
        self.__category = category

    @property
    def idCode(self):
        return self.__idCode

    @idCode.setter
    def idCode(self, value):
        self.__idCode = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value
