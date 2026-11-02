account_holder_name="Renujaan" #global scope

def balance(): 
    account_balance=1000 #enclosing scope

    def branch():
        branch_name="Chenkalady Branch" #local scope

        print("Account Holder Name:", account_holder_name) #output: Renujaan
        print("Branch Name:", branch_name) #output: Chenkalady Branch
        print("Account Balance:", account_balance) #output: 1000

    branch() #call branch() function to execute the code

balance() # call balance() function to execute the code