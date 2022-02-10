'''
Omar Ahmed
CS175-50L
Resturant
SP 2022
'''

# While Loop
cont="yes"

while cont == "yes":

    vegetarian=False
    vegan=False
    glutenfree=False

    #Prompting User

    vege= input("Is anyone in your party a vegetrian?: ")
    if vege.lower() == 'yes':
        vegetarian= True

    veg=input("Is anyone is your party vegan?: ")
    if veg.lower() == 'yes':
        vegan = True

    gluten=input("Is anyone in your party gluten-free?: ")
    if gluten.lower() == 'yes':
        glutenfree= True

    #Output of Resturant Choices 

    if vegan:
        print('Corner Cafe \n The Chefs kitchen')
    elif glutenfree:
        print('Main Street Pizza Company \n Corner Cafe \n The Chefs Kitchen ')
    elif vegetarian:
        print('Main Street Pizza Company \n Corner Cafe \n The Chefs Kitchen \n Mamas Fine Italian')
    else:
        print('Joes Gourmet Burgers \nMain Street Pizza Company \n Corner Cafe \n The Chefs Kitchen \n Mamas Fine Italian')
    repeat=print("If you would like to contine type yes if not type no to end")
    cont= input()
print("Goodbye!")
