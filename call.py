from lesson020 import AccountManager
import datetime


account1 = AccountManager(1234563,"Bruce",10000)
account2 = AccountManager(1234563,"Tim",20000)
account3 = AccountManager(1234563,"Jason",10000)
account4 = AccountManager(1234563,"Ivy",20000)
account5 = AccountManager(1234563,"Talia",10000)
account6 = AccountManager(1234563,"Harley",20000)
# account2.random_data()
# account1.random_data()
# account3.random_data()
# account4.random_data()
# account5.random_data()
# account6.random_data()
account2.transaction(False,date=datetime.date(2018,1,12),
                amount=100,
                category="Food",
                desc="pizza",
                mode_of_payment="UPI", )
account2.transaction(False,date=datetime.date(2020,3,12),
                amount=200,
                category="Travel",
                desc="Bus",
                mode_of_payment="UPI", )
account2.transaction(False,date=datetime.date(2019,2,5),
                amount=300,
                category="Food",
                desc="pizza",
                mode_of_payment="UPI", )
account2.transaction(False,date=datetime.date(2019,5,2),
                amount=400,
                category="Enterntainment",
                desc="movie",
                mode_of_payment="UPI", )
account2.transaction(False,date=datetime.date(2020,3,11),
                amount=90,
                category="Travel",
                desc="bus",
                mode_of_payment="UPI", )
# account2.transaction(False,date=datetime.date(2019,4,12),
#                 amount=400,
#                 category="Travel",
#                 desc="Bus",
#                 mode_of_payment="UPI", )
# account2.transaction(True,date=datetime.date(2019,5,21),
#                 amount=9000,
#                 category="Credit",
#                 desc="Bonus",
#                 mode_of_payment="UPI", )
# account2.transaction(False,date=datetime.date(2019,7,1),
#                 amount=100,
#                 category="Food",
#                 desc="pasta",
#                 mode_of_payment="UPI", )
# account2.transaction(False,date=datetime.date(2020,1,2),
#                 amount=3455,
#                 category="Groceries",
#                 desc="Balls",
#                 mode_of_payment="UPI", )
# account2.transaction(False,date=datetime.date(2020,3,14),
#                 amount=100,
#                 category="Travel",
#                 desc="Bus",
#                 mode_of_payment="UPI", )
#account2.print_report()