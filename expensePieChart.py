'''
Omar Ahmed
BestSellers
CS175L-50
Spring 2022
'''

import matplotlib.pyplot as plt
import numpy as np
def main():
     try:
        expense_file = open('expenses.txt','r')
     except IOError:
        print('ERROR: File not found')
     else:
         pi_chart(expense_file)
    
def pi_chart(ex):
    expense_list = []
    for n in ex:
        n =  n.strip('\n')
        expense_list.append(n.split('\t'))
    amount = []
    name = []
    for i in expense_list:
        amount.append(i[1])
        name.append(i[0])
    y = np.array(amount)
    mylabels = name 
    plt.pie(y, labels = mylabels)         
    plt.show()
        
main()
