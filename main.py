import file_ops
import report

def show_all():
    data = file_ops.read_all()
    print("\nID | Date | Category | Amount | Mode")
    for row in data:
        print(row["ID"], "|", row["Date"], "|", row["Category"], "|", row["Amount"], "|", row["Mode"])

def add_item():
    data = file_ops.read_all()
    new_id = str(len(data) + 1)
    dt = input("Enter Date (YYYY-MM-DD): ")
    print("Categories:", file_ops.categories)
    cat = input("Enter Category: ")
    amt = input("Enter Amount: ")
    print("Modes:", file_ops.modes)
    mode = input("Enter Mode: ")
    record = {"ID": new_id, "Date": dt, "Category": cat, "Amount": amt, "Mode": mode}
    data.append(record)
    file_ops.save_all(data)
    print("Expense Added!")

def search_item():
    data = file_ops.read_all()
    key = input("Enter ID or Category to search: ")
    for row in data:
        if row["ID"] == key or row["Category"].lower() == key.lower():
            print(row)

def update_item():
    data = file_ops.read_all()
    uid = input("Enter ID to update: ")
    new_amt = input("Enter new Amount: ")
    for row in data:
        if row["ID"] == uid:
            row["Amount"] = new_amt
    file_ops.save_all(data)
    print("Updated!")

def delete_item():
    data = file_ops.read_all()
    did = input("Enter ID to delete: ")
    for i in range(len(data)):
        if data[i]["ID"] == did:
            data.pop(i)
            break
    file_ops.save_all(data)
    print("Deleted!")

file_ops.create_dataset()

while True:
    print("\n1.Show All  2.Add  3.Search  4.Update  5.Delete  6.Report  7.Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        show_all()
    elif ch == "2":
        add_item()
    elif ch == "3":
        search_item()
    elif ch == "4":
        update_item()
    elif ch == "5":
        delete_item()
    elif ch == "6":
        report.show_report()
    elif ch == "7":
        print("Bye!")
        break
    else:
        print("Wrong choice")
