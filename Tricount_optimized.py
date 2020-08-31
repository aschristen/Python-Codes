def verify_amounts_input(list_of_amounts):
    while True:
        try:
            list_of_amounts=[float(amount) for amount in list_of_amounts]
            break
        except: 
            print("Your input is wrong.")
            amounts=input ('Provide the amount of money that each of them disposes ' \
        'in the same order and separated by commas')
            list_of_amounts=amounts.split(",")
    return list_of_amounts

def create_list_friends_amounts ():
    
    friends=input('Provide the names of your travel buddies separated by commas')

    list_of_friends=friends.split(",")
    
    amounts=input ('Provide the amount of money that each of them disposes ' \
        'in the same order and separated by commas')

    list_of_amounts=verify_amounts_input(amounts.split(","))
   

    while (len(list_of_friends)!=len(list_of_amounts)):

        print("The number of buddies should be equal to the number of amounts of money. Input for each of your buddies an amount of money (s)he disposes " \
            "and separate by commas ")

        friends=input('Provide the names of your travel buddies separated by commas')
        list_of_friends=friends.split(",")
        
        amounts=input ('Provide the amount of money that each of them disposes ' \
                        'in the same order and separated by commas') 

        list_of_amounts=verify_amounts_input(amounts.split(","))

    else:
        friends_and_amounts=[(friend,amount) for friend, amount in zip(list_of_friends, list_of_amounts)]
        total_budget=sum([amount for _,amount in friends_and_amounts])

        print(friends_and_amounts)
        print("The total budget for the trip is {}".format(total_budget))

        for friend,amount in zip(list_of_friends, list_of_amounts):
             share_to_pay=total_budget/len(friends_and_amounts)
             balance_member=amount-share_to_pay
             
             if(balance_member<0):
                 print("{} owes still {:.2f}".format(friend,-balance_member))
             elif(balance_member>0):
                 print("{} has to receive {:.2f}".format(friend, balance_member))
             else:
                 print("The budget of {} is balanced ".format(friend))


create_list_friends_amounts()
 

