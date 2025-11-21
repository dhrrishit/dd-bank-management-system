# DD Bank – Command-Line Bank Management System

DD Bank is a simple, command-line based bank management system built in Python.  
It allows a user to create and manage a single bank account at a time using a JSON file as lightweight storage.

---

## 🧾 Project Overview

The goal of this project is to simulate the core operations of a bank account in a minimal but structured way:

- Create a new bank account
- Deposit money
- Withdraw money
- View account details
- Update account details
- Delete an account

All the data is stored in a local JSON file, which acts as a tiny database.

---

## ✨ Features

1. **Account Creation**
   - Name, age, email, phone number, address, pincode
   - Auto-generated 9-digit account number
   - User-defined 6-digit PIN (validated)
   - Age restriction: minimum 18 years

2. **Deposit Money**
   - Validates account number + PIN
   - Minimum deposit amount: ₹500
   - Balance updated in JSON storage

3. **Withdraw Money**
   - Validates account number + PIN
   - Maximum withdrawal amount: ₹20,000 per transaction
   - Checks for sufficient balance before withdrawal

4. **View Account Details**
   - View all stored details including balance
   - Requires valid account number and PIN

5. **Update Account Details**
   - Updatable fields: Name, Email, Phone Number, Address, Pincode, Account PIN
   - Non-updatable: Age, Account Number, Balance (for integrity)
   - Empty input keeps old value

6. **Delete Account**
   - Validates account number + PIN
   - Asks for delete confirmation
   - Permanently removes account from the JSON file

---

## 🏗️ Technologies & Tools Used

- **Language:** Python 3
- **Standard Libraries:** `json`, `random`, `pathlib`
- **Storage:** Local JSON file (`data.json`)
- **Environment:** Any machine with Python 3 installed
- **Version Control:** Git + GitHub

---

## 📂 Project Structure

```text
dd-bank-management-system/
├── src/
│   └── bank_management.py      # Main application logic and menu
├── data/
│   └── data.json               # JSON storage for bank accounts
├── README.md                   # Project overview and usage instructions
├── statement.md                # Problem statement & scope
└── report/
    └── DD_Bank_Project_Report.md   # Detailed report (exported as PDF for submission)
