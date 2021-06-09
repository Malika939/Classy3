class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        #Динамические поля
        self.name = name
        self.age = age
        #Приватные поля
        self.__money = 0
        self.__house = None


    def info(self):
        print(f'Name: {self.name}')
        print(f'Name: {self.age}')
        print(f'Name: {self.__house}')
        print(f'Name: {self.__money}')

    #статические поля
    @staticmethod
    def default_info():
        print(f'Имя по умолчанию{Human.default_name}') 
        print(f'Возраст по умолчанию: {Human.default_age}')

    #приватный метод
    def __make_deal():
        pass



class Haus:
    #Динамические поля
    def __init__(self, area, price):
        self._area = area
        self._price = price


    def final_price(self, discount):
        final_price = self._price * (100 -discount) / 100
        print(f,'Финальный прайс:{final_price')
        return final_price

class SmallHaus(Human):
    def __init__(self, name, age):
        super().__init__(name=name, age=age)





if __name__== "__main__":
    Malika = Human('Malika', 35)
    Malika.info()      
