"""Lesson 020"""
import csv
import os
import datetime
import random


def get_balance(file):
    """retrieves balance from ledger or sets it to 100000 if no ledger"""
    if os.path.isfile(file):
        with open(file, "r", encoding="utf-8") as file_:
            csvreader = csv.DictReader(file_)
            data = list(csvreader)
        return data[-1]["balance"]

    return 100000


def cred(amount):
    """Credits amount to balance"""
    balance = get_balance("ledger.csv")
    balance = int(balance) + amount
    return balance


def debit(amount):
    """Debits amount from balance"""
    balance = get_balance("ledger.csv")
    balance = int(balance) - amount
    return balance


def transaction(credit=False, **kwargs):
    """Performs a transaction"""
    if credit:
        balance = cred(kwargs["amount"])
    else:
        balance = debit(kwargs["amount"])
    kwargs["balance"] = balance
    ledger(kwargs, credit)
    category_(kwargs, credit)
    payment(kwargs, credit)
    print_report()
    return balance


def ledger(trans: dict, credit):
    """Store transaction data in ledger.csv file"""
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

    file_exists = os.path.isfile("ledger.csv")

    with open("ledger.csv", "a", encoding="utf-8", newline="") as ledger_file:
        csvwriter = csv.DictWriter(ledger_file, fieldnames=data.keys())

        if not file_exists:
            csvwriter.writeheader()  # Write header only if the file is empty

        csvwriter.writerow(data)


def category_(trans: dict, credit):
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
        "mode_of_payment": trans["mode_of_payment"],
    }
    file_exists = os.path.isfile(trans["category"] + ".csv")

    with open(trans["category"] + ".csv", "a", encoding="utf-8", newline="") as cate:
        csvwriter = csv.DictWriter(cate, fieldnames=data.keys())

        if not file_exists:
            csvwriter.writeheader()  # Write header only if the file is empty

        csvwriter.writerow(data)


def payment(trans: dict, credit):
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
    file_exists = os.path.isfile(trans["mode_of_payment"] + ".csv")

    with open(
        trans["mode_of_payment"] + ".csv", "a", encoding="utf-8", newline=""
    ) as moolah:
        csvwriter = csv.DictWriter(moolah, fieldnames=data.keys())

        if not file_exists:
            csvwriter.writeheader()  # Write header only if the file is empty

        csvwriter.writerow(data)


def print_report():
    """creates a report and prints it in passbook format"""
    categ = ["Credit", "Food", "Travel", "Entertainment", "Daily"]
    with open("ledger.csv", "r", encoding="utf-8") as file1:
        glasses = csv.DictReader(file1)
        data = list(glasses)
    lst = sorted([i["date"] for i in data])
    lst.insert(0, "category")
    string = ""
    string += "".join(f"{i:18}" for i in lst)
    string += "\n"

    for i in categ:
        if os.path.isfile(i + ".csv"):
            string += f"{i:18}"
            with open(i + ".csv", "r", encoding="utf-8") as file2:
                glasses = csv.reader(file2)
                data = list(glasses)
                flat_data = [j for i in data[1:] for j in i]
                for j in lst[1:]:
                    if j in flat_data:
                        string += f"{flat_data[flat_data.index(j)+3]:18}"
                    else:
                        string += f"{'-':18}"
                string += "\n"
    print(string)
    store_report(string)


def store_report(string):
    """stores the report in a text file"""
    with open("report.txt", "w", encoding="utf-8") as output:
        output.write(string)


def random_data():
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
    years = [2018, 2019, 2020, 2021, 2022, 2023]

    for _ in range(10):
        year = random.choice(years)
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        input_d = datetime.date(year, month, day)
        credit = random.choice((True, False))
        print(credit)
        if credit:
            category = list(categ.keys())[0]
        else:
            category = random.choice(list(categ.keys())[1:])
        desc = random.choice(categ[category][1:])
        amount = random.choice(range(categ[category][0]))
        mode_of_payment = random.choice(pay)
        transaction(
            credit,
            date=input_d,
            amount=amount,
            category=category,
            desc=desc,
            mode_of_payment=mode_of_payment,
        )


if __name__ == "__main__":
    random_data()
    print_report()
