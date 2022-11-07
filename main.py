import person

# defining the main function
def main():
    # Creating the Person class object
    person1 = person.Person()

    # Using the setters method to set the attributes for the Person Class
    person1.set_name("James Polkuu")
    person1.set_address("Fiapre Street 22")
    person1.set_telephone("0550877222")

   # Creating the Person class object
    customer1 = person.Customer()
    # Using the setters method to set the attributes for the Customer Class
    customer1.set_name("James Polkuu")
    customer1.set_address("Fiapre Street 22")
    customer1.set_telephone("0550877222")
    customer1.set_mailing_list(False)
    customer1.set_customer_number('11223A')

    # Displaying the person class using the getters/accessors methods 
    print(f'\nName: {person1.get_name()}')
    print(f'Address: {person1.get_address()}') 
    print(f'Telephone: {person1.get_telephone()}')

    # Displaying the Customer class using the getters/accessors methods 
    print(f'\nName: {customer1.get_name()}')
    print(f'Address: {customer1.get_address()}')
    print(f'Telephone: {customer1.get_telephone()}')
    print(f'Put on Mailing List?: {customer1.get_mailing_list()}')
    print(f'Customer Number: {customer1.get_customer_number()}\n')

# Calling the main method
main()