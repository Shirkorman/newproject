# import pandas
import pygame
import keyboard
import consts

from tkinter import *
import sys
import time
global count
count =0

dict = {
   consts.ONE_KEY: '',
    consts.TWO_KEY: '',
    consts.THREE_KEY: '',
    consts.FOUR_KEY: '',
    consts.FIVE_KEY: '',
    consts.SIX_KEY: '',
    consts.SEVEN_KEY: '',
    consts.EIGHT_KEY: '',
    consts.NINE_KEY: ''
}

def detect_key(key):
    keys = pygame.key.get_pressed()
    if keys[consts.ONE_KEY]:
        return consts.ONE_KEY
    if keys[consts.TWO_KEY]:
        return consts.TWO_KEY
    if keys[consts.THREE_KEY]:
        return consts.THREE_KEY
    if keys[consts.FOUR_KEY]:
        return consts.FOUR_KEY
    if keys[consts.FIVE_KEY]:
        return consts.FIVE_KEY
    if keys[consts.SIX_KEY]:
        return consts.SIX_KEY
    if keys[consts.SEVEN_KEY]:
        return consts.SEVEN_KEY
    if keys[consts.EIGHT_KEY]:
        return consts.EIGHT_KEY
    if keys[consts.NINE_KEY]:
        return consts.NINE_KEY
    return 0

def what_time_key_pressed(key):
    pass


def creating_cvs_file(key):
    pass


def put_data_in_chart(file):
    pass


def opening_cvs_file(key):
    pass


def continue_game():
    pass


# def main_database(event, soldier_place, mines, grass):



def start_time(event):
    start = time.time()

    return end - start

def end_time(event):
    if event.type == pygame.KEYUP:
        return time.time()
    return False

def is_less_than_sec(event):
    end = time.time()
    if event.type == pygame.KEYUP:
        end = time.time()
        return end



