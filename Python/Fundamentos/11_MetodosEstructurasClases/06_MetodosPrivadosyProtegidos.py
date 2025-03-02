
# Para proteger una variable  o método se usa por convención un _ antes del nombre o metodo

class BankAccount(): 
    def __init__(self, name, balance, account):
        self.name = name
        self.balance = balance
        self.__account = account
        self.__transactions = []

    def __update_balance(self, amount, operation):
        if operation == 'increment': 
            self.balance += amount
        elif operation == 'decrement': 
            self.balance -= amount
        print(f'The actual balance is: {self.balance}')

    def _register_transaction(self, amount, account, type_transfer):

        if type_transfer == 'in': 
            self.__update_balance(amount, operation="increment")
            self.__transactions.append({
                "amount": amount,
                "account": account,
                "type_transfer": type_transfer
            })
        
        elif type_transfer == 'out': 
            self.__update_balance(amount, operation="decrement")
            self.__transactions.append({
                "amount": amount,
                "account": account,
                "type_transfer": type_transfer
            })

    def _get_account_number(self):
        print(f'Your number account is: {self.__account}') 
    def _show_transactions(self): 
        for transaction in self.__transactions:
            print(f'{transaction}\n') 

thomas_account = BankAccount("Thomas", 1500000000, 4333567867564)
david_account = BankAccount("David", 500000000, 4324567564)

thomas_account._get_account_number()
thomas_account._register_transaction(1500000, 243546573454, 'out')
thomas_account._register_transaction(23000000, 243546573454, 'in')
thomas_account._register_transaction(1500000, 243546573454, 'out')
thomas_account._show_transactions()