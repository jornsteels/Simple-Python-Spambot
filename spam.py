from pynput.keyboard import Key, Controller
import random
import time
import json
keyboard = Controller()
started = False #for repeatable script
stime = False #fallback for wrong value type in input
sbasic_information = False #for checking if the input is a valid type
start_random = False #for starting random method
scomfi = False #fallback for wrong mode in misc
shelp = False #for checking if input is valid with the exit help function
warning = False #for checking if input is valid with the 500 messages limit
word_list_used = [] #creating a list so there are no double words

instructions = """
****************************************************************************************************************
*                                                       INSTRUCTIONS:                                          *
*   step 1: choose one of the options you get                                                                  *
*   step 2: go to whatsapp web or other msging app on your pc                                                  *
*   step 3: click on the input box for a msg                                                                   *
*   step 4: wait till the timer hits 0                                                                         *
*   step 5: watch it spam                                                                                      *
*                                                                                                              *
****************************************************************************************************************
"""


help_txt = """
                    HELP

        normal spam mode:
            get to choose what to send and how many times.
            you can set an startmessage to let your friend/enemy know whats gonna happen

        random word spam mode:
            get to choose how many messages will be send, the words are completely random
            YOU DO NOT GET TO CHOOSE THESE

        [FAQ]:

            is there a limit?:
                well i have build in a limit but you can say yes to still go thru

            is my pc good enough for this?:
                depends on how manny messages you are gonna send

        for other questions:
            jopsteels@gmail.com
            +31 0610240195
"""

credits = """
                                            CREDITS:

                    creator: Jorn Staals
                    idea: Jorn Staals & Twitch chat
                    website: jorn.great-site.net/spambot


"""


options = """
            1. spam #choose one sentece or word to spam
            2. random #spam random words
            3. misc #for advanced users
            4. help #display some help info
            5. credits #display the credits
"""
#setting premade screens with info


def whitelines():
    i = 10
    while i > 0:
        print("\n")
        i -= 1
#10 whitelines



def warncheck():
    if times > 500:
        print("")
        print(
            "WARNING:above the 500 messages is not recomended for both parties.")
        dang = input("you still want to go thru? yes/no: ")
        if "yes" in dang:
            print("ok its your choice")
            time.sleep(2)
            print("\n\n\n\n")

        elif "no" in dang:
            print("ok good choice")
            exit()
            time.sleep(2)

        else:
            stime = False
            exit()



print(instructions)
print("\n\n\n\n")
#print the instructions

