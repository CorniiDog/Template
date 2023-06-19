from toolbox import database

# Create test class
class Test:
    """
    Notes
    -----
    This is a test class, it is used to test the documentation generator

    References
    ----------
    No Links

    Examples
    --------
    test_contact = Test.Test_Contact("123-456-7890", 1234)
    test_object = Test("Bill", 20, test_contact)
    print(test_object)
    """
    class Test_Contact:
        """
        Notes
        -----
        This is a test class, it is used to test the documentation generator

        References
        ----------
        No Links

        Examples
        --------
        test_contact = Test.Test_Contact("123-456-7890", 1234)
        print(test_contact)
        """

        def __init__(self, phone: str, address: int):
            """
            Parameters
            ----------
            phone : str
                The phone number of the person to greet
            address : int
                The address of the person to greet
            Returns
            -------
            None
                This function does not return anything

            Notes
            -----
            This function is called when the object is created

            References
            ----------
            No Links

            Examples
            --------
            address_object = Test.Test_Contact("123-456-7890", 1234)
            """
            self.phone = phone
            self.address = address
        def __str__(self):
            """
            Parameters
            ----------
            None

            Returns
            -------
            str
                This function returns a string representation of the object

            Notes
            -----
            This function is called when the object is printed

            References
            ----------
            No Links

            Examples
            --------
            address_object = Test.Test_Contact("123-456-7890", 1234)
            print(address_object)
            """
            return f"Phone: {self.phone}, Address: {self.address}"


    def __init__(self, name: str, age: int, contact: Test_Contact):
        """
        Parameters
        ----------
        name : str
            The name of the person to greet
        age : int
            The age of the person to greet
        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        This function is called when the object is created

        References
        ----------
        No Links

        Examples
        --------
        test_object = Test("Bill", 20)
        """
        self.name = name
        self.age = age
        self.contact = contact

    def __str__(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        str
            This function returns a string representation of the object

        Notes
        -----
        This function is called when the object is printed

        References
        ----------
        No Links

        Examples
        --------
        test_object = Test("Bill", 20)
        print(test_object)
        """
        return f"Name: {self.name}, Age: {self.age}" + "\n" + str(self.contact)


def print_hi(name: str) -> None:
    """
        Parameters
        ----------
        name : str
            The name of the person to greet

        Returns
        -------
        None
            This function does not return anything

        Notes
        --------
        ello

        References
        ------------
        https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html

        Examples
        --------
        print_hi('PyCharm')

        """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}
    database.save('spreadsheet_people', spreadsheet_data)
    print(spreadsheet_data)

    database.save_key('test', 'ello', override=True)
    print(database.load_key('test'))

    test_object = Test("Bill", 20, Test.Test_Contact("123-456-7890", 1234))
    print(test_object)

    test_contact = Test.Test_Contact("123-456-7890", 1234)
    print(test_contact)

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
