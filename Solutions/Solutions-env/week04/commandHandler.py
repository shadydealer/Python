from category import Category
from category import Income
from category import Expense
import sys
import re

class MoneyTracker():
    
    def __extract_date(self, line):
        match = re.search("\\d+-\\d+-\\d+", line)
        if match:
            return match.group(0)
        else:
            raise ValueError(f'Line containing the date is not in the correct format. Line:\n{line}\n')
    
    def __add_transaction(self, amount, transactionType, category):
        if category == "New Income":
            return Income(category, amount)
        elif category == "New Expense":
            return Expense(category, amount)
        else:
            raise ValueError("Transaction category must be:\n"
                             "New Income\n"
                             "New Expense\n")

    def __extract_transaction(self, line):
        amount, transactionType, category = line.strip().split(', ')
        
        try:
            amount = float(amount)
        except TypeError as te:
            raise TypeError(f'"Amount" must be of type {type(float)}\n')

        if amount < 0:
            raise ValueError("\"Amount\" must be non-negative integer\n")
        if type(transactionType) is not str:
            raise TypeError(f'"Transaction type" must be of type {type(str)}\n')
        if type(category) is not str:
            raise TypeError(f'"Category" must be of type {type(str)}\n')
        
        return self.__add_transaction(amount,  transactionType, category)
    
    def __parse_txt(self, fileName):
        
        transactions = {}
        try:
            with open(fileName) as file:
                date = ""
                for line in file:
                    if line.startswith("==="):
                        date = self.__extract_date(line)
                        transactions.update({date: []})
                    else:
                        transaction = self.__extract_transaction(line)
                        transactions[date].append(transaction)
        except IOError:
            pass
        else:
            return transactions

    def __init__(self, clientName):
        
        if type(clientName) is not str:
            raise TypeError(f'ClientName must be of type {type(str)}\n')
        self.__clientName = clientName
        fileName = f'{clientName}.txt'
        self.__transactions = self.__parse_txt(fileName)

    def add_expense(self, amount, category, date):
        pass
    def __str__(self):
        return str(self.__transactions)
    def __repr__(self):
        return str(self)