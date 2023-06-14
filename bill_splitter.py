#Name: Gacamumakuba David
#reg: 221010521
#IT department
import random
num_friends = int(input("Enter the number of friends joining (including you):\n"))
friend_dit = {}
if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("enter the name of people joining the party")
    for friend in range(num_friends):
        name = input()
        friend_dit.update({name:0})
    bill = int(input("Enter the total bill value\n"))
    spilt_value = round(bill/num_friends,2)
    friend_dit={key: spilt_value for key in friend_dit}
    feature=input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No\n")
    if feature == 'Yes':
        luck_people = random.choice(list(friend_dit))
        print("%s is the lucky one!"%luck_people)
        spilt_value = round(bill/(num_friends-1),2)
        friend_dit ={key: spilt_value for key in friend_dit}
        friend_dit.update({luck_people:0})
        print(friend_dit)
    elif feature =='No':
        print("No one is going to be lucky")
        print(friend_dit)
    else:
        print("invalid input")
        
    
    
    
    
