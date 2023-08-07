import re

mText = input("\nEnter the main text : ")

while 1:
    print("\n\n 1:to check that a string contains only a certain set of characters(in this case a-z, A-Z and 0-9)")
    print("2:that matches a string that has an a followed by zero or more b's")
    print("3:that matches a string that has an a followed by zero or one 'b'")
    print("4:to find the sequences of one upper case letter followed by lower case letters")
    print("5:to search for numbers (0-9) of length between 1 and 3 in a given string\n 6: to terminate\n\n")
    
    ch = int(input("Enter your choice: "))
    if ch==1:
        sChar = input("\nEnter the characters to be searched : ")
        res = re.findall(f"[{sChar}]", mText)
        if res:
            print("\nThe following characters from ", "'", sChar, "'", "found in ", "'", mText, "'")
            print(res)
        else:
            print("Characters NOT found")
    elif ch==2:  # ii.	that matches a string that has an a followed by zero or more b's.
        res = re.search('ab*', mText)
        if res:
            print("\nString",res.group(),"is found in",mText,"at ",res.span())   
        else:
            print("\nString NOT found")
    elif ch==3: # iii.	that matches a string that has an a followed by zero or one 'b'
        res = re.search('ab?', mText)
        if res:
            print("\nString",res.group(),"is found in",mText,"at ",res.span())  
        else:
            print("\nString NOT found")
        
    elif ch==4: # iv.	to find the sequences of one upper case letter followed by lower case letters.
        res = re.findall('[A-Z]+[a-z]+', mText)
        if res:
            print("\n[A-Z]+[a-z]+ is found in ", mText, )
            print(res)
        else:
            print("\nString NOT found")
    
    elif ch==5:# v.	to search for numbers (0-9) of length between 1 and 3 in a given string.\
        res = re.findall('[0-9]{1,3}', mText)
        if res:
            print("\n[0-9]{1,3} is found in ", mText, )
            print(res)  
        else:
            print("\nString NOT found")
    else:
        break
    ch=input("Do u want to re-enter the mainstring[y/n]")
    if ch=='y':
        mText = input("\nEnter the main text : ")

    
print("Good Bye")
  
