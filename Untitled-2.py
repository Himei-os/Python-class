class Cake:
    def __init__(self):
        self.__price = 20

    def sell(self):
        print(f'Selling price of the cake is: ${self.__price}')

    def set_price(self, new_price):
        if new_price <= 0:
            print('Price must be POSITIVE.')
        else:
            self.__price = new_price

    def get_price(self):
        return self.__price

cake = Cake()
cake.sell()

cake.__price = 50
cake.sell()

cake.set_price(80)
cake.sell()