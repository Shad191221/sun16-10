
#!welcome to dhanush's coffee shop....

name = input("enter your name :")
if name == 'dhanush' or name == 'Dhanush':
    print("Hello Boss ! make you way to the room your food will be on its way :)")
    menu1 = ['Lime tea','mint lime','falooda']
    print("Today your special items are ",menu1)
    order1 = input("What shall i order from these special items : ")
    for options in menu1:
        if order1 in menu1:
            print(f"Your {order1} will be sent soon Boss!")
        elif order1 not in menu1:
            print("Sorry,Boss we will find a way to arrange your request..")
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
    

