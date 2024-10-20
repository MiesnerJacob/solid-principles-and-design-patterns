# Uses Adapter Design Pattern
import pygame

class InputAdapter:
    def __init__(self, game):
        self.game = game
        self.dragging_slider = False

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_button = self.game.renderer.get_clicked_button(pos)
                if clicked_button == "start":
                    self.game.start()
                elif clicked_button == "pause":
                    self.game.pause()
                elif clicked_button == "restart":
                    self.game.restart()
                elif clicked_button == "slider":
                    self.dragging_slider = True
                elif clicked_button == "change_style":
                    self.game.change_style()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging_slider = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging_slider:
                    new_speed = self.game.renderer.update_slider(event.pos[0])
                    self.game.set_speed(new_speed)
            elif event.type == pygame.QUIT:
                return False
        return True
