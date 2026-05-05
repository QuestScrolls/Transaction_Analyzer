# Transaction Analyzer

A simple command-line Python application that helps you track and analyze a list of bank transactions. It calculates deposits, withdrawals, balance, largest transactions, and averages.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Improvements from Original](#improvements-from-original)
- [License](#license)

## Features
- **View** all transactions in a clean format.
- **Summary** of total deposited, withdrawn, and current balance.
- **Analyze** to see:
  - Largest single deposit and withdrawal.
  - Average deposit and withdrawal amounts.
- Simple interactive menu, no external dependencies.

## Installation
No additional libraries required – just Python 3.6+.

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
2.  Navigate into the project folder:
  cd transaction-analyzer
3.Run the script from the terminal
  python transaction_analyzer.py

Example Output:
Options: [view] transactions | [summary] | [analyze] | [stop]
> summary

--- Account Summary ---
Total deposited : $  4522.70
Total withdrawn : $ -2071.34
Balance          : $  2451.36
------------------------
