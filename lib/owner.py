
class Owner():

    account_balance = 1000.00

    def __init__(self, first_name, last_name, age, account_balance=1000):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = account_balance

    #Decorator
    #🛑 build out methods then see how to use decorators
    def balance_calculator(func):
        def report_account(owner):
            print(f'calc, {owner.first_name} Account Amount: {owner.account_balance}')
            final_balance = func(owner) #🛑 func is  the function below the decorator
            print(f'calc, {owner.first_name} New Account Amount = ${final_balance}')
        return report_account
    
    @balance_calculator
    def vet_visit(self, bill=100): #🛑 vet_visit is the func being passed into balance_calculator
        # print(f'Current Account Balance: $1000')
        # final_balance = func(100.00)
        # print(f'New Account Balance = ${final_balance}')
        print(f"vet, Deducting {bill} from Account...")
        self.account_balance -= bill
        
        return '{:.2f}'.format(self.account_balance)

    @balance_calculator
    def weekly_food(self, bill = 50):
        # print(f'Current Account Balance: $1000')
        # final_balance = func(50.00)
        # print(f'New Account Balance = ${final_balance}')
        print(f"Deducting {bill} from Account...")
        self.account_balance -= bill
        
        return '{:.2f}'.format(self.account_balance)
        
    @balance_calculator
    def weekly_housing(self, bill = 75):
        # print(f'Current Account Balance: $1000')
        # final_balance = func(75.00)
        # print(f'New Account Balance = ${final_balance}')
        print(f"Deducting {bill} from Account...")
        self.account_balance -= bill
        
        return '{:.2f}'.format(self.account_balance)
    
import ipdb; ipdb.set_trace()