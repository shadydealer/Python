import sys
import re
from enum import Enum
from collections import defaultdict

class Transaction(Enum):
    new_expense = 0
    new_income = 1

money_tracker_file_name = "money_tracker_file.txt"
data = {}


def list_commands():
    print("Choose one of the following options to continue")
    print("1 - show all data")
    print("2 - show data for specific date")
    print("3 - show expenses, ordered by categories")
    print("4 - add new income")
    print("5 - add new expense")
    print("6 - exit")

def show_all_data():
    for key in data:
        print("=== {} ===".format(key))
        for transaction in data[key]:
            print("{0}, {1}, {2}".format(str(transaction[0]), str(transaction[1]), str(transaction[2])))


def extract_date(string):
    match = re.search("\\d+-\\d+-\\d+", string)
    if match:
        string_date = match.group(0)
        return string_date
    else:
        raise ValueError("Incorrect line format: {}".format(string))

def extract_transaction_info(string):
    money, description ,transaction_type = string.split(', ')

    if transaction_type == "New Expense":
        transaction_type = Transaction.new_expense
    elif transaction_type == "New Income":
        transaction_type = Transaction.new_income
    return (money,description,transaction_type)

def extract_data(file_name):
    try:
        money_tracker_file = open(file_name, 'r')
        
        date = 0
        
        for line in money_tracker_file:

            if line.startswith("==="):
                date = extract_date(line)
            else:
                transaction_info = extract_transaction_info(line)
            data[date].append(transaction_info)

        money_tracker_file.close()

        return True
    except OSError:
        return False
    except ValueError as ve:
        print(ve.message)

def add_income(income_type, money, date_string):
    date = extract_date(date_string)
    info = (money, income_type, Transaction.new_income)
    
    if date in data:
        data[date].append(info)
    else:
        data[date] = [(info)]

def add_expense(income_type, money, date_string):
    date = extract_date(date_string)
    info = (money, income_type, Transaction.new_expense)
    if date in data:
        data[date].append(info)
    else:
        data[date] = (info)

def main():
    command = 0
    amount = 0
    date = ""

    while command != 6:
        try:
            list_commands()
            try:
                command = int(input())
                if command > 6:
                    raise ValueError
            except ValueError:
                raise ValueError("Invalid command.")

            try:
                if command == 1:
                    show_all_data()
                if command == 4:
                    print("New income amount:")
                    amount = int(input())
                    print("New income type:")
                    income_type = input()
                    print("New income date:")
                    date = input()
                    add_income(income_type, amount, date)
                    print(data)
                if command == 5:
                    print("New income amount:")
                    amount = int(input())
                    print("New income type:")
                    income_type = input()
                    print("New income date:")
                    date = input()
                    add_expense(income_type, amount,date)

            except ValueError:
                raise ValueError("Invalid amount.")

        except ValueError as ve:
            print(ve.message)

if __name__ == "__main__":
    main()