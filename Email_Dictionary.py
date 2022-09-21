emaild = {}                 #empty email dictionary

def menu():
    print('Menu')
    print('----------------------------------------')
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")

def lue():                                  #look up existing email
    a1 = input('Enter a name: ')
    if a1 in emaild.keys():
        print('Name:', a1, '\n Email:', emaild[a1])
    else:
        print('The specified name was not found.')

def adden():                                    #add new name and email
    a1 = input('Enter name: ')
    a2 = input('Enter email: ')
    if a1 in emaild.items() or a2 in emaild.items():
        print('Name or email already exists.')
    else:
        emaild[a1] = a2
        print('Name and email added.')

def chae():                                             #change existing email
    a1 = input('Enter name: ')
    if a1 in emaild.keys():
        a2 = input('Enter the new email: ')
        emaild[a1] = a2
        print('Information updated.')
    else:
        print('The specified name was not found.')

def delen():              #delete name and email from dictionary
    a1 = input('Enter name: ')
    if a1 in emaild.keys():
        emaild.pop(a1)
        print('Information Deleted.')
    else:
        print('The specified name was not found.')

def ef():           #load emails from file
    f = open('emails.txt', 'r')
    for line in f:
        k, v = line.split()
        emaild[k] = v
    f.close()

def sf():          #save to file
    f = open('emails.txt', 'w')
    for k, v in emaild.items():
        f.write(k + ' ' + v + '\n')
    f.close()

def main():
    menu()                                                                                              #display menu
    option = str(input("Enter your choice: "))                          #ask for user choice
    ef()
    while option != '5':                                                                        #loop while user hasn't picked to exit
        while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':                #loop if user picked an option that is not available
            print("You have entered an ***invalid option***, please try again. Your options are displayed below. \n")
            menu()
            option = str(input("Enter your choice: "))
        if option == '1':                           #for looking up an email
            lue()
        elif option == '2':                         #to add an email
            adden()
        elif option == '3':                         #to change an email
            chae()
        elif option == '4':                         #to delete an email
            delen()
        menu()                                          #promt for user input after completing task
        option = str(input("Enter your choice: "))
    sf()
    print("Information Saved.") #if they exit
main()
