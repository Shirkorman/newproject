import pandas
import pygame
import time
import keyboard
import consts
import pandas as pd
from pynput import keyboard

START = False
STOP = False
dict = {
   consts.ONE_KEY: {},
    consts.TWO_KEY: {},
    consts.THREE_KEY: {},
    consts.FOUR_KEY: {},
    consts.FIVE_KEY: {},
    consts.SIX_KEY: {},
    consts.SEVEN_KEY: {},
    consts.EIGHT_KEY: {},
    consts.NINE_KEY: {}
}

def detect_key(key):
    if key[consts.ONE_KEY]:
        return 0
    elif key[consts.TWO_KEY]:
        return 1
    elif key[consts.THREE_KEY]:
        return 2
    elif key[consts.FOUR_KEY]:
        return 3
    elif key[consts.FIVE_KEY]:
        return 4
    elif key[consts.SIX_KEY]:
        return 5
    elif key[consts.SEVEN_KEY]:
        return 6
    elif key[consts.EIGHT_KEY]:
        return 7
    elif key[consts.NINE_KEY]:
        return 8
    else:
        return False


def creating_cvs_file(data):
    df = pd.DataFrame.from_dict(data)
    df.to_csv(r'test8.csv', index=False, header=True)
    return df

def put_data_in_chart(key, file):
    dict[key] = file


def opening_csv_file(key):
    df = pd.read_csv(dict[key])
    data_continue = {
        "soldier_place": df[0],
        "mines": df[1],
        "grass": df[2]
    }
    return data_continue


def what_time_key_pressed(key, data, time):
    key1 = detect_key(key)
    if time < 1.0:
        file = creating_cvs_file(data)
        put_data_in_chart(key1, file)
        return -1
    else:
        data_continue = opening_csv_file(key1)
        return data_continue



def main_database(soldier_place, mines, grass, key_game, time):
    data = {
        "soldier_place": soldier_place,
        "mines": mines,
        "grass": grass
    }
    return what_time_key_pressed(key_game, data, time)

def show_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("Time: {0}:{1}:{2}".format(int(hours), int(minutes), int(seconds)))

def check_reboot(STOP, START):
    if STOP == True and START == True:
        STOP = False
        START = False
    return STOP, START

def end(STOP, event, start_time = None):
    if STOP == False and event.type == pygame.KEYUP:
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_lapsed = time_lapsed % 60
        show_time(time_lapsed)
        return end_time, True

def start(START):
    if START == False:
        start_time = time.time()
        return start_time, True




