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

    def count_substring(self, phrase: str, substring: str) -> int:
        """7"""
        count = 0

        for word in phrase.split():
            if word == substring:
                count += 1
        return count

    def check_palindrome(self, number: int) -> bool:
        """9"""
        original_num = number
        reverse_num = 0
        while number > 0:
            reminder = number % 10
            reverse_num = (reverse_num * 10) + reminder
            number = number // 10

        if original_num == reverse_num:
            return True
        else:
            return False

    def mix_two_lists(self, list1: list, list2: list) -> list:
        """10"""
        list1_odd = []
        list2_even = []

        for number in list1:
            if number % 2 == 1:
                list1_odd.append(number)

        for number in list2:
            if number % 2 == 0:
                list2_even.append(number)

        return list1_odd + list2_even

    def extract_digit_reverse(self, number: int) -> str:
        """11"""
        reverse_num_str = ""
        reverse_num = 0
        while number > 0:
            reminder = number % 10
            reverse_num = reminder
            reverse_num_str += str(reverse_num) + " "
            number = number // 10

        return reverse_num_str.strip()
