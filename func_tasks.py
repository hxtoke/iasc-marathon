def hello_world ():
    print("Hello, World!")

def greet(Денис):
    print(f"Привіт, {Денис}!")
 
def square(n):
    return n * n

def add(a, b):
    return a + b

def great(name="Денис"):
    print(f"Привіт, {name}!")

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def is_even(n):
    return n % 2 == 0

def print_numbers(n):
    for i in range(1, n + 1):
     print(i)

def find_name(name, name_list):
    return name in name_list

def max_of_three(a, b, c):
    return max(a, b, c) 

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def print_user_info(**info):
    print_user_info(name="Денис", age=17)

def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()

