"""
File Name: adventure_game.py
Creator: Ammon Jones
Purpose: Create a game that is depended on the response of the player.
"""
# Libraries needed to complete the task:
import time
# Functions needed to complete the task:

# Constants needed to complete the task:

# Info needed from user to complete the task:
print('To play the game please enter the following:')
your_name = input('What is your name? ')
# Formulas needed to complete the task:

#The Game
choice = input(f'You are snowboarding by yourself up in the mountains and it starts to get dark.\n You have the choice to HIKE up and do one more run or head HOME? You hear your Moms voice in your head saying: {your_name} you know what I would want you to do.\n Type "hike" to do another run or "home" to go back home like you know your Mom would want you to do: ')
if choice.lower() == 'hike':
    print('Your Mom is not happy with your decision! You should know better!')
    choice = input('You hiked up to the top of the mountain and you are now snowboarding down the mountain. You cant see\nvery well but there is a drop off up ahead. Should you JUMP off of it or go AROUND? ')
    if choice.lower() == 'jump':
        print('Your Mom is real unhappy with you now!')
        choice = input('Right before going off of the drop you decide to attempt a double backflip, you fly through the air \n one flip, two flip, stomp it! You are soo pumped you shred down to the bottom with amazing pow turns \nand when you get to the bottom you want to celibrate. What do you do to celibrate? Call all of your FRIENDS to brag, go get a burrito from RANCHERITOS, or do BOTH by inviting your friends to rancheritos and then \nbragging about what you did while eating a delicous burrito at midnight? ')
        if choice.lower() == 'friends':
            print('That is a good choice but why put or between two good things?')
        elif choice.lower() == 'rancheritos':
            print('That is a good choice but why put or between two good things?')
        elif choice.lower() == 'both':
            print('You go to rancheritos cuz you hungry and your friends meet you there, it taste soo freaking good but even better because \n you are soo much better and cooler than your friends and they think you are sooo rad!')
            time.sleep(120)
        else:
            print('Ehh who care what you think that you are going to do, \nwe all know that you are smart enough to find a way to get your friends to come to rancheritos with you so \nthat you can enjoy a burrito togther while you tell them how amazing you are!')
    elif choice.lower() == 'around':
        choice = input('Last minute you swerve around the drop off, and crash into a tree well. You are stuck upsidedown in a tree well \nShould you try and WIGGLE yourself free or reach for your PHONE in your pocket and call for help? ')
        if choice.lower() == 'wiggle':
            print('You wiggle until you fall sideways and are able to reach and undo your snowboard bindings and get free!')
        elif choice.lower() == 'phone':
            print('While trying to get your phone out of your pocket you loose hold of it and it falls below you into the snow. \nYou cant reach it and end up trying to become unstuck but the blood rushes to your head so you passout, get hypothermia, and eventually die. ')
        else:
            print("If you don't make a choice in life time will make the decision for you! You just sat in the cold, got hypothermia, and died!")
    else:
        print("If you don't make a choice in life time will make the decision for you! You just sat in the cold, got hypothermia, and died!")
elif choice.lower() == 'home':
    print('Your Mom is proud of you!')
    choice = input("You're in your car driving home and it's past your CURFEW but your FRIENDS want to hangout. What do you choose? ")
    if choice.lower() == 'friends':
        choice = input('Your friends call you on your way and tell you to meet at rancheritos to get a burrito\nbecause they have something to tell you, do you go? YES or NO? ')
        if choice.lower() == 'yes':
            print('You meet them at rancheritos and realize that you are so lame becasue they were also just snowboarding they landed\na double backflip and you didnt!')
        elif choice.lower() == 'no':
            print('You go home, your mom is asleep and you regret it because you could have stayed up snowboarding or hanging out with your friends!')
        else:
            print('Make up your mind dude!!! Or else time will make the decision for you!!!')
    elif choice.lower() == 'curfew':
        choice = input('You decide to drive home to make your mom happy, but once you get there she makes you do the chores\nthat you didnt do becasue you left them to go\nsnowboarding... Do you do your CHORES or go to your room and SLEEP?')
        if choice.lower() == 'chores':
            print('Wow what a boring choice')
        elif choice.lower() == 'sleep':
            print('Good choice you deserve it after an amazing day of shredding!')
            time.sleep(120)
        else:
            print('Dummy you are wasting precious sleep time! Go to bed so that you can get up early and shred tomorrow!')
    else:
        print('Come on you now that hanging out with your friends will be way more fun then going home! Go hangout with them!\nMaybe you can go get a burrito or something!')
else:
    print("If you don't make a choice in life time will make the decision for you! You just sat in the cold, got hypothermia, and died!")

