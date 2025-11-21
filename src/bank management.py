import json
import random
from pathlib import Path

GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

class Bank:
    data = 'data/data.json' # path of the data file
    dummy_data = [] # for dummy (copy) data
    try:
        if Path(data).exists() and Path(data).is_file(): # checking PATH of our data exists or not
            with open(data,'r') as erk: # reading the file
                dummy_data = json.loads(erk.read()) # dummy loading the entire json file in dummy_data
        else: 
            print("No such file exists. Please try a different path!")
    except Exception as err:
        print(f"There was an error! - {err}")

    @staticmethod
    def __update():  # updating the data from dummy into the data.json
        with open(Bank.data, 'w') as erk:
            erk.write(json.dumps(Bank.dummy_data))
        
    def Createaccount(self):
        try:
            info = {
                "Name": input("Enter your full name: "),
                "Age": int(input("Enter your age: ")),
                "Email": input("Enter your email: "),
                "Phone Number": int(input("Enter your phone number (+91): ")),
                "Address": input("Enter your address: "),
                "Pincode": int(input("Enter your pincode: ")),
                "Account Number": random.randint(100000000,999999999),
                "Account Pin": int(input("Enter your 6 digit PIN: ")),
                "Balance" : 0
            }
            if info['Age']<18: 
                print(RED + "Sorry you are not eligible to create a bank account!" + ENDC)
            elif len(str(info['Account Pin'])) != 6:
                print(RED + "Please set-up a valid 6-digit Pin" + ENDC)
            else:
                print("_______________________________________________________________________")
                print("Thank you, Please note down these detials -")
                for i in info:
                    print(RED + f"{i}: {info[i]}" + ENDC)
                Bank.dummy_data.append(info)
                Bank.__update()
        except Exception as err:
            print(f"Sorry there was an error as {err}, DD account was not Created!")


    def Depositamount(self):
        try:
            accCheck = int(input("Please enter your account number: "))
            pinCheck = int(input("Please enter your 6-digit PIN: "))
            userdata = [i for i in Bank.dummy_data if accCheck == i['Account Number'] and pinCheck == i['Account Pin']]
            if not userdata:
                print("No matched credentials found! Please enter your valid details.")
            else:
                print(f"Welcome {userdata[0]['Name']}!")
                try:
                    amt = int(input("Enter the amount you want to deposit (₹): "))
                    if 500>amt:
                        print("Please deposit an allowed amount (₹500-₹50,000)")
                    else:
                        userdata[0]["Balance"] += amt 
                        Bank.__update()
                        print(GREEN + "Amount Deposited Succesfully!" + ENDC)
                except ValueError as vae:
                    print(RED + f"There was a value error as {vae}" + ENDC)
        except Exception as err:
            print(f'Sorry there was an error as {err}!')
            

    def Withdrawamount(self):
        try:
            accCheck = int(input("Please enter your account number: "))
            pinCheck = int(input("Please enter your 6-digit PIN: "))
            userdata = [i for i in Bank.dummy_data if accCheck == i['Account Number'] and pinCheck == i['Account Pin']]
            if not userdata:
                print(RED + "No matched credentials found! Please enter your valid details." + ENDC)
            else:
                print(f"Welcome {userdata[0]['Name']}!")
                amt = int(input("Enter the amount you want to withdraw (₹): "))
                if amt > 20000:
                    print(RED + "Withdrawal amount cannot exceed ₹20,000!" + ENDC)
                elif userdata[0]["Balance"] < amt:
                    print("Insufficient Balance!")
                else:
                    userdata[0]["Balance"] -= amt
                    Bank.__update()
                    print(GREEN + "Amount Withdrawn Successfully!" + ENDC)
        except Exception as err:
            print(RED + f'Sorry there was an error as {err}!' + ENDC)


    def ViewAccount(self):
        accCheck = int(input("Please enter your account number: "))
        pinCheck = int(input("Please enter your 6-digit PIN: "))
        userdata = [i for i in Bank.dummy_data if accCheck == i['Account Number'] and pinCheck == i['Account Pin']]
        if not userdata:
            print(RED + "No matched credentials found! Please enter your valid details." + ENDC)
        else:
            print("_____________________________________________")
            print(RED + f"Welcome {userdata[0]['Name']}!" + ENDC)
            print("Here are your details: \n ")
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")
            print("_____________________________________________")


    def Updatedetails(self):
        accCheck = int(input("Please enter your account number: "))
        pinCheck = int(input("Please enter your 6-digit PIN: "))
        userdata = [i for i in Bank.dummy_data if accCheck == i['Account Number'] and pinCheck == i['Account Pin']]
        if not userdata:
            print(RED + "No matched credentials found! Please enter your valid details." + ENDC)
        else:
            try:
                print(RED + f"Welcome {userdata[0]['Name']}!" + ENDC)
                print("You cannot change your Age, Acount Number or Balance \nPlease fill the details below or leave it empty for no change.")
                updated_name = input("Enter your updated name: ")
                if updated_name:
                    userdata[0]["Name"] = updated_name

                updated_email = input("Enter your updated email: ")
                if updated_email:
                    userdata[0]["Email"] = updated_email

                updated_phone = input("Enter your updated phone number: ")
                if updated_phone:
                    userdata[0]["Phone Number"] = int(updated_phone)

                updated_address = input("Enter your updated address: ")
                if updated_address:
                    userdata[0]["Address"] = updated_address

                updated_pincode = input("Enter your updated pincode: ")
                if updated_pincode:
                    userdata[0]["Pincode"] = int(updated_pincode)

                updated_pin = input("Enter your updated account PIN: ")
                if updated_pin:
                    userdata[0]["Account Pin"] = int(updated_pin)

                Bank.__update()
                print(GREEN + "Details updated successfully!" + ENDC)
            except ValueError:
                print(RED + "Invalid input for a numeric field. Please enter numbers only." + ENDC)
            except Exception as err:
                print(RED + f"An error occurred: {err}" + ENDC)

    def DeleteAccount(self):
        accCheck = int(input("Please enter your account number: "))
        pinCheck = int(input("Please enter your 6-digit PIN: "))
        userdata = [i for i in Bank.dummy_data if accCheck == i['Account Number'] and pinCheck == i['Account Pin']]
        if not userdata:
            print(RED + "No matched credentials found! Please enter your valid details." + ENDC)
        else:
            print(RED + f"Welcome {userdata[0]['Name']}!" + ENDC)
            print("Please confirm you want to proceed with this action:")
            print(f"1 : {RED}Delete{ENDC} your bank account")
            print(f"2 : {GREEN}Exit{ENDC} this choice")
            check = int(input("Enter your choice: "))
            if check == 2:
                pass
                print("No worries. Happy Banking")
            elif check == 1:
                index = Bank.dummy_data.index(userdata[0])
                Bank.dummy_data.pop(index)
                print(GREEN + f"Account Deleted Succesfully!" + ENDC)
                Bank.__update()
            else:
                print("Please enter a valid choice!")

user = Bank() # created an object as user

while True: 
    print("_____________________________________________")
    print("Press 1 to create a DD Bank account")
    print("Press 2 to deposit an amount to your account")
    print("Press 3 to withdraw money from your account")
    print("Press 4 to view details of your account")
    print("Press 5 to update your bank details")
    print("Press 6 to delete your DD Bank account")
    print("Press 7 to exit this program")
    print("_____________________________________________")
    try:
        check = int(input("Enter your response: "))
        if check == 1:
            user.Createaccount()
        elif check == 2: 
            user.Depositamount()
        elif check == 3:
            user.Withdrawamount()
        elif check == 4:
            user.ViewAccount()
        elif check == 5: 
            user.Updatedetails()
        elif check == 6:
            user.DeleteAccount()
        elif check == 7:
            print(RED + "Exiting Program...." + ENDC)
            break
        else:
            print(RED + f'Sorry, please refer to the options given above!' + ENDC)
    except Exception as err:
        print(RED + f'Sorry, please refer to the options given above!' + ENDC)