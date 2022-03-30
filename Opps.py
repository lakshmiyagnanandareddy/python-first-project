def main():
    class Game:

        def __init__(self, type):
            self.typeOfGame = type

        def game_score(self, score):
            self.scoreOfGame = score

        def show_game_type(self):
            return self.typeOfGame

        def show_game_score(self):
            return self.scoreOfGame

    print("What type of game you want to play")
    print("Enter 1 - if you want to play adventure game.\n"
          "Enter 2 - if you want to play action game.\n")
    try:
        Gtype = int(input())
        if Gtype == 1:
            Gtype = "Adventure"
        elif Gtype == 2:
            Gtype = "Action"
    except:
        Gtype = int(input("enter either 1 or 2"))
    myGame = Game(Gtype)
    print("you are tried to play", myGame.show_game_type())
    Gtype = int(input("Enter the highest score"))
    myGame.game_score(Gtype)
    print("your highest score is ", myGame.show_game_score())
    print("your data has been saved successfully")
    print("you have played", myGame.show_game_type(), "game", "\n"
                                                              "your highest score is", myGame.show_game_score())


def main1():
    class Car:

        def __init__(self, collection_car):  # __init__ - takes input from the object.
            self.__car = collection_car  # using self.car we can make contact between class and object

        def set_car(self, change_collection_car):
            self.__car = change_collection_car

        def show_car(self):
            return self.__car

        def __str__(self):
            return self.__car + " had been broughted by you."  # This will allows us to add string in 'return' function only.

    print("welcome to nandu website")
    print("which car you want to buy")
    print("Enter (1: Toyota, 2: Benz, 3: Tesla,4: Nission)")
    choice = int(input())
    if choice == 1:
        choice = "Toyota"
    elif choice == 2:
        choice = "Benz"
    elif choice == 3:
        choice = "Tesla"
    elif choice == 4:
        choice = "Nission"
    owned_car = Car(choice)
    print(owned_car)
    correction = input("If you want to change the car,Enter y - yes or n - no.")
    if correction.lower() == "y":
        print("Enter (1: Toyota, 2: Benz, 3: Tesla, 4: Nission.)")
        choice = int(input())
        if choice == 1:
            choice = "Toyota"
        elif choice == 2:
            choice = "Benz"
        elif choice == 3:
            choice = "Tesla"
        elif choice == 4:
            choice = "Nission"
    owned_car.set_car(choice)
    print("congrats!!!")
    print("you had brought a new", owned_car.show_car(), "car")
    print(owned_car)


def mainex():
    class Employee():
        def __init__(self, ):
            self.name = ""
            self.Id = ""
            self.shift = ""

        def employee_name(self, name):
            self.name = name

        def employee_Id(self, Id):
            self.Id = Id

        def employee_shift(self, shift):
            self.shift = shift

        def show_employee_name(self):
            return self.name

        def show_employee_Id(self):
            return self.Id

        def show_employee_shift(self):
            return self.shift

    my_employee_information = Employee()

    def main():
        print("welcome to Software solution")
        print("Enter your name : ")
        name = input()
        print("Enter your id number : ")
        id = input()
        print("Enter your work shift : ")
        shift = input("Enter 'morning' for morning shift,'afternoon' for afternoon shift :")
        assign(my_employee_information, name, id, shift)

        print("Name : ", my_employee_information.show_employee_name())
        print("ID : ", my_employee_information.show_employee_Id())
        print("shift : ", my_employee_information.show_employee_shift())

    def assign(my_employee_information, name, id, shift):
        my_employee_information.employee_name(name)
        my_employee_information.employee_Id(str(id))
        my_employee_information.employee_shift(shift.lower())

    main()


def mainex1():
    class Basket:

        def __init__(self, name, price):
            self.name = name
            self.price = price

        def show_name(self):
            return self.name

        def show_price(self):
            return self.price

    def main():
        def Price():
            print("Enter the price of the fruit")
            try:
                price = int(input())
            except:
                print("Enter Integer values")
                Price()
            return price
        my_list = list()
        again = "y"
        while again == "y":
            print("Enter the fruit name : ")
            name = input()

            price = Price()
            show = Basket(name, price)
            my_list.append(show)
            again = input("Do you want to add other fruit to basket,Enter y-yes and n- no : ")
        print("Here is your basket : ")
        for i in my_list :
            print(i.show_name(), "is", i.show_price())

    main()


