import pandas
import pygame
import time
import keyboard
import consts
import pandas as pd


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
    keys = pygame.key.get_pressed()
    if keys[consts.ONE_KEY]:
        return consts.ONE_KEY
    elif keys[consts.TWO_KEY]:
        return consts.TWO_KEY
    elif keys[consts.THREE_KEY]:
        return consts.THREE_KEY
    elif keys[consts.FOUR_KEY]:
        return consts.FOUR_KEY
    elif keys[consts.FIVE_KEY]:
        return consts.FIVE_KEY
    elif keys[consts.SIX_KEY]:
        return consts.SIX_KEY
    elif keys[consts.SEVEN_KEY]:
        return consts.SEVEN_KEY
    elif keys[consts.EIGHT_KEY]:
        return consts.EIGHT_KEY
    elif keys[consts.NINE_KEY]:
        return consts.NINE_KEY
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


def what_time_key_pressed(key, data):
    if 1:
        detect_key(key)
        file = creating_cvs_file(data)
        put_data_in_chart(key, file)
        return -1
    if 2:
        detect_key(key)
        data_continue = opening_csv_file(key)
        return data_continue



def main_database(soldier_place, mines, grass, key_game):
    data = {
        "soldier_place": soldier_place,
        "mines": mines,
        "grass": grass
    }
    return what_time_key_pressed(key_game, data)