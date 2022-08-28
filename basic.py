# Python Basic Exercise for Beginners
# from https://pynative.com/python-basic-exercise-for-beginners/

class Exercises:
    """Exercises"""

    def multiply_or_sum(self, a: int, b: int) -> int:
        """1"""
        if (a*b) <= 1000:
            return a*b
        else:
            return a+b

    def print_sum(self, number: int) -> str:
        """2"""
        print("Printing current and previous number sum in a range(", number, ")")
        for x in range(number):
            print("Current Number ", x, "Previous Number  ",
                  x-1, "  Sum:  ", x + (x-1))

    def print_even_char(self, string: str) -> str:
        """3"""
        print("Orginal String is  ", str)
        print("Printing only even index chars")
        for char in string:
            if (string.find(char) % 2) == 0:
                print(char)

    def remove_char(self, str: str, index: int) -> str:
        """4"""
        return print(str[index:])

    def first_last_same(self, numbers_x: list) -> bool:
        """5"""
        if numbers_x[0] == numbers_x[-1]:
            return print(True)
        else:
            return print(False)

    def divisible_by_5(self, number_list: list) -> bool:
        """6"""
        print("Given list is ", number_list)
        print("Divisible by 5")
        for number in number_list:
            if number % 5 == 0:
                print(number)


#execute.multiply_or_sum(40, 30)
# execute.print_sum(10)
# execute.print_even_char("pynative")
#execute.remove_char("pynative", 2)
#execute.first_last_same([10, 20, 32, 40, 11])
#execute.divisible_by_5([10, 20, 32, 40, 11])
