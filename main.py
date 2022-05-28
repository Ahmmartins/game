print('''
_ // / _
/ o    \ /
> ))_. / \
    <
''')

print("welcome to the finding memo")
print("your mission is to find where memo is")
choice_1 = input(" you are to go to his house, where do you want to go? type 'left' or 'right'").lower()
if choice_1 == 'left':
    choice_2 = input("you are at his  house, type 'F' to enter through the front or type 'B' to go through the back")
    if choice_2 == 'F':
        choice_3 = input(" correct. so which room do you think memo is ? 'A' or 'B'?")
        if choice_3 == 'B':
            choice_4 =input("correct. now finally where in the room do you think he is. type 'U' for under the bed or type 'O' for ontop the wardrobe")
            if choice_4 == 'o':
                print( "you have found memo. you win 50 thousand dollars cash price")
            else:print("you almost got it but you lost")

        else:
            print("sorry you lost the game")
    else:
        print("game over. you passed the wrong place")
else:
    print("you are wrong,game over")



