"""
Simple Stock Portfolio Tracker
==============================
Calculates the total value of a stock portfolio using a hardcoded price list.

The user enters stock symbols and quantities. The program looks up each price
in a dictionary, multiplies price by quantity, adds everything up, prints a
summary table, and can save the result as a .txt report and a .csv file.

Concepts used: dictionaries, input/output, basic arithmetic, file handling.

Author: Bhavesh Tayade
"""

import csv
import os
from datetime import datetime

# ---------------------------------------------------------------------------
# 1. HARDCODED STOCK PRICES  (symbol -> price per share)
#    Edit this dictionary to add stocks or update prices.
# ---------------------------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180.00,    # Apple
    "TSLA": 250.00,    # Tesla
    "MSFT": 420.00,    # Microsoft
    "GOOGL": 165.00,   # Alphabet
    "AMZN": 185.00,    # Amazon
    "NVDA": 120.00,    # NVIDIA
    "INFY": 1650.00,   # Infosys
    "TCS": 3900.00,    # Tata Consultancy Services
}

CURRENCY = "$"          # change to "Rs." if you switch to Indian stock prices
OUTPUT_FOLDER = "."     # "." means the folder the script is run from
WIDTH = 52              # width of the printed table, used for the dividers


def show_available_stocks():
    """Print every stock in the price dictionary."""
    print("\nAvailable stocks")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<7}{CURRENCY}{price:>10,.2f}")
    print("-" * 30)


def ask_quantity(symbol):
    """Keep asking until the user types a whole number greater than 0."""
    while True:
        raw = input(f"  Quantity of {symbol}: ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("  ! Please enter a whole number greater than 0.")


def collect_holdings():
    """
    Ask the user for stock symbols and quantities.

    Returns a dictionary of holdings, for example {"AAPL": 10, "TSLA": 4}.
    An empty line finishes the input.
    """
    holdings = {}
    print("\nEnter your holdings. Press Enter on an empty line when finished.")
    print("Type LIST at any time to see the available stocks again.")

    while True:
        symbol = input("\n  Stock symbol: ").strip().upper()

        if symbol == "":
            if holdings:
                break                      # at least one stock entered, stop
            print("  ! You have not entered any stock yet.")
            continue

        if symbol == "LIST":
            show_available_stocks()
            continue

        if symbol not in STOCK_PRICES:
            print(f"  ! '{symbol}' is not in the price list. Type LIST to see options.")
            continue

        quantity = ask_quantity(symbol)
        # If the same stock is entered twice, add the quantities together.
        holdings[symbol] = holdings.get(symbol, 0) + quantity
        print(f"  + {quantity} x {symbol} recorded.")

    return holdings


def build_rows(holdings):
    """
    Convert holdings into table rows and calculate the grand total.

    Each row is [symbol, quantity, price, value] where value = price * quantity.
    Returns (rows, total).
    """
    rows = []
    total = 0.0

    for symbol, quantity in holdings.items():
        price = STOCK_PRICES[symbol]
        value = quantity * price           # <- the core arithmetic
        total = total + value
        rows.append([symbol, quantity, price, value])

    rows.sort(key=lambda row: row[3], reverse=True)   # biggest holding first
    return rows, total


def money(amount):
    """Format a number as currency, e.g. 1800.0 -> '$1,800.00'."""
    return f"{CURRENCY}{amount:,.2f}"


def print_report(rows, total):
    """Print the portfolio summary table on the screen."""
    print("\n" + "=" * WIDTH)
    print("PORTFOLIO SUMMARY".center(WIDTH))
    print("=" * WIDTH)
    print(f"{'STOCK':<8}{'QTY':>5}{'PRICE':>13}{'VALUE':>16}{'SHARE':>10}")
    print("-" * WIDTH)

    for symbol, quantity, price, value in rows:
        share = (value / total) * 100      # this stock's % of the portfolio
        print(f"{symbol:<8}{quantity:>5}{money(price):>13}"
              f"{money(value):>16}{share:>9.1f}%")

    print("-" * WIDTH)
    print(f"{'TOTAL INVESTMENT':<26}{money(total):>26}")
    print("=" * WIDTH)


def save_txt(rows, total, path):
    """Write a readable report to a .txt file."""
    stamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    with open(path, "w", encoding="utf-8") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write(f"Generated on: {stamp}\n")
        f.write("=" * WIDTH + "\n")
        f.write(f"{'STOCK':<8}{'QTY':>5}{'PRICE':>13}{'VALUE':>16}\n")
        f.write("-" * WIDTH + "\n")

        for symbol, quantity, price, value in rows:
            f.write(f"{symbol:<8}{quantity:>5}{money(price):>13}"
                    f"{money(value):>16}\n")

        f.write("-" * WIDTH + "\n")
        f.write(f"Different stocks : {len(rows)}\n")
        f.write(f"Total investment : {money(total)}\n")


def save_csv(rows, total, path):
    """Write the same data to a .csv file that opens in Excel."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])

        for symbol, quantity, price, value in rows:
            writer.writerow([symbol, quantity, f"{price:.2f}", f"{value:.2f}"])

        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"{total:.2f}"])


def main():
    """Run the tracker from start to finish."""
    print("=" * WIDTH)
    print("SIMPLE STOCK PORTFOLIO TRACKER".center(WIDTH))
    print("=" * WIDTH)

    show_available_stocks()

    holdings = collect_holdings()
    rows, total = build_rows(holdings)
    print_report(rows, total)

    choice = input("\nSave this report to files? (y/n): ").strip().lower()

    if choice in ("y", "yes"):
        txt_path = os.path.join(OUTPUT_FOLDER, "portfolio_report.txt")
        csv_path = os.path.join(OUTPUT_FOLDER, "portfolio_report.csv")
        save_txt(rows, total, txt_path)
        save_csv(rows, total, csv_path)
        print(f"  Saved -> {txt_path}")
        print(f"  Saved -> {csv_path}")
    else:
        print("  Report not saved.")

    print("\nDone.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nCancelled by user.")
