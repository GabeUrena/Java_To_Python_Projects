from datetime import date
class atm2:

#make object and constructor for a person's account and call their balance using person.balance

    def __init__(self):
        self.bank_id = ''
        self.first_name = ''
        self.last_name = ''
        self.balance = 0
        self.pin = ''
        self.creation_date = date.today()


    def __init__(self, id, fname, lname, bal, p):
        self.bank_id = id
        self.first_name = fname
        self.last_name = lname
        self.balance = bal
        self.pin = p
        self.creation_date = date.today()


    def getFName(self):
        return self.first_name


    def getLName(self):
        return self.last_name


    def getBalance(self):
        return self.balance


    def getPin(self):
        return self.pin


    def getCreationDate(self):
        return self.creation_date


    def withdraw (self, amount, balance):
        self.balance = self.balance - amount
        return self.balance


    def deposit (self, amount, balance):
        self.balance = self.balance + amount
        return self.balance


    def start (self):
    
        pin_attempts = 0
        is_quit = 'false'
        user_input = '0'
        
        print('Welcome to PYTHON BANK!')

        #   Checking bank id
        id_temp = input('Enter your Bank ID #: ')
        while id_temp != self.bank_id:
            temp = (input('Invalid Bank ID, please try again. : '))

        pin_temp = input(f'Welcome {self.first_name}, please type in your 4 digit pin! : ')
        while pin_temp != self.pin:
            pin_attempts += 1
            if pin_attempts >= 3:
                print('You have exceeded the number of attempts, closing session!')
                break
            pin_temp = (input('Invalid pin, please try again. : '))
        
        while pin_attempts < 3:

            print(f'Your total balance is: ${self.balance}')
            user_input = input('Would you like to (1)WITHDRAW (2)DEPOSIT (3)Exit : ')
            
            if (user_input == '1') or (user_input.lower() == 'withdraw'):
                temp_num = int(input('Enter amount to withdraw: '))
                while temp_num > self.balance or temp_num < 0:
                    temp_num = int(input('Invalid amount please enter amount to withdraw: '))
                self.balance = self.withdraw(temp_num, self.balance)
                
            elif (user_input == '2') or (user_input.lower() == 'deposit'):
                temp_num = int(input('Enter amount to deposit: '))
                while temp_num < 0:
                    temp_num = int(input('Invalid amount please enter amount to deposit: '))
                self.balance = self.deposit(temp_num, self.balance)
            
            elif (user_input != '3') or (user_input.lower() != 'exit'):
                print('Finalizing your transaction(s)')
                print('.')
                print('Exiting . . .')
                print(f'Goodbye {self.first_name} {self.last_name}.')  
                break
        

person1 = atm2('0001', 'Gabriel','Urena',4123.55,'1111')
person1.start()

# create user if not found in text document
 
# make function newUser, that will generate a new id, 
# take in name, and password/pin , and starting balance

# start atm, using their password. display name and balance
# 
# prompt to deposit, withdraw, edit account,

# allow user to exit at anytime

# everything is stored on text document  
#        learn to encrypt that password and store it.


