#!/usr/bin/env python3

import gui
import game_2048 as G2048

import pyglet

import random
import sys

def argGet():
    args = sys.argv
    #DOCELA COOL, ALE ASI SE TO TAKHLE NEDĚLÁ :D
    if("--help" in args):
        print("{} help:".format(args[0]))
        print("              -h   human-playable")
        print("              -g   gui XXX -t tui")
        print()
        print("           dim=x   2048 board size")
        print("          seed=x   game seed")
        print("        scount=x   2048 number of starting tiles")
        quit()

    seed = random.randint(0,999999)
    try:
        seed = int([x.split("=")[1] for x in args if "seed" in x][0])
    except:
        pass

    dim = 4
    try:
        dim = int([x.split("=")[1] for x in args if "dim" in x][0])
    except:
        pass

    start_count = 3
    try:
        start_count = int([x.split("=")[1] for x in args if "scount" in x][0])
    except:
        pass

    return seed, dim, start_count

seed, dim, start_count = argGet()
game = G2048.gBoard(dim, start_count, seed)
#game.print_board()

GUI = gui.GUI_Window(game_class=game,
                     agent_class="agent",
                     sleep_time=0,
                     h_playable=True,
                     width=300,
                     height=300,
                     caption="2048")
pyglet.app.run()
