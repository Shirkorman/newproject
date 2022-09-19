# import pandas
import time
import pygame.key
import keyboard
import pygame
import consts

def creating_cvs_file(key):
    pass

def put_data_in_chart(file):
    pass

def opening_cvs_file(key):
    pass

def continue_game():
    pass

def number_key_pressed(event, soldier_place, mines, grass):
    start_time = time.time()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == consts.ONE_KEY:
                running = False

        if event.type == KEYUP:
            if event.key == consts.ONE_KEY:
                key_A_pressed = False



