# Stock Portfolio Tracker

A command-line tool in Python that calculates the total value of a stock portfolio.
The user enters stock symbols and quantities, the program looks up each price from a
predefined dictionary, computes the value of every holding, and prints a summary table.
The report can be saved as both a plain-text file and a CSV.

Built with the Python standard library only — no external packages required.

## Features

- Predefined price list held in a dictionary (8 stocks, easy to edit)
- Interactive input for stock symbols and quantities
- Case-insensitive symbols (`aapl` and `AAPL` both work)
- Input validation: unknown symbols and non-numeric or zero quantities are rejected
  and re-prompted instead of crashing
- Repeated entries of the same stock are merged (10 AAPL + 5 AAPL = 15 AAPL)
- Holdings sorted by value, with each stock's percentage share of the portfolio
- Exports `portfolio_report.txt` (formatted report) and `portfolio_report.csv` (opens in Excel)

## How to run

```bash
python stock_tracker.py
```

Type `LIST` at the symbol prompt to see the available stocks. Press Enter on an
empty line to finish entering holdings.

## Sample run

```
====================================================
                 PORTFOLIO SUMMARY
====================================================
STOCK     QTY        PRICE           VALUE     SHARE
----------------------------------------------------
INFY        2    $1,650.00       $3,300.00     47.1%
AAPL       15      $180.00       $2,700.00     38.6%
TSLA        4      $250.00       $1,000.00     14.3%
----------------------------------------------------
TOTAL INVESTMENT                           $7,000.00
====================================================
```

## Generated CSV

```csv
Stock,Quantity,Price,Value
INFY,2,1650.00,3300.00
AAPL,15,180.00,2700.00
TSLA,4,250.00,1000.00

TOTAL,,,7000.00
```

## Concepts used

| Concept | Where it appears |
|---|---|
| Dictionary | `STOCK_PRICES` price lookup; `holdings` symbol-to-quantity map |
| Input / output | `collect_holdings()`, `print_report()` |
| Basic arithmetic | `value = quantity * price`, running total, percentage share |
| File handling | `save_txt()` with `open()`, `save_csv()` with the `csv` module |
| Functions | Each step is a separate function called from `main()` |
| Validation loops | `ask_quantity()` re-prompts until the input is valid |

## Customising

Prices and currency live at the top of the script:

```python
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    # add your own here
}

CURRENCY = "$"      # change to "Rs." for Indian stock prices
```

## Scope and limitations

Prices are hardcoded, not fetched live, so the total reflects the values written in
`STOCK_PRICES` rather than the current market. It calculates the value of a holding
at the given price; it does not track cost basis, profit/loss, brokerage, or currency
conversion. A natural next step would be reading prices from a CSV file or a market
data API, and using pandas for larger portfolios.

## Files

| File | Description |
|---|---|
| `stock_tracker.py` | The program |
| `portfolio_report.txt` | Text report (generated on save) |
| `portfolio_report.csv` | CSV export (generated on save) |

---

Author: Bhavesh Tayade
