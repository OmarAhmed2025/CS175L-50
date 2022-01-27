#Name: Omar Ahmed
# CS 175L-50
#Spring 2022

# Useer Inputs 

commission= float(input("Constant Commission Rate: "))
shares=int(input("How many shares did you purchase: "))
purchase=float(input("How much did you pay per share: "))
selling_price=float(input("Selling Price: "))

# Calculations 

amount=shares * purchase
pre_com= amount * commission
sold= selling_price * shares
post_com= sold * commission
total_com= pre_com + post_com
total_profit= sold - amount - total_com
 #Print Statements
print(f'Total amount paid for stock: $  {amount: .2f}' )
print(f'Commission paid on the purchase: $ {pre_com: .2f}' )
print(f'Amount the stock sold for: $ {sold: .2f}')
print(f'Commission paid on the sale: $ {post_com: .2f}')
print(f'Total commission paid: $ {total_com: .2f}')
print(f'Total profit: $ {total_profit: .2f}')                 
        