#mainex1()
def mainex2():
    class CreateFile:
        def __init__(self, contact_name, contact_phone_number):
            self.name = contact_name
            self.phone_number = contact_phone_number

        def __str__(self):
            return "name : " + self.name + " phone number :" + self.phone_number

        def create_file(self, file_name):
            file = open(file_name, "wt")
            file.write(self.name + "\n")
            file.write(self.phone_number + "\n")
            file.close()
            print("your data has been saved successfully")

    def main():
        contact_name = input("Enter your name : ")
        contact_phone_number = int(input("Enter your contact number"))
        contact_object = CreateFile(str(contact_name), str(contact_phone_number))
        file_name = input("Enter the name you would like to save : ")
        file_name = file_name + ".txt"
        contact_object.create_file(file_name)
        print(contact_object)
        print("your file ", file_name, "has been succesfully saved")

    main()


def inherit():
    class Account:  # This is the super class
        def __init__(self, bank, account_type):
            self.bank = bank
            self.account_type = account_type

        def show_bank(self):
            return self.bank

        def show_saving(self):
            return self.account_type

    class BankAccount(Account):  # subclass - a class which inherits the properties of the super class.
        def __init__(self, bank, account_type, name, amount):

            Account.__init__(self, name, amount)
            self.name = name
            self.amount = amount

        def show_name(self):
            return self.name

        def show_amount(self):
            return self.amount

    def main():
        print("welcome to payment mode !!")
        bank = input("Enter your bank name : ")
        account_type = input("Enter your account type : ")
        name = input("Enter your name : ")
        amount = int(input("Enter your amount : "))

        Bank = BankAccount(bank, account_type, name, str(amount))

        print("This is the bank : ", Bank.show_bank())
        print("Account type is : ", Bank.show_saving())
        print("Your name is : ", Bank.show_name())
        print("Your amount is : ", Bank.show_amount())

    main()


def inhex():
    class OldManagement:
        def __init__(self, general_manager, marketing_manager):
            self.general_manager = general_manager
            self.marketing_manager = marketing_manager

        def show_general_manager(self):
            return self.general_manager

        def show_marketing_manager(self):
            return self.marketing_manager

    class NewManagement(OldManagement):
        def __init__(self, new_general_manager, new_marketing_manager, financial_manager):

            OldManagement.__init__(self, new_general_manager, new_marketing_manager)
            self.financial_manager = financial_manager

        def show_financial_manager(self):
            return self.financial_manager

    def main():
        print("welcome to our company")
        general_manager = input("Enter the name of a general manager : ")
        marketing_manager = input("Enter the name of a marketing manager: ")
        management1 = OldManagement(general_manager, marketing_manager)
        print()
        new_general_manager = input("Enter the name of a new general manger : ")
        new_marketing_manager = input("Enter the name of a new marketing manager : ")
        financial_manager = input("Enter the name of a new financial manager : ")
        management2 = NewManagement(new_general_manager, new_marketing_manager, financial_manager)
        print()
        print("Here is your new management !!")
        print()

        show(management2)
        print(management2.show_financial_manager(), "is your financial manager")

    def show(mymanagement):
        print(mymanagement.show_general_manager(), "is your new general manager.")
        print(mymanagement.show_marketing_manager(), "is your new marketing manager.")

    main()


def inhex2():
    class Car:
        def __init__(self, company, model, miles):
            self.company = company
            self.model = model
            self.miles = miles

        def show_company(self):
            return self.company

        def show_model(self):
            return self.model

        def show_miles(self):
            return self.miles

    class CCar(Car):
        def __init__(self, price, company, model, miles):
            Car.__init__(self, company, model, miles)
            self.price = price

        def show_price(self):
            return self.price

    def main():
        print("welcome to our website !!")
        print("please upload your car description.")
        company = input("Enter the company of the car : ")
        model = input("Enter the model of the car : ")
        miles = input("Enter the miles of the car")
        print("Here is the information of your car we will display on our site!!")
        my_car1 = Car(company, model, miles)
        show(my_car1)
        price = input("Do you want to add the price of the car ""\n"
                      "y -yes and n - no")
        if price.lower() == "y":
            price = int(input("Enter the price of the car"))
            my_car = CCar(str(format(price, '.,d')), company, model, miles)
            print("the estimated price of the car is :", my_car.show_price())

    def show(my_car):
        print("company :", my_car.show_company())
        print("model :", my_car.show_company())
        print("miles :", my_car.show_miles())

    main()


def polymorphism():
    # polymorphism - which means poly(many) and morphism(types), it means same function name can be used in different types.
    class Dog:
        def show_dog(self):
            print("This is dog.")

    class Cat(Dog):
        def show_dog(self):
            print("This is a cat")

    class Fish(Dog):
        def show_dog(self):
            print("This is a fish")

    my_dog = Dog()
    my_cat = Cat()
    my_fish = Fish()
    my_dog.show_dog()
    my_cat.show_dog()
    my_fish.show_dog()

polymorphism()