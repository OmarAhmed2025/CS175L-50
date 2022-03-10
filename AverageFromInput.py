'''
Omar Ahmed
AverageFromInput
CS175L-50
Spring 2022
'''
def main():
    number_file = open('numbers.txt','r')
    count= 0
    total= 0
    average = 0
    for n in number_file:
        num = float(n)
        total = num + total
        count = count + 1
        print(f'I read in {count} number(s) Current number is: {num:6,.2f}')
    average = total/count
    print(f'Average: {average}')
main()
