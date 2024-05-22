def first():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(self.restaurant_name, " ", self.cuisine_type)
        def open_restaurant(self):
            print(self.restaurant_name, " открыт")
    class icecreamstand(restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            self.flavors = flavors
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def flavor(self):
            for flavor in self.flavors:
                print(flavor)
    icecreamstand = icecreamstand("морожка","мороженое",["клубничное","ванильное"])
    icecreamstand.flavor()





def second():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type,rate):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rate = rate
        def describe_restaurant(self):
            print(self.restaurant_name, " ", self.cuisine_type)
        def open_restaurant(self):
            print(self.restaurant_name, " открыт")
        def rate(self,new_rate):
            self.rate = new_rate
            print("новое значение: ", self.new_rate)

    class icecreamstand(restaurant):
        def __init__(self, restaurant_name, cuisine_type, type, flavors, rate, location, hours):
            self.rate = rate
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.flavors = flavors
            self.location = location
            self.hours = hours
            self.type = type
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
        def del_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
        def prov_flavor(self, flavor):
            return flavor in self.flavors
        def flavors(self):
            print("Сорта мороженого: ")
            for flavor in self.flavors:
                print(flavor)
        def type(self):
            print("Вид мороженого: ")
            for flavor in self.flavors:
                print(flavor)

    icecreamstand = icecreamstand("морожка", "мороженое", ["на палочке", "в рожке"],["банановое", "апельсиновое"], 4, "ул. Кузбасская, д. 15", "10:00 - 18:00")

    icecreamstand.add_flavor("Ванильное")
    icecreamstand.add_flavor("Шоколадное")
    icecreamstand.add_flavor("Клубничное")

    icecreamstand.del_flavor("Клубничное")

    print(icecreamstand.prov_flavor("Клубничное"))
    icecreamstand.type()
second()