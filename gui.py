#!/usr/bin/env python3

import pyglet
from pyglet.gl import *
import random as R
import time

class GUI_Window(pyglet.window.Window):
    def __init__(self, game_class, agent_class, sleep_time=0, h_playable=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.GC = game_class # 2048 game class
        self.agent_class = agent_class # ml agent
        self.playable = h_playable

        if(sleep_time != 0):
            pyglet.clock.schedule_interval(self.update, sleep_time)

    def drawLine(self,sX,sY,eX,eY):
        glBegin(GL_LINES)
        glVertex2f(sX,sY)
        glVertex2f(eX,eY)
        glEnd()

    def drawText(self, text,sX,sY,size):
        label = pyglet.text.Label(str(text),
                                  font_size=size,
                                  x=sX,
                                  y=sY,
                                  anchor_x='center',
                                  anchor_y='center')
        label.draw()

    def drawSquare(self, sX,sY,size,color):
        glBegin(GL_QUADS)
        glColor3f(color[0],color[1],color[2])
        glVertex2f(sX,sY)
        glVertex2f(sX+size,sY)
        glVertex2f(sX+size,sY+size)
        glVertex2f(sX,sY+size)
        glEnd()

    def checkerBoard(self,size):
        win_size = self.get_size()[0]
        for i in range(self.GC.b_WH):
            self.drawLine(i*win_size//self.GC.b_WH , 0, i*win_size//self.GC.b_WH, win_size) #horizontal
            self.drawLine(0, i*win_size//self.GC.b_WH, win_size, i*win_size//self.GC.b_WH) #vertical

    def on_draw(self):
        self.clear()
        self.checkerBoard(50)
        #self.GC.print_board()

        win_size = self.get_size()[0]
        for y in range(self.GC.b_WH): #reversed - pyglet window left bottom 0:0
            for x in range(self.GC.b_WH):
                R = (self.GC.board[self.GC.b_WH-1 - y][x]/((2048.0/3.0)*1)) * 1
                G = (self.GC.board[self.GC.b_WH-1 - y][x]/((2048.0/3.0)*2)) * 1
                B = (self.GC.board[self.GC.b_WH-1 - y][x]/((2048.0/3.0)*3)) * 1

                self.drawSquare(sX = (win_size//self.GC.b_WH)*x, 
                                sY = (win_size//self.GC.b_WH)*y, 
                                size = win_size//self.GC.b_WH,
                                color = [R,G,B])
                self.drawText(text = str(self.GC.board[self.GC.b_WH-1 - y][x]), 
                              sX = win_size//(self.GC.b_WH*2) + (win_size//self.GC.b_WH)*x, 
                              sY = win_size//(self.GC.b_WH*2) + (win_size//self.GC.b_WH)*y, 
                              size = 30)

    def on_key_release(self, key, modifiers):
        """ PLAYABLE """
        if(self.playable):
            if(key == pyglet.window.key.NUM_2 or key == pyglet.window.key.S):
                self.GC.process_move(2)
            elif(key == pyglet.window.key.NUM_8 or key == pyglet.window.key.W):
                self.GC.process_move(8)
            elif(key == pyglet.window.key.NUM_6 or key == pyglet.window.key.D):
                self.GC.process_move(6)
            elif(key == pyglet.window.key.NUM_4 or key == pyglet.window.key.A):
                self.GC.process_move(4)
        pass

    def update(self, dt):
        pass


if __name__ == "__main__":
    window = GUI_Window("board", 800,800, "My Window", resizable=False)
    print(window.gameboard)
    pyglet.app.run()
