import pygame

class Player:
    x = 0
    y = 0
    alive = True
    idle = True
    jump = False
    vel = 0
    rect = pygame.Rect(50, y, 50, 40)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_rect(self, rect):
        self.rect = rect

    def get_rect(self):
        return self.rect

    def set_jump(self, jump):
        self.jump = jump

    def get_jump(self):
        return self.jump

    def set_vel(self, vel):
        self.vel = vel

    def get_vel(self):
        return self.vel

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def set_idle(self, idle):
        self.idle = idle

    def get_idle(self):
        return self.idle


class Pipes():
    x = 0
    y = 0
    top_rect = pygame.Rect(0, 0, 0, 0)
    bot_rect = pygame.Rect(0, 0, 0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_top_rect(self, rect):
        self.top_rect = rect

    def get_top_rect(self):
        return self.top_rect
        
    def set_bot_rect(self, rect):
        self.bot_rect = rect

    def get_bot_rect(self):
        return self.bot_rect