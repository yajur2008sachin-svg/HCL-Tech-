import csv
import random

modes = ("UPI", "Cash", "Card")
categories = {"Food", "Travel", "Bills", "Shopping", "Study"}
file_name = "expenses.csv"

def create_dataset():
    f = open(file_name, "w", newline="")
    w = csv.writer(f)
    w.writerow(["ID", "Date", "Category", "Amount", "Mode"])
    cat_list = list(categories)
    for i in range(1, 56):
        c = random.choice(cat_list)
        m = random.choice(modes)
        amt = random.randint(50, 1000)
        if i == 5 or i == 25:
            amt = ""
        w.writerow([i, "2026-11-20", c, amt, m])
    f.close()

def read_all():
    f = open(file_name, "r")
    r = csv.DictReader(f)
    data = list(r)
    f.close()
    return data

def save_all(data):
    f = open(file_name, "w", newline="")
    w = csv.DictWriter(f, fieldnames=["ID", "Date", "Category", "Amount", "Mode"])
    w.writeheader()
    w.writerows(data)
    f.close()
