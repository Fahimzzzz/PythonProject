import string                                                   #import the alphabet
abc = string.ascii_lowercase                            #set lowercase alphabet to global variable abc
mcabc = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'] #mcabc variable for morse code letters
mcnum = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.'] #mcnum for morse code numbers 1-0
mcd, mcdf = {}, {}                                    #empty dictionary for morse code, empty dictionary for flipped morse code dictionary

def menu():                                                         #a function to display the menu options
    print("*** Enter 't' for encoding text.")               #option 1
    print("*** Enter 'm' for decoding morse code.") #option 2
    print("*** Enter 'e' to exit the program.")             #option 3

def mcid():                                                     #function to put letters and numbers with corresponding morse code in dictionary
    for i in range(len(abc)):                               #adding letters first, run for length of alphabet
        mcd[abc[i]] = mcabc[i]                          #add letter and morse code to mcd dictionary as key and value
    for i in range(10):                                     #adding numbers onto morse code dictionary
        mcd[str(i)] = mcnum[i]
    mcd[' '] = ' '                                                  #empty space for dictionary
    for k, v in mcd.items():                                #flipped morse code dictionary
        mcdf[v] = k
mcid()

def abctmc():                                                       #function to convert english text to morse code
    conv = ''                                                           #empty string that will contain conversion
    i1 = list(input("Enter the text to be converted: "))            #user input that will be converted
    for i in range(len(i1)):                                        #make userinput all lowercase
        i1[i] = i1[i].lower()
    for i in i1:                                                        #put morse code into conversion variable given the key for morse code dictionary
        conv = conv + mcd[i] + ' '
    print(conv)                                                         #print translation, 1 space already include at end of each morse code with each regular space being covereted to 2 spaces, allowing to meet the requirement of 1 space between morse code chars and 3 between morse code words

def mctabc():                                                       #function to convert morse code into text
    mc, mctoabc = '', ''                              #list for morse code and conversion
    sc = 0                                              #keep track of spaces
    i2 = list(input("Enter the morse code to be converted: ") + ' ')        # grab user input into list
    for i in i2:                                                                                    #loop to check characters
        if i != ' ':                                                                                #if not a space, add morse code to mc
            sc = 0
            mc = mc + i
        elif i == ' ':                                                                              #if a space is found, search flipped morse code dictionary for translation and add it to conversion variable mctoabc.
            sc = sc + 1
            if mc != '':
                mctoabc = mctoabc + mcdf[mc]
                mc = ''
            elif sc == 3:                                                                       #if space count is 3, add a space to conversion variable
                mctoabc = mctoabc + ' '
    print(mctoabc)                                                                          #print morse code translation

def main():                                                         #main function that will operate the others
    print('Hello, this program allows you to translate text to morse code or translate morse code to text.')                #Greetings
    print('There are three options displayed below.\n')                                                                                 
    menu()                                                                                              #display menu
    option = str(input("Please enter your choice here: "))                          #ask for user choice
    while option != 'e':                                                                        #loop while user hasn't picked to exit
        while option != 't' and option != 'm' and option != 'e':                #loop if user picked an option that is not available
            print("You have entered an ***invalid option***, please try again. Your three options are displayed below. \n")
            menu()
            option = str(input("Please enter your choice here: "))
        if option == 't':                           #use function text to morse code function
            abctmc()
        elif option == 'm':                         #use morse code to text function
            mctabc()
        menu()                                          #promt for user input after completing task
        option = str(input("Please enter your choice here: "))
    print("Thanks for using this program!") #farewell if they exit
main()
