import time
import pygame

def main():
    play_mp3("./static/music/song.wav")
    pygame.mixer.music.play(-1)

    minimum = {0:5, 1:15, 2:40, 3:10}
    importance = {0:4, 1:3, 2:14, 3:3}
    names = {0:"Willing Power", 1:"Allah", 2:"Finance", 3:"Body"}
    user_time  = get_digit("Enter a time that you want to dedicate in a minute format above 5 minute: ", 5)
    importance = missions(importance, minimum, user_time )
    extra()
    display(names, importance)
    work(importance, names)

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def work(importance, names):
    """last_task = list(importance.keys())[-1] 
    input("Press Enter to start your real work: ")
    for key in importance.keys():
        print(f"Now It is time to work on {names[key]}...")
        input(f"When you feel comfortable press Enter to start your work for {importance[key]} minutes : ")
        timer(importance[key])
        if key != last_task:
            resting()
    print("You Successfully managed to finish one full cycle. I am proud of you. ")"""
 
    input("Press Enter to start your real work: ")
    while importance:
        key = list(importance.keys())[0]
        value = importance.pop(key)
        print(f"Now It is time to work on {names[key]}...")
        input(f"When you feel comfortable press Enter to start your work for {value} minutes : ")
        timer(value)
        if importance:
            resting()
    print("You Successfully managed to finish one full cycle. I am proud of you. ")

def get_digit(text, bot, top=-1):
    while True:
        digit = input(text)
        if digit.isdigit():
            digit = int(digit)
            if digit < bot:
                    print(f"input needs to be above or equal to {bot}")
            else:
                if top != -1:
                    if digit > top:
                        print(f"input needs to be below or equal to {top}") 
                    else: 
                        return digit
                else: 
                    return digit                     
        else:
            print("You entered not integer value. Time must be in a minute format")
def timer(_minute):
    second = _minute * 60
    while second > 0:
        minute = second // 60
        print(f"{minute:02}:{second - minute * 60:02}", end="\r")
        time.sleep(1)
        second -= 1

def missions(dict, minimum, user_time ):
    print("Here is your priorities. Please read and type the option that you are worst now.\n")
    answer = get_digit("0. Willing Power [0]\n1. Allah         [1]\n2.a) Finance     [2]\n2.b) Body        [3]\nOption: ", 0, 3)

    if user_time  > 70:  
        dict[answer] *= 2
        total = 0
        for value in dict.values():
            total += value
        user_time  = round(user_time  / total)
        for key in dict.keys():
            dict[key] *= user_time 
        return dict
    else:
        for key in list(minimum.keys()):
            if user_time  >= minimum[key]:
                user_time  -= minimum[key]
            else:
                del minimum[key]
        user_time  = round(user_time  / len(minimum))
        for key in minimum.keys():
            minimum[key] += user_time 
        return minimum

def resting():
    user_time  = get_digit("Determine Resting Time, minimum is 1 minutes: ", 1)
    print("Now You are Resting...")
    timer(user_time )
    input("Time is up press Enter to continue with the other task: ")

def extra():
    if get_digit("Is there any extra work? 0 for No, 1 for Yes: ", 0, 1) == 1:
        user_time  = get_digit("Enter a time that you want to dedicate in a minute format to extra work: ", 1)
        input("Press Enter to start your extra work: ")
        print(f"Now It is time to work on extra work...")
        timer(user_time )
        resting()

def display(names, dict):
    i = 1
    print("\nWORK SCHEDULE\n------------------------------------------")
    for key in dict.keys():
        print(f"|{i}. {names[key]} for {dict[key]} minutes  |")
        i += 1
    print("------------------------------------------")
    
 
if __name__ == "__main__":
    main()