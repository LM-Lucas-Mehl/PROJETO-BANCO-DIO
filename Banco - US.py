ballance = 0

daily_withdraw = 0

historic = ""

while True:
    menu = int(input('''
        =======================================  
                      DIO BANK
        =======================================            
        =                                     =
        =           [1] Deposit               =
        =                                     =
        =           [2] Withdraw              =
        =                                     =
        =           [3] Extract               =
        =                                     = 
        =           [0] Exit                  =
        =                                     =
        =======================================             
        SELECTION:       '''))

    # -------------------- FIXED STATS --------------------

    WITHDRAWN_DAY_LIMIT = 3
    WITHDRAWN_LIMIT = 500

    # -------------------- VOLATILE STATS --------------------
    # ballance = 0

    # historic = ""

# -------------------- FUNCTIONS -----------------------------

    # -------------------- EXIT OPERATION --------------------
    if menu == 0:
        print("        Thanks for using our services, come back anytime you need.")
        break
    

    while True:
    # -------------------- DEPOSIT OPERATION --------------------
            
            if menu == 1:
                amount  = float(input('''
        AMOUNT: '''))
                ballance += amount
                historic += f'DEPOSIT: R$ {amount:.2f}\n'
            
                # RETURN TO MENU
                ansdep = str(input('''
                    Repeat Action: 
                [Y]               [N]
                          ''')).upper()
                
                if ansdep == 'Y':
                    continue
                elif ansdep == 'N':
                    break
                
                else:
                    print("        Invalid command, please try again.")
                
                break

    # -------------------- WITHDRAWN OPERATION --------------------

            elif menu == 2:
                withdrawn = float(input('''
        AMOUNT: '''))
                if ballance < withdrawn:
                    print("Transaction invalid, not enough credits")
                    
                elif withdrawn > WITHDRAWN_LIMIT:
                    print("Transaction Invalid, withdraw limit reached")
                    
                elif daily_withdraw >= WITHDRAWN_DAY_LIMIT:
                    print("Transaction Invalid, daily withdraw limit reached, come back tomorrow")
                else:
                    ballance -= withdrawn
                    daily_withdraw += 1
                    historic += f'WITHDRAWN: R$ {withdrawn:.2f}\n'
                 
                # RETURN TO MENU   
                ansdep = str(input('''
                    Repeat Action: 
                [Y]               [N]
                          ''')).upper()
                
                if ansdep == 'Y':
                    continue
                elif ansdep == 'N':
                    break
                
                else:
                    print("        Invalid command, please try again.")

    # -------------------- EXTRACT OPERATION --------------------

            elif menu == 3:
                
                print('''\n================ EXTRACT ================''')
                print(f"{historic}")
                print('=========================================')
                print(f"SALDO: R$ {ballance}")
                print('=========================================')
                # if extract == Y:

                # elif extract == N:
                
                # RETURN TO MENU
                ansdep = str(input('''
                    Repeat Action: 
                [Y]               [N]
                          ''')).upper()
                
                if ansdep == 'Y':
                    continue
                elif ansdep == 'N':
                    break
                
                else:
                    print("        Invalid command, please try again.")
            
            else:
                print("        Invalid command, please try again")
                break
