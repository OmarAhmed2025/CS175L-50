'''
Omar Ahmed
AverageFromInputwithexceptionhandling
CS175L-50
Spring 2022
'''
def main():
          try:
              number_file = open('numbers.txt','r')
          except IOError:
            print('ERROR: File not found')
          else:
              cnt,tot = read_nums(number_file)
              av = average(tot,cnt)
              print(f"The average of {cnt} nums in the file is: {av}")
                  

          
    
             
                     

def read_nums(number_file):
    count= 0
    total= 0
    average = 0
    for n in number_file:
         try:
            num = float(n)
         except ValueError:
            print('ERROR: Not an integer!')
         else:
            print(n)
            total = num + total
            count = count + 1
    return count, total

def average(tot, cnt):
    average = tot/cnt
    return average

if __name__== '__main__':
    main()
