import time
import pygame
import keyboard
import random

timestamps = {
    '00:00': 0,
    '05:37': 337,
    '10:54': 654,
    '12:13': 733,
    '16:15': 975,
    '21:10': 1270,
    '26:40': 1600,
    '28:18': 1698,
    '38:40': 2320,
    '41:38': 2498,
    '43:24': 2604,
    '50:29': 3029,
    '54:13': 3253,
    '59:23': 3563
}
menu_music_path = "./static/music/play_list.mp3"
def main():
    play_mp3(menu_music_path ,-1, timestamps)
    minimum = {0:15, 1:5, 2:40, 3:10}
    importance = {0:3, 1:4, 2:14, 3:3}
    names = {0:"Allah", 1:"Willing Power", 2:"Finance", 3:"Body"}
    user_time  = get_digit("Enter a time that you want to dedicate in a minute format above 5 minute: ", 5)
    importance = missions(importance, minimum, user_time, names )
    extra()
    display(names, importance)
    work(importance, names)

def play_mp3(file_path, number_of_play, time_stamps):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    starting = random.choice(list(time_stamps.keys()))
    pygame.mixer.music.play(number_of_play)
    if pygame.mixer.music.get_busy(): 
        pygame.mixer.music.set_pos(time_stamps[starting])
   
    

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
        if pygame.mixer.music.get_busy():  # Check if music is currently playing
            pygame.mixer.music.stop()
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
    print("Press and hold 's' to stop")
    while second > 0:
        minute = second // 60
        print(f"{minute:02}:{second - minute * 60:02}", end="\r")
        if keyboard.is_pressed('s'):
            break
        time.sleep(1)
        second -= 1
        

def missions(dict, minimum, user_time, names ):
    for name in names:
        print(f"{name}. {names[name]}   [{name}]")
    answer = get_digit("Here is your priorities. Please read and type the option that you are worst now: ", 0, 3)
    
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
    play_mp3(menu_music_path ,-1, timestamps)
    user_time  = get_digit("Determine Resting Time, minimum is 1 minutes: ", 1)
    print("Now You are Resting...")
    timer(user_time )
    input("Time is up press Enter to continue with the other task: ")

def extra():
    if get_digit("Is there any extra work? 0 for No, 1 for Yes: ", 0, 1) == 1:
        user_time  = get_digit("Enter a time that you want to dedicate in a minute format to extra work: ", 1)
        input("Press Enter to start your extra work: ")
        print(f"Now It is time to work on extra work...")
        if pygame.mixer.music.get_busy():  # Check if music is currently playing
            pygame.mixer.music.stop()
        timer(user_time)
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