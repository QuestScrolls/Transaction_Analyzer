#!/usr/bin/env python3
"""
Transaction Analyzer
--------------------
A simple command-line tool to analyze a list of financial transactions.
Supports viewing all transactions, printing a summary, and showing key statistics.

Run directly: python transaction_analyzer.py
"""

from typing import List, Tuple

# Sample data (amount, description)
TRANSACTIONS: List[Tuple[float, str]] = [
    (749.17, "Investment Return"),
    (-11.54, "Utilities"),
    (-247.58, "Online Shopping"),
    (981.17, "Investment Return"),
    (-410.65, "Rent"),
    (310.60, "Rent"),
    (563.70, "Gift"),
    (220.79, "Salary"),
    (-49.85, "Car Maintenance"),
    (308.49, "Salary"),
    (-205.55, "Car Maintenance"),
    (870.64, "Salary"),
    (-881.51, "Utilities"),
    (518.14, "Salary"),
    (-264.66, "Groceries"),
]


def print_transactions(transactions: List[Tuple[float, str]]) -> None:
    """Print each transaction in a formatted way."""
    if not transactions:
        print("No transactions to display.")
        return
    print("\n--- All Transactions ---")
    for amount, statement in transactions:
        print(f"${amount:>10.2f}  {statement}")
    print("------------------------")


def print_summary(transactions: List[Tuple[float, str]]) -> None:
    """Print total deposits, total withdrawals, and net balance."""
    deposits = [amt for amt, _ in transactions if amt >= 0]
    withdrawals = [amt for amt, _ in transactions if amt < 0]

    total_deposited = sum(deposits)
    total_withdrawn = sum(withdrawals)
    balance = total_deposited + total_withdrawn

    print("\n--- Account Summary ---")
    print(f"Total deposited : ${total_deposited:>10.2f}")
    print(f"Total withdrawn : ${total_withdrawn:>10.2f}")
    print(f"Balance          : ${balance:>10.2f}")
    print("------------------------")


def analyze_transactions(transactions: List[Tuple[float, str]]) -> None:
    """
    Analyze transactions: show largest deposit/withdrawal and averages.
    Does NOT modify the original list.
    """
    if not transactions:
        print("No transactions to analyze.")
        return

    # Separate amounts without sorting the original list
    deposits = [(amt, desc) for amt, desc in transactions if amt >= 0]
    withdrawals = [(amt, desc) for amt, desc in transactions if amt < 0]

    # Largest deposit and withdrawal
    largest_deposit = max(deposits, key=lambda x: x[0], default=None)
    largest_withdrawal = min(withdrawals, key=lambda x: x[0], default=None)

    # Averages
    avg_deposit = sum(amt for amt, _ in deposits) / len(deposits) if deposits else 0.0
    avg_withdrawal = sum(amt for amt, _ in withdrawals) / len(withdrawals) if withdrawals else 0.0

    print("\n--- Transaction Analysis ---")
    if largest_deposit:
        print(f"Largest deposit : ${largest_deposit[0]:.2f} - {largest_deposit[1]}")
    else:
        print("No deposits found.")
    if largest_withdrawal:
        print(f"Largest withdrawal: ${largest_withdrawal[0]:.2f} - {largest_withdrawal[1]}")
    else:
        print("No withdrawals found.")
    print(f"Average deposit   : ${avg_deposit:.2f}")
    print(f"Average withdrawal: ${avg_withdrawal:.2f}")
    print("-----------------------------")


def main():
    """Command-line menu loop."""
    print("Welcome to Transaction Analyzer!")
    while True:
        print("\nOptions: [view] transactions | [summary] | [analyze] | [stop]")
        choice = input("> ").strip().lower()

        if choice == "view":
            print_transactions(TRANSACTIONS)
        elif choice == "summary":
            print_summary(TRANSACTIONS)
        elif choice == "analyze":
            analyze_transactions(TRANSACTIONS)
        elif choice in ("stop", "quit", "exit"):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 'view', 'summary', 'analyze', or 'stop'.")


if __name__ == "__main__":
    main()
