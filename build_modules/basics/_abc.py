from abc import ABC, abstractmethod
"abc - abstract base class which has mainly abstract class, abstract method"\
"abstract class - which has abstract methods."\
"abstract method - which has the declaration."


class Main(ABC):
    @abstractmethod # if we use @abstractmethod - we have to declare total classes in the abstract classes
    def laptop(self):
        print("ab")

    def desktop(self):
        pass


class Demo(Main):
    def laptop(self):
        print("It's working..")

    def desktop(self):
        print("it's not working..")


obj = Demo()

obj.laptop()
