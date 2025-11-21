# Problem Statement & Scope – DD Bank

## Problem Statement

In many introductory banking simulations and programming assignments, there is a need for a simple system that can model basic banking operations without using a full database or complex infrastructure.  
The problem is to design and implement a minimal bank management system that allows a user to create and manage a bank account in a secure and structured way using only core Python and file-based storage.

## Scope of the Project

The scope of this project is intentionally limited to core banking operations for a single user account at a time:

- Creating a bank account with personal details and a secure 6-digit PIN
- Depositing money into the account
- Withdrawing money with defined constraints
- Viewing current account details
- Updating selected profile details
- Deleting an existing account

The project uses a JSON file as the storage mechanism and focuses on correctness, validation, and basic error handling rather than scalability or multi-user concurrency.

## Target Users

- Students learning basic Python programming and file handling
- Beginners who want to understand how a simple bank system works
- Instructors who need a small CLI-based demo of banking operations
- Anyone who wants to experiment with a minimal account management system on the command line

## High-Level Features

1. **Account Creation**
   - Collects user details
   - Generates a random account number
   - Validates age and PIN length
   - Stores data in a JSON file

2. **Deposit Money**
   - Authenticates using account number + PIN
   - Enforces a minimum deposit amount

3. **Withdraw Money**
   - Authenticates using account number + PIN
   - Enforces a maximum withdrawal limit and checks balance

4. **View Account**
   - Prints all stored details for the authenticated user

5. **Update Account Details**
   - Allows selective updates of profile fields
   - Maintains integrity of age, account number, and balance

6. **Delete Account**
   - Authenticates the user
   - Confirms the action before permanently removing the account