while (started == False):
    with open("misc/settings.json") as f:
      data = json.load(f)
    #opening settings.json

    print(options)
    mode_chooser = input("choose one option from above: ")
    #user input for mode


    if "spam" in mode_chooser or mode_chooser == "1":
        while (sbasic_information == False):
            print("")
            startmsg = input("what is your startmsg?(leave blank for none): ")
            spam_txt = input("wich word/sentence do you want to spam?: ")
            times = input("how many times do you want to send it?: ")
            wait_time = input("how much time before spamming?(in sec): ")
            #user input for time and times etc.

            try:#check if input is a int, if not throw an exception
                times = int(times)
                wait_time = int(wait_time)
                sbasic_information = True
            except ValueError:
                print("there was an error, the value you entert was not a number")
                print("please try again!")
                time.sleep(5)
                whitelines()
            except TypeError:
                print("thats not a number, please try a valid number!")
                time.sleep(5)
                whitelines()
                #letting user try again

        while (stime == False):#warning when messages are more than 500
            warncheck()

            print(f"you got {wait_time} seconds!")
            print(f"the victim will be spammed {times} times with \"{spam_txt}\"")
            time.sleep(2)
            print("\n\n")
        #info summary

            print("countdown starts now!")
            print("")

            print(f"{wait_time} seconds till spam", end='')
            while wait_time >= 0:
                print(f"\r{wait_time} seconds till spam", end='', flush=True)
                wait_time -= 1
                time.sleep(1)
            #started countdown

            print("starting now")
            if startmsg != "":
                keyboard.type(startmsg)
                keyboard.press(Key.enter)
                time.sleep(data["waitkey"])
                keyboard.release(Key.enter)
                times -= 1
            #startmsg sending

            print("\n\n\n")
            print(f"{times} more times!", end='')
            while times >= 1:
                keyboard.type(spam_txt)
                keyboard.press(Key.enter)
                time.sleep(data["waitkey"])
                keyboard.release(Key.enter)
                times -= 1
                print(f"\r{times} more times!", end='', flush=True)
            #spamming

            print("\n\n\n")
            keyboard.type("spam complete!")
            time.sleep(3)
            #letting user know that its done

            print("spam complete!, thnx for using this product")
            exit()
            #exiting script


    elif "random" in mode_chooser or mode_chooser == "2":

        while (start_random == False):
            times = input("\nhow many messages would you like to be send?: ")
            wait_time = input("how much time in seconds do you want before spamming: ")
            #getting basic input from user
            try:
                times = int(times)
                wait_time = int(wait_time)
                start_random = True
            except ValueError:
                print("that is not a valid amount! please try again")
                time.sleep(5)
                whitelines()
            except TypeError:
                print("that is not a number please try a valid number!")
                time.sleep(5)
                whitelines()
            #checking user input for valid value
            warncheck()
            #warning user


        print("\n\n")
        print(f"\r{wait_time} seconds till spam", end='')
        while wait_time >= 0:
            print(f"\r{wait_time} seconds till spam ", end='', flush=True)
            time.sleep(1)
            wait_time -= 1

        #wait_time

        wordlist_file = open("misc/wordlist.txt", "r")
        word_list = wordlist_file.readlines()

        #getting words from file

        print("\n\n\n")
        print("starting now!")
        print("\n\n")
        #letting user know that it started


        times -= 1
        #removing one time
        print(f"{times} more times!", end='')
        while times >= 0:
            snum = False
            #trying to get no double words

            while (snum == False):
                random_index = random.randint(1, 999)#generate random number
                random_word = word_list[random_index]#choosing random word out list
                random_word = random_word[:-1]#removing the \n rom the words, so only the word is used
                if random_word in word_list_used:
                    pass
                else:
                    snum = True
            #checking if word is already used


            word_list_used.append(random_word)
            #adding word to list so it can be checked

            keyboard.type(random_word)
            keyboard.press(Key.enter)
            time.sleep(data["waitkey"])
            keyboard.release(Key.enter)
            #sending the message

            print(f"\r{times} more times! ", end='', flush=True)
            #letting the user see how many times till done

            times -= 1

        print("\nspam is done!")
        #letting user know that its done
        exit()
        #exiting

    elif "misc" in mode_chooser or mode_chooser == "3":
        print("this mode is for advaced users")
        print("if you don't know what u are doing, please go back")
        while scomfi == False:
            sure = input("are you sure you want to go thru? Y/n: ")
            if ("y" in sure):
                scomfi = True
            elif ("n" in sure):
                print("alright")
                scomfi = True
            else:
                print("that is not a valid option, please try again!")
                whitelines()
                pass

        while (swaitkey != True):
            print("currently: " + data["waitkey"])
            waitkey_json = input("how much time between pressing enter in seconds?: ")
            if waitkey_json == "":
                waitkey_json = data["waitkey"]
            else:
                try:
                    waitkey_json = int(waitkey_json)
                    swaitkey = True
                except ValueError:
                    waitkey_json = data["waitkey"]
                    print("that is not a valid option, please try again")

        while (swarnlimit != True):
            print("\n\ncurrently: " + data["warnlimit"])
            warnlimit_json = input("how much messages before warning?: ")
            if warnlimit_json == "":
                warnlimit_json = data["warnlimit"]
            else:
                try:
                    warnlimit_json = int(warnlimit_json)
                    swarnlimit = True
                except ValueError:
                    warnlimit_json = data["warnlimit"]
                    print("that is not a valid option, please try again")


    elif "help" in mode_chooser or mode_chooser == "4":
        print("\n" + help_txt + "\n")
        #printing help

        answer = ""
        #removing the answer so you need to put in again

        while (shelp != True):
            leave_help = input("Type exit for leaving: ")
            if "yes" in leave_help:
                print("okay")
                shelp = True
                whitelines()
            elif leave_help == "e":
                print("okay")
                shelp = True
                whitelines()
            else:
                print("if you want to leave type exit\n")
                leave_help = ""
            #checking if they want to leave help


    elif "credits" in mode_chooser or mode_chooser == "5":
        print(f"\n {credits} \n")


    else:
        print("\nthat is not a valid answer, please try again")
        whitelines()
