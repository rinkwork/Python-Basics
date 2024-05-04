#       if condition:
#           do this 
#       else:
#           do this

#       if condition:
#           do this
#       elif: 
#           do this 
#       else:
#           do this

num = input('Enter Value = ')
if int(num) % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

# Case Statement 

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.") #default option