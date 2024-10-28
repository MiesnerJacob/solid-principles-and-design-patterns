import pygame
from pygame.locals import *
import math
import time


class Graphic:
    def render(self, surface):
        pass

    def move(self, dx, dy):
        pass

class Circle(Graphic):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Rectangle(Graphic):
    def __init__(self, center_x, center_y, width, length, color, angle=0):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.length = length
        self.color = color
        self.angle = angle

    def render(self, surface):
        end_x = self.center_x + math.cos(math.radians(self.angle)) * self.length
        end_y = self.center_y - math.sin(math.radians(self.angle)) * self.length
        pygame.draw.line(surface, self.color, (self.center_x, self.center_y), (end_x, end_y), self.width)

    def move(self, dx, dy):
        self.center_x += dx
        self.center_y += dy

    def set_angle(self, angle):
        self.angle = angle

class Group(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def render(self, surface):
        for child in self.children:
            child.render(surface)

    def move(self, dx, dy):
        for child in self.children:
            child.move(dx, dy)

def create_clock_face(group, center_x, center_y, radius, color):
    for hour in range(12):
        angle = (2 * math.pi / 12) * hour
        x = center_x + int(math.cos(angle) * radius)
        y = center_y + int(math.sin(angle) * radius)
        group.add(Circle(x, y, 10, color))

def update_clock_hands(hour_hand, minute_hand, second_hand):
    current_time = time.localtime()
    hour = current_time.tm_hour % 12 + current_time.tm_min / 60
    minute = current_time.tm_min + current_time.tm_sec / 60
    second = current_time.tm_sec

    hour_hand.set_angle(-360 * hour / 12 + 90)
    minute_hand.set_angle(-360 * minute / 60 + 90)
    second_hand.set_angle(-360 * second / 60 + 90)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Smooth Draggable Clock')
clock = pygame.time.Clock()

clock_group = Group()
create_clock_face(clock_group, 400, 300, 150, (255, 255, 255))  # White circles for hours
hour_hand = Rectangle(400, 300, 5, 100, (255, 0, 0), 0)  # Red hour hand
minute_hand = Rectangle(400, 300, 3, 140, (0, 255, 0), 0)  # Green minute hand
second_hand = Rectangle(400, 300, 1, 160, (255, 255, 255), 0)  # White second hand
clock_group.add(hour_hand)
clock_group.add(minute_hand)
clock_group.add(second_hand)

dragging = False
last_mouse_pos = (0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            dragging = True
            last_mouse_pos = event.pos

        elif event.type == MOUSEBUTTONUP:
            dragging = False

        elif event.type == MOUSEMOTION and dragging:
            current_mouse_pos = event.pos
            dx = current_mouse_pos[0] - last_mouse_pos[0]
            dy = current_mouse_pos[1] - last_mouse_pos[1]
            clock_group.move(dx, dy)
            last_mouse_pos = current_mouse_pos

    if not dragging:
        update_clock_hands(hour_hand, minute_hand, second_hand)

    screen.fill((0, 0, 0))
    clock_group.render(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
