'''
Omar Ahmed
CS-175L
calculateaverage.py (Extra Cerdit) 
Spring 2022
'''
#Get the random numbers
import my_random 

#Main Function with main logic for program 
def main():
    cont = True
    while cont:
          n= 5
          grades=[]
          for i in range(n):
              score = get_random_val()
              grades.append(score)

          each_grade=[]
          for j in range(len(grades)):
            determine_grade(grades[j])
            each_grade.append(determine_grade(grades[j]))

          final_average= calc_average(grades)
          AVERAGE = calc_average(grades)
          f_average = determine_grade(AVERAGE)

          print("Score \t\t\t Numeric Grade \t\t\t Letter Grade")
          print("----- \t\t\t --------------\t\t\t ------------")
          for i in range(len(grades)):
              print(f"Score {i+1}: \t\t\t {grades[i]:>,.2f} \t\t\t {each_grade[i]}")
          print(f"Final Average is:\t\t {AVERAGE:>,.2f} \t\t\t {f_average}")
          cont = repeat()
    print("Goodbye!")
#Calculate Average
def calc_average(grades):
  return  sum(grades)/5

#Determining The Grade for each test score
def determine_grade(score): 
    if score >=90 and score <= 100:
        return " A "
    elif score >= 80 and score <= 89:
        return " B "
    elif score >= 70 and score <= 79:
        return " C "
    elif score >= 60 and score <= 79:
        return " D "
    else: # Grade 60 or less
        return " F "
#Repeating The Average Calculation
def repeat():
    cont = input("Would you like to compute another average?(yes or no): ")
    if cont == 'yes':
        return True
    else:
        return False
def get_random_val():
    return my_random.gen_random(1,100)
    
#Call the main function
main()
