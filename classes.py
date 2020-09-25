# TODO classes basic

class MyClass:
    # class variables,
    # use them as 'global' or 'static' fields for the class,(e.g), otherwise just use attributes(instance variables)
    # e.g. keeping track of how many instances of the class there are
    class_var = "this is a class variable"
    num_of_instances = 0

    # a class variable can not be acceses in a function normally, class_var = "something"
    # it has to be accessed either by a class instance or by the class name
    # self.class_var   OR    MyClass.class_var

    # instance1.class_var = "something", it will create the attribute 'class_var' and give it that value
    # MyClass.class_var = "dummy text", it will change the value for ALL the instances

    def __init__(self, var1, var2):  # init = constructor
        # instance variables / attributes
        self.var1 = var1  # self._var1 - protected attribute, self.__var1 - private attribute
        self.var2 = var2
        MyClass.num_of_instances += 1

    # regular method / instance method
    def myfunc(self):  # self is automatically included because that's python
        self.var1 = "dummy text" + self.class_var

    @classmethod  # decorator
    def a_class_method(cls, random_argument):  # call like this : MyClass.a_class_method(args)
        cls.class_var += "add this text"

    @classmethod  # instance1 = MyClass.alternative_constructor(args)
    def alternative_constructor(cls, rand_string):  # in case we receive some data that needs to be processed
        tpl = rand_string.split('-')  # before we create the object,
        return cls(tpl[0], tpl[1])

    @staticmethod  # used when you don't access the instance of the class
    def is_too_large(my_string):  # does not take 'self' or 'cls' as arguments
        if len(my_string) > 13:
            return True
        return False

    # todo getters, setters and deleters

    # GETTER
    @property
    def custom_info(self):  # defining 'custom_info' like it's a method, we can access it like an attribute
        return '{},{}'.format(self.var1, self.var2)  # instance1.custom_info

    # SETTER
    @custom_info.setter
    def custom_info(self, value):
        self.var1, self.var2 = value.split(' ')

    # DELETER
    @custom_info.deleter
    def custom_info(self):
        self.custom_info = None


# TODO  subclasses aka inheritance

# to find out the method resolution order: print(help(class_name))
class Employee:

    def __init__(self, first_name="", last_name="", salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = r'{}.{}@email.com'.format(first_name, last_name)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def apply_raise(self, raise_amount):
        self.salary = int(self.salary * raise_amount)


class Developer(Employee):

    def __init__(self, first_name="", last_name="", salary=0, prog_lang=""):
        super().__init__(first_name, last_name, salary)  # calling the parent constructor
        self.prog_lang = prog_lang  # handling what is left


class Manager(Employee):

    def __init__(self, first_name="", last_name="", salary=0, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):  # you can also add Developer as an employee
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for i, e in enumerate(self.employees):
            print(i, " ", e.full_name())


# TODO basic magic methods

# dir(class_name)  returns the magic methods inherited by a class
class Entity:

    # calling magic methods
    # instance.__magicMethod__()
    # magicMethod(instance)

    def __init__(self, name="", code="", location=""):
        self.name = name
        self.code = code
        self.location = location

    # unambiguous representation of the object
    def __repr__(self):  # meant to be seen by other developers, and used for logging and debugging
        # something that we can use to recreate the object in Python code
        return "Entity('{}', '{}', '{}')".format(self.name, self.code, self.location)
        # instance2 = eval(instance1.__repr__())

    def __str__(self):  # the instance uses __str__ over __repr__, when calling print(instance1), __str__ will be used
        return "{} - {}".format(self.name, self.location)

    def __len__(self):  # "length" of instance, or whatever you want to get when calling len(instance1)
        return len(self.code)


# TODO Operator Overloading + Full Class That does something

class City:

    # constructor                                                         // PIB e pe romana pt ca da
    def __init__(self, city_name="", city_location="", city_population=0, city_pib=0):
        self.__name = city_name
        self.__location = city_location
        self.__population = city_population
        self.__pib = city_pib

    # getters and setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__name = str(value)

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        try:
            self.__population = int(value)
        except ValueError:
            raise Exception("value should be an integer, your value was: {}".format(value))

    @property
    def pib(self):
        return self.__pib

    @pib.setter
    def pib(self, value):
        try:
            self.__pib = int(value)
        except ValueError:
            raise Exception("value should be an integer, your value was: {}".format(value))

    # other magic functions
    def __str__(self):
        return self.name + " " + self.location + " " + str(self.population) + " " + str(self.pib)

    def __repr__(self):
        return "City('{}', '{}', {}, {})".format(self.name, self.location, self.population, self.pib)

    # overloading operators

    def __add__(self, other):  # adds populations
        if isinstance(other, City) is True:
            return City(city_population=self.__population + other.__population, city_pib=self.__pib + other.__pib)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, City) is True:
            return City(city_population=self.__population - other.__population, city_pib=self.__pib - other.__pib)
        return NotImplemented

# TODO classes tricks, and important observations

'''
mg = Manager()
isinstance(mg, Employee'# or Manager') - true 
issubclass(Manager, Developer) - false'''  # isinstance(), verifies if an object is an instance of the class

'''
 def myfunc( other_items,*args, **kwargs)
 # *args takes an arbitrary number of arguments 
 # **kwargs takes an arbitrary number of keyword arguments
 // you don't have to call them args and kwargs, * and ** do the 'magic'
'''
