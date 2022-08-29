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
        result_list = []
        print("Printing current and previous number sum in a range(", number, ")")
        for x in range(number):
            print("Current Number ", x, "Previous Number  ",
                  x-1, "  Sum:  ", x + (x-1))
            result_list.append([x, x-1, x+(x-1)])
        return result_list

    def print_even_char(self, string: str) -> list:
        """3"""
        result_string = ""
        print("Orginal String is  ", str)
        print("Printing only even index chars")
        for char in string:
            if (string.find(char) % 2) == 0:
                result_string += char

        return result_string

    def remove_char(self, str: str, index: int) -> str:
        """4"""
        return str[index:]

    def first_last_same(self, numbers_x: list) -> bool:
        """5"""
        if numbers_x[0] == numbers_x[-1]:
            return True
        else:
            return False

    def divisible_by_5(self, number_list: list) -> list:
        """6"""
        result_list = []
        print("Given list is ", number_list)
        print("Divisible by 5")
        for number in number_list:
            if number % 5 == 0:
                result_list.append(number)

        return result_list

# execute.multiply_or_sum(40, 30)
# execute.print_sum(10)
# execute.print_even_char("pynative")
# execute.remove_char("pynative", 2)
# execute.first_last_same([10, 20, 32, 40, 11])
# execute.divisible_by_5([10, 20, 32, 40, 11])
