"""
This is a git tools demo
"""

def print_even_numbers(stop):
    """
    This function prints even numbers to the "stop" param
    :param stop:
    :return:
    """
    for number in range(stop):
        if number%2==0:
            print(number)
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('PyCharm')
    print_even_numbers(101)
