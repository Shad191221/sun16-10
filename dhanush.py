
#!welcome to dhanush's coffee shop

name = input("enter your name :")
if name == 'dhanush' or name == 'Dhanush':
    print("Hello sir ! make you way to the room your food is on the way :)")
else:
    print(f"Greeting {name} welcome to Dhanush's Coffee Shop")
    menu = ['masala tea','Cappucchino','Latte','Black coffee']
    print("Today we are serving",menu)
    order = input("What to order sir ?")
    for options in menu:
        if order in menu:
            print(f"Your order {order} is on the way . ")
        else :
            print ("Sorry,not avialable in the menu..")
    

