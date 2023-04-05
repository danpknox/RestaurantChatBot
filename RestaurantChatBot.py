#menu
menu = ["Coffee", "Cookie", "Brownie", "Croissant"]
#available reservation times
reservation_times = ["5:00 pm", "6:00 pm", "7:00 pm"]

#print options available to users 
def print_options():
    print("\nWelcome to The Bakery! \nHow can I help you? \n1. Take a look at the menu. \n2. Ask about daily specials. \n3. Make a reservation. \n4. Order take out. \n5. Exit.")

dailyspecial = "Chocolate Cake"

#print menu
def print_menu():
    print (menu)
    
#print daily special
def daily_specials():
    print(f"Today's daily special is {dailyspecial}!")
    
#make a reservation
def reservation():
    z = False
    #while loop that runs and asks for time until user enters either a valid time or exits
    while not z:
        x = input(f"The available times are {reservation_times} What time would you like? Type 'none' if none ")
        if x in reservation_times:
            print(f"You are all set for {x}")
            #remove time entered from list of available reservation times
            reservation_times.remove(x)
            z = True
        elif x == "none":
            z = True
        else:
            print("Not available")
            
            
            
            
              
#order takeout
def takeout():
    #create a list to store user's order
    order = []
    z = False
    #while loop that runs and asks for food item until user is done with order
    while not z:
        i = input(f"Our menu consists of {menu} and our daily special is {dailyspecial} What would you like? Type 'done' when done ")
        if i in menu or i == dailyspecial:
            print(f"{i} has been added to your order!")
            order.append(i)
        elif i == "done":
            z = True
            print (f"Your order consists of {order}")
        else:
            print("Not available")
#exit
def exit():
    print("Thanks for visiting!")
    
#dictionary to assign different numbers to different functions    
actions = { 1: print_menu, 
            2: daily_specials, 
            3: reservation, 
            4: takeout, 
            5: exit }

print_options()
choice = int(input())
#execute whichever function that matches user input corresponding to the dictionary
actions[choice]()
#while loop that runs until user enters 5 to exit
while (choice !=5):
    print_options()
    choice = int(input())
    actions[choice]()
