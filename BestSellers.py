#Omar Ahmed and Ava Ondecker
#BestSellers
#CS175L-50
#Spring 2022

def main():
    sb_list=[]
    b_list = []
    cntr,sb_list,b_list = read_books()
    print(f"Read {cntr} Books ")
    while(True):
        print("What would you like to do?")
        print("1: Look up year range")
        print("2: Look up month/year")
        print("3: Search for Author")
        print("4: Search for title")
        print("Q: Quit")

        response= input("Enter the menu Item: ")

        if response == '1':
            year_range(b_list)
        elif response == '2':
            month_year(b_list)
        elif response == '3':
            author(b_list)
        elif response == '4':
            title(b_list)
        elif response == 'Q' or  response == 'q':
            print('Done')
            break
        else:
            print("I don't understand this command!")

def read_books():
    book_list = open('bestsellers.txt', 'r')
    books =[]
    count = 0
    for line in book_list.readlines():
        line = line.strip()
        count +=1
        sub_list = []
        sub_list.append(line.split('\t'))
        books.append(sub_list)
    #print(sub_list)
    #print(books)
    return count,sub_list,books

def year_range(b_list):
    year1 = int(input("Enter The Starting Year: "))
    year2 = int(input("Enter The Ending Year: "))
    for items in range(0,len(b_list)):
        current = b_list[items] [0][3]
        for letter in current:
            if letter == ' ' or letter == '/t':
               current = current.replace(letter, '')
        date = int(current[len(current)-4:])
        if date >= year1 and date<= year2:
            print(b_list[items][0][0], 'by:', b_list[items][0][1], '(pub date:',current + ')')
        
def month_year(b_list):
    month = int(input("Enter The Month(1-12): "))
    year = int(input("Enter The Year: "))
    for items in range(0,len(b_list)):
        current = b_list[items] [0][3]
        for letter in current:
            if letter == ' ' or letter == '/t':
               current = current.replace(letter, '')
        dates = current.split('/')
        bYear = int(dates[2])
        bMonth = int(dates[0])
        if month == bMonth and year == bYear:
            print(b_list[items][0][0], 'by:', b_list[items][0][1], '(pub date:',current + ')')
        

def author(b_list):
    author = (input("Enter Search String: "))
    for items in range(0,len(b_list)):
        current = b_list[items] [0][1]
        for letter in current:
            if letter == ' ' or letter == '/t':
               current = current.replace(letter, '')
        if author.lower() in current.lower():
            print(b_list[items][0][0], 'by:', b_list[items][0][1], '(pub date:',b_list[items][0][3] + ')')
        
def title(b_list):
    title = (input("Enter Search String: "))
    for items in range(0,len(b_list)):
        current = b_list[items] [0][0]
        if title.lower() in current.lower():
            print(b_list[items][0][0], 'by:', b_list[items][0][1], '(pub date:',b_list[items][0][3] + ')')
        

main()
