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
        self.var1 = var1
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
        tpl = rand_string.split('-')                # before we create the object,
        return cls(tpl[0], tpl[1])

    @staticmethod  # used when you dont access the instance on the class
    def is_too_large(my_string):  # does not take 'self' or 'cls' as arguments
        if len(my_string) > 13:
            return True
        return False


# TODO  subclasses aka inheritance

# to find out the method resolution order: print(help(class_name))
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = r'{}.{}@email.com'.format(first_name, last_name)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def apply_raise(self, raise_amount):
        self.salary = int(self.salary * raise_amount)


class Developer(Employee):

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)  # calling the parent constructor
        self.prog_lang = prog_lang  # handling what is left


class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for index, e in enumerate(self.employees):
            print(index, " ", e.full_name())
