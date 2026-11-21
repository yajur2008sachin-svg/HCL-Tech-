import numpy as np
import pandas as pd
from file_ops import file_name

def show_report():
    df = pd.read_csv(file_name)
    df["Amount"] = df["Amount"].fillna(df["Amount"].mean())

    print("\n--- PANDAS DATAFRAME (FIRST 5 ROWS) ---")
    print(df[["ID", "Category", "Amount"]].head(5))

    arr_1d = np.array(df["Amount"])
    first_three = arr_1d[:3]
    a, b, c = first_three
    arr_2d = np.array([[1, a], [2, b], [3, c]])

    print("\n--- NUMPY ANALYSIS ---")
    print("First 3 Amounts (Slicing):", first_three)
    print("Last Amount (Indexing):", arr_1d[-1])
    print("2D Array Sample:\n", arr_2d)
    print("Sum:", round(np.sum(arr_1d), 2))
    print("Mean:", round(np.mean(arr_1d), 2))
    print("Max:", np.max(arr_1d))
    print("Min:", np.min(arr_1d))
    print("Standard Deviation:", round(np.std(arr_1d), 2))

    print("\n--- CATEGORY WISE TOTAL (GROUPBY) ---")
    print(df.groupby("Category")["Amount"].sum())

    print("\n--- EXPENSES ABOVE 500 (FILTER & SORT) ---")
    high = df[df["Amount"] > 500].sort_values(by="Amount", ascending=False)
    print(high[["ID", "Category", "Amount"]].head(5))
