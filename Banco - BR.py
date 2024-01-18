saldo = 0

limite_diario = 0

extrato = ""

while True:
    menu = int(input('''
        =======================================  
                      BANCO DIO
        =======================================            
        =                                     =
        =           [1] Deposito              =
        =                                     =
        =           [2] Saque                 =
        =                                     =
        =           [3] Extrato               =
        =                                     = 
        =           [0] Sair                  =
        =                                     =
        =======================================             
        SELECTION:       '''))

    # -------------------- STATUS FIXOS --------------------

    LIMITE_SAQUE_DIARIO = 3
    LIMITE_SAQUE = 500
    
# -------------------- FUNÇÕES -----------------------------

    # -------------------- FUNÇÃO SAÍDA --------------------
    if menu == 0:
        print("        Obrigado por utilizar nossos serviços, volte sempre.")
        break
    

    while True:
    # -------------------- FUNÇÃO DEPOSITO --------------------
            
            if menu == 1:
                valor  = float(input('''
        VALOR: '''))
                saldo += valor
                extrato += f'DEPOSITO: R$ {valor:.2f}\n'
            
                # RETORNAR AO MENU
                quest = str(input('''
                    Repetir Ação: 
                [Y]               [N]
                          ''')).upper()
                
                if quest == 'Y':
                    continue
                elif quest == 'N':
                    break
                
                else:
                    print("        Comando inválido, tente novamente")
                
                break

    # -------------------- FUNÇÃO SAQUE --------------------

            elif menu == 2:
                saque = float(input('''
        VALOR: '''))
                if saldo < saque:
                    print("Operação invalida, saldo insuficiente")
                    
                elif saque > LIMITE_SAQUE:
                    print("Operação invalida, limite de saque excedido")
                    
                elif limite_diario >= LIMITE_SAQUE_DIARIO:
                    print("Transação invalida, limite diario de saque atingido, retorne amanhã")
                else:
                    saldo -= saque
                    limite_diario += 1
                    extrato += f'saque: R$ {saque:.2f}\n'
                 
                # RETORNAR AO MENU   
                quest = str(input('''
                    Repetir ação: 
                [Y]               [N]
                          ''')).upper()
                
                if quest == 'Y':
                    continue
                elif quest == 'N':
                    break
                
                else:
                    print("        Comando inválido, tente novamente")

    # -------------------- EXTRACT OPERATION --------------------

            elif menu == 3:
                print('''\n================ EXTRATO ================''')
                print(f"{extrato}")
                print('=========================================')
                print(f"SALDO: R$ {saldo}")
                print('=========================================')
                # if extract == Y:

                # elif extract == N:
                
                # RETORNAR AO MENU
                quest = str(input('''
                    Repetir ação: 
                [Y]               [N]
                          ''')).upper()
                
                if quest == 'Y':
                    continue
                elif quest == 'N':
                    break
                
                else:
                    print("        Comando inválido, tente novamente")
                    
            else:
                print("        Comando inválido, tente novamente")
                break
