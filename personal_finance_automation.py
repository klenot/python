import csv
import gspread

MONTH = "july"
file = f"personal_finance_import/cs_{MONTH}.csv"

transactions = []

subsNames = {"APPLE.COM/BILL 800700527 IE", "Fakturoid", "Vodafone Czech Republic a.s.", "ADOBE PHOTOGPHY PLAN Dublin IE", }

# This code is for opening the csv files.
with open(file, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        date = row[0]
        name = row[1]
        amount = float(row[2].replace("\xa0", "").replace(",", "."))
        typeOfPayment = row[3]
        category = "other"

        if row[1] == "":
            name = "NO NAME"
        if name in subsNames:
            category = "SUBSCRIPTION"
        if name == "NO NAME" and amount == 0.0:
            category = "DELETE"

        transaction = [name, date, amount, typeOfPayment, category]
        # print(transaction)
        transactions.append(transaction)

    # transactions.pop(0)
    print(transactions)

    for transaction in transactions:
        print(transaction)


# This code connects google sheets file.
sa = gspread.service_account(filename="/Users/mara/OneDrive/Github/python/venv/lib/python3.10/site-packages/gspread/service_account.json")
sh = sa.open("Personal Finance Project")
