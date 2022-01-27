#Name: Omar Ahmed
#CS 175L-50
#Stocks Assignment
#Spring 2022

# User Inputs for Stock Prices and Shares

commission= float(input("Constant Commission Rate: "))
shares=int(input("How many shares did you purchase: "))
purchase=float(input("How much did you pay per share: "))
selling_price=float(input("Selling Price: "))

# Calculations for Stock Prices and Commission

amount=shares * purchase
pre_com= amount * commission
sold= selling_price * shares
post_com= sold * commission
total_com= pre_com + post_com
total_profit= sold - amount - total_com
 # Format Print Statements for Stocks Results 
print(f'Total amount paid for stock: $  {amount: .2f}' )
print(f'Commission paid on the purchase: $ {pre_com: .2f}' )
print(f'Amount the stock sold for: $ {sold: .2f}')
print(f'Commission paid on the sale: $ {post_com: .2f}')
print(f'Total commission paid: $ {total_com: .2f}')
print(f'Total profit: $ {total_profit: .2f}')                 
        
