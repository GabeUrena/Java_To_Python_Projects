#   loading and then defining variable to read data
bank_id = '0001'
first_name = 'Gabriel'
last_name = 'Urena'
balance = 42667
pin = '1111'
creation_date = '12/07/2023'
pin_attempts = 0
is_quit = 'false'
user_input = '0'
#make object and constructor for a person's account and call their balance using person.balance

def withdraw (amount, balance):
    balance = balance - amount
    return balance

def deposit (amount, balance):
    balance = balance + amount
    return balance


print('Welcome to PYTHON BANK!')

#   Checking bank id
id_temp = input('Enter your Bank ID #: ')
while id_temp != bank_id:
    temp = (input('Invalid Bank ID, please try again. : '))

pin_temp = input(f'Welcome {first_name}, please type in your 4 digit pin! : ')
while pin_temp != pin:
    pin_attempts += 1
    if pin_attempts >= 3:
        print('You have exceeded the number of attempts, closing session!')
        break
    pin_temp = (input('Invalid pin, please try again. : '))
    
while pin_attempts < 3:

    print(f'Your total balance is: ${balance}')
    user_input = input('Would you like to (1)WITHDRAW (2)DEPOSIT (3)Exit : ')
        
    if (user_input == '1') or (user_input.lower() == 'withdraw'):
        temp_num = int(input('Enter amount to withdraw: '))
        while temp_num > balance or temp_num < 0:
            temp_num = int(input('Invalid amount please enter amount to withdraw: '))
        balance = withdraw(temp_num, balance)
            
    elif (user_input == '2') or (user_input.lower() == 'deposit'):
        temp_num = int(input('Enter amount to deposit: '))
        while temp_num < 0:
            temp_num = int(input('Invalid amount please enter amount to deposit: '))
        balance = deposit(temp_num, balance)
        
    elif (user_input != '3') or (user_input.lower() != 'exit'):
        print('Finalizing your transaction(s)')
        print('.')
        print('Exiting . . .')
        print(f'Goodbye {first_name} {last_name}.')  
        break
        

              

# create user if not found in text document
 
# make function newUser, that will generate a new id, 
# take in name, and password/pin , and starting balance

# start atm, using their password. display name and balance
# 
# prompt to deposit, withdraw, edit account,

# allow user to exit at anytime

# everything is stored on text document  
#        learn to encrypt that password and store it.


