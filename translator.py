import shelve
import sys
import time

creole = shelve.open('perm_dict.py')

count = 0
while True:
    count += 1
    def redefine():
        ifDelete = input('\nWhat word would you like to delete from the dictionary?')
        ifDelete = ifDelete.lower()
        ifDelete = ifDelete.strip()
        if ifDelete.isdigit() == True:
            print('Please enter the word again.  It looks like you typed in a number.')
            redefine()
            
        elif ifDelete == '':
            print("'  ' is not a word... idiot.")
            redefine()
            
        elif ifDelete in creole:
            del creole[ifDelete]
            print(ifDelete + ' has been deleted.')
            ifDelete = input('Would you like to delete any other words?')
            ifDelete = ifDelete.lower()
            ifDelete = ifDelete.strip()
            if ifDelete == 'yes' or ifDelete == 'y':
                redefine()
                        
        else:
            print('\nSorry, ' + ifDelete + ' is not in the dictionary yet.')
            redefine()
            
    def flow(count):
        if count > 1:
            time.sleep(2)
            more = input("\nWould you like to translate any other words?")
            more = more.strip()
            more = more.lower()
            if more == 'yes' or more == 'y':
                main()
            elif more == 'no' or more == 'n':
                sure = input('Would you like to delete any words from the Creole Dictionary?')
                sure == sure.lower()
                if sure == 'no':
                    print("""Ok, have a great rest of your day!
    Haitian Translator will shutdown automatically in 5 seconds""")
                    creole.close()
                    time.sleep(5)
                    sys.exit()

                elif sure == 'yes' or sure == 'y':
                    redefine()
        else:
            pass
        
    flow(count)
    
    def main():
        
        def addWord(word):
            addDef = input("What is the Haitian Creole word for " + str(word) + '?')
            addDef = addDef.strip()
            addDef = addDef.lower()
            creole[str(word)] = str(addDef)
            print('In Haitian Creole: '+ str(word) +' = '+ addDef)
            
        def notIn(phrase):
            choice = input("""Sorry, """ + str(phrase.upper()) + """ hasn't been entered into the dictionary yet.
    Would you like to enter """ + str(phrase.upper()) + """ into the dictionary?
    Please type in yes or no.""")
            choice = choice.lower()
            choice = choice.strip()
            if choice == 'yes' or choice == 'y':
                print('OK! Lets add that new word!')
                addWord(phrase)
            elif choice == 'no' or choice == 'n':
                choice = input('Did you enter the word incorectly?')
                choice = choice.lower()
                choice = choice.strip()
                if choice == 'yes' or choice == 'y':
                    translate()
                else:
                    flow(2)
                    
        def translate():
            phrase = input('\nWhat would you like to translate into Haitian Creole?')
            phrase = phrase.strip()
            phrase = phrase.lower()
            punctuation = ''
            if phrase == 'q':
                phrase = input('Would you like to exit the program?')
                phrase = phrase.strip()
                phrase = phrase.lower()
                if phrase == 'yes' or phrase == 'y':
                    sys.exit()
                elif phrase == 'no' or phrase == 'n':
                    translate()
            if len(phrase) > 0:                
                if phrase[-1] == '.' or phrase[-1] == '!' or phrase[-1] == '?':
                    punctuation = phrase[-1]
                    phrase = phrase.replace(phrase[-1], '')
                for i in phrase:
                    if i.isalpha() == True:
                        pass
                    elif i == ' ':
                        pass
                    else:
                        phrase = phrase.replace(i, '')
            else:
                translate()
            phrase = phrase.split(' ')
            sentence = ''            
            for i in phrase:
                word = i
                if i in creole and creole[i] == ' ':
                    print(i + ' was already in the dict as a blank value. ' + i + ' has now been deleted.')
                    del creole[i]
                    
                elif i in creole:
                    sentence += creole[i] + ' '
                                        
                else:
                    notIn(word)
            sentence = sentence.strip()
            sentence = sentence + punctuation
            print(sentence)            
        translate()        
    main()
