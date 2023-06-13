from toolbox import database

# Create test class
class Test:
    def __init__(self, name: str, age: int):
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
        return f"Name: {self.name}, Age: {self.age}"


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

    test_object = Test("Bill", 20)
    print(test_object)

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
