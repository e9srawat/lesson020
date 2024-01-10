"""Lesson 020"""
import csv
import os
import datetime
import random


class AccountManager:
    """Account Manager Class"""

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance
        self.path = self.owner + "/"

    def get_balance(self, file):
        """retrieves balance from ledger or sets it to 100000 if no ledger"""
        if os.path.isfile(file):
            with open(file, "r", encoding="utf-8") as file_:
                csvreader = csv.DictReader(file_)
                data = list(csvreader)
            return data[-1]["balance"]

        return self.balance

    def cred(self, amount):
        """Credits amount to balance"""
        balance = self.get_balance(self.path + "ledger.csv")
        balance = int(balance) + amount
        return balance

    def debit(self, amount):
        """Debits amount from balance"""
        balance = self.get_balance(self.path + "ledger.csv")
        balance = int(balance) - amount
        return balance

    def transaction(self, credit=False, **kwargs):
        """Performs a transaction"""
        if credit:
            balance = self.cred(kwargs["amount"])
        else:
            balance = self.debit(kwargs["amount"])
        kwargs["balance"] = balance
        self.ledger(kwargs, credit)
        self.category_(kwargs, credit)
        self.payment(kwargs, credit)
        self.print_report()
        return balance

    def ledger(self, trans: dict, credit):
        """Store transaction data in ledger.csv file"""
        os.makedirs(self.path, exist_ok=True)
        if credit:
            cr = "+"
        else:
            cr = "-"
        data = {
            "date": trans["date"],
            "category": trans["category"],
            "desc": trans["desc"],
            "amount": f"{cr}{trans['amount']}",
            "balance": trans["balance"],
            "mode_of_payment": trans["mode_of_payment"],
        }

        file_exists = os.path.isfile(self.path + "ledger.csv")

        with open(
            self.path + "ledger.csv", "a", encoding="utf-8", newline=""
        ) as ledger_file:
            csvwriter = csv.DictWriter(ledger_file, fieldnames=data.keys())

            if not file_exists:
                csvwriter.writeheader()  # Write header only if the file is empty

            csvwriter.writerow(data)

    def category_(self, trans: dict, credit):
        """Store transaction data in csv file wrt category"""
        if credit:
            cr = "+"
        else:
            cr = "-"
        data = {
            "date": trans["date"],
            "category": trans["category"],
            "desc": trans["desc"],
            "amount": f"{cr}{trans['amount']}",
        }
        file_exists = os.path.isfile(self.path + "category" + ".csv")

        with open(
            self.path + "category" + ".csv", "a", encoding="utf-8", newline=""
        ) as cate:
            csvwriter = csv.DictWriter(cate, fieldnames=data.keys())

            if not file_exists:
                csvwriter.writeheader()  # Write header only if the file is empty

            csvwriter.writerow(data)

    def payment(self, trans: dict, credit):
        """Store transaction data in csv file wrt mode_of_payment"""
        if credit:
            cr = "+"
        else:
            cr = "-"
        data = {
            "date": trans["date"],
            "mode_of_payment": trans["mode_of_payment"],
            "amount": f"{cr}{trans['amount']}",
            "desc": trans["desc"],
        }
        file_exists = os.path.isfile(self.path + "mode_of_payment" + ".csv")

        with open(
            self.path + "mode_of_payment" + ".csv", "a", encoding="utf-8", newline=""
        ) as moolah:
            csvwriter = csv.DictWriter(moolah, fieldnames=data.keys())

            if not file_exists:
                csvwriter.writeheader()  # Write header only if the file is empty

            csvwriter.writerow(data)

    def print_report(self):
        """creates a report and prints it in passbook format"""
        with open(self.path + "category.csv", "r", encoding="utf-8") as file1:
            glasses = csv.DictReader(file1)
            data = list(glasses)
        for i in data:
            i["date"] = i["date"][:-3]
        lst = sorted(set(i["date"] for i in data))
        categ = sorted(set(i["category"] for i in data))
        string = ""
        string += f"{'category':18}" + "".join(f"{i:18}" for i in lst)
        string += "\n"

        def dictionator(category):
            dicn = {category: {}}
            for i in data:
                if category in i.values():
                    if i["date"] not in dicn[category]:
                        dicn[category].update({i["date"]: int(i["amount"])})
                    else:
                        dicn[category][i["date"]] += int(i["amount"])
            return dicn

        for i in categ:
            string += f"{i:18}"
            dicn = dictionator(i)
            for j in lst:
                if j in dicn[i]:
                    string += f"{str(dicn[i][j]):18}"
                else:
                    string += f"{'-':18}"
            string += "\n"
        print(string)
        self.store_report(string)

    def store_report(self, string):
        """stores the report in a text file"""
        with open(self.path + "report.txt", "w", encoding="utf-8") as output:
            output.write(string)

    def random_data(self):
        """gets 10 random datas and performs transactions with those datas"""
        categ = {
            "Credit": [10000, "Bonus", "UPI_Transfer", "Donation"],
            "Food": [
                300,
                "Shwarma",
                "Pizza",
                "Pasta",
                "Burger",
                "Noodles",
                "Sushi",
                "Waffles",
            ],
            "Travel": [900, "Bus", "Train", "Rickshaw", "Taxi"],
            "Entertainment": [600, "Movie", "Turf", "Bowling", "Swimming"],
            "Daily": [1000, "Petrol", "Groceries", "Munchies"],
        }
        pay = ["UPI", "Card", "Bank_Transfer"]

        for _ in range(10):
            year = random.choice(range(2018, 2024))
            month = random.choice(range(1, 13))
            day = random.choice(range(1, 29))
            input_d = datetime.date(year, month, day)
            category = random.choice(list(categ.keys())[1:])
            credit = category == "Credit"
            desc = random.choice(categ[category][1:])
            amount = random.choice(range(categ[category][0]))
            mode_of_payment = random.choice(pay)
            self.transaction(
                credit,
                date=input_d,
                amount=amount,
                category=category,
                desc=desc,
                mode_of_payment=mode_of_payment,
            )
