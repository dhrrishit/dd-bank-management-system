# 🏦 DD Bank – Command-Line Bank Management System (Python + JSON)

DD Bank is a simple and fully functional **command-line based Bank Management System** developed using Python. It allows users to create and manage bank accounts with features like deposit, withdrawal, updating details, viewing details, and deleting accounts. All data is stored in a **JSON file**, making the project lightweight, portable, and easy to maintain.

---

## 📌 Overview

This project simulates the core banking operations in a simple CLI environment. It was developed as part of VIT Bhopal’s **Build Your Own Project (BYOP)** requirement.

The project includes:

* Proper folder structure
* Multiple functional modules
* JSON-based data storage
* User authentication using Account Number + PIN
* Error handling & validation
* Complete documentation

---

## ✨ Features

### **1. Create Bank Account**

* Collects user details (Name, Age, Email, Phone, Address, Pincode)
* Generates a unique **9-digit account number** automatically
* Requires a **valid 6-digit PIN**
* Ensures user age is **18+**

### **2. Deposit Money**

* Authenticates using Account Number + PIN
* Minimum deposit: **₹500**
* Updates balance in the JSON file

### **3. Withdraw Money**

* Authenticates user
* Maximum withdrawal per transaction: **₹20,000**
* Ensures sufficient balance

### **4. View Account Details**

* Shows all stored information
* Requires correct credentials

### **5. Update Account Details**

* Editable fields: Name, Email, Phone, Address, Pincode, PIN
* Non-editable: Age, Account Number, Balance
* Empty inputs keep old values

### **6. Delete Account**

* Requires authentication
* Asks for confirmation before permanent deletion

---

## 🏗️ Technologies Used

* **Python 3**
* **JSON** for data storage
* **pathlib**, **json**, **random** modules
* **Git / GitHub** for version control

---

## 📂 Project Structure

```text
dd-bank-management-system/
├── src/
│   └── bank_management.py
├── data/
│   └── data.json
├── README.md
├── statement.md
└── report/
    └── DD_Bank_Project_Report.pdf (to be uploaded separately)
```

---

## ⚙️ Installation & Running the Project

### **1. Clone the Repository**

```bash
git clone https://github.com/dhrrishit/dd-bank-management-system.git
cd dd-bank-management-system
```

### **2. Ensure Python Is Installed**

```bash
python --version
```

Python 3.x is required.

### **3. Run the Program**

```bash
cd src
python bank_management.py
```

You will see a menu like:

```text
Press 1 to create a DD Bank account
Press 2 to deposit an amount
Press 3 to withdraw money
Press 4 to view account details
Press 5 to update your details
Press 6 to delete your account
Press 7 to exit
```

---

## 🧪 Testing Instructions

You can manually test by trying:

* Creating an account with valid & invalid inputs
* Depositing below ₹500
* Withdrawing above balance
* Updating only one field
* Deleting an account & verifying deletion

---

## 📸 Screenshots

### **1. Program Start (Main Menu)**
![Program Start](images/Program%20Start.png)

### **2. Account Details Saved Display**
![Details Saved Display](images/Details%20Saved%20Display.png)

### **3. Data Stored in JSON Format**
![Data in JSON](images/data%20in%20JSON%20format.png)

---

## 👤 Author

**Name:** Dhrrishit V. Deka

---

## 📄 License

This project is for academic and learning purposes.
