class Person:

    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__tel_number = ''


    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__tel_number = telephone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__tel_number


class Customer(Person):

    def __init__(self):
        Person.__init__(self)
        self.__customer_number = ""
        self.__mailing_list = True

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list

    def mailing_list(self):
        if self.mailing_list:
            print('True')
        else:
            print('False')

    



        