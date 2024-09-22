from abc import ABC, abstractmethod
import pygame
import pygame_gui
from moviepy.editor import *
import pygame_gui

class WidgetRenderer(ABC):
    abstractmethod
    def render(self, screen, ui_manager) -> str:
        pass

class ImageRenderer(WidgetRenderer):
    def __init__(self, image_path, size=None):
        self.image_path = image_path
        self.image = None
        self.size = size

    def load_image(self):
        self.image = pygame.image.load(self.image_path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def render(self, screen, ui_manager):
        if not self.image:
            self.load_image()
        screen.blit(self.image, (200, 70))
        return "Rendering an image", None

class VideoRenderer(WidgetRenderer):
    def __init__(self, video_path, size=None):
        self.video_path = video_path
        self.clip = None
        self.playing = False
        self.start_time = 0
        self.size = size

    def load_movie(self):
        self.clip = VideoFileClip(self.video_path)
        if self.size:
            self.clip = self.clip.resize(self.size)

    def render(self, screen, ui_manager):
        if not self.clip:
            self.load_movie()
        current_time = pygame.time.get_ticks() / 1000
        if not self.playing:
            self.playing = True
            self.start_time = current_time

        if self.playing:
            elapsed_time = current_time - self.start_time
            if elapsed_time < self.clip.duration:
                frame = self.clip.get_frame(elapsed_time)
                frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                screen.blit(frame, (200, 70))
            else:
                self.playing = False
        return "Rendering a video", None

    def stop(self):
        self.playing = False

class FormRenderer(WidgetRenderer):
    def __init__(self):
        self.form_elements = []
        self.panel = None

    def create_form(self, ui_manager):
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((300, 60), (260, 480)),
            manager=ui_manager,
            object_id="form_panel",
            anchors={"left": "left",
                     "right": "right",
                     "top": "top",
                     "bottom": "bottom"}
        )
        
        self.form_elements.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 10), (200, 40)),
                                                                text="First Name",
                                                                manager=ui_manager,
                                                                container=self.panel))
        self.form_elements.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((30, 50), (200, 40)),
                                                                       manager=ui_manager,
                                                                       container=self.panel))
        self.form_elements.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 110), (200, 40)),
                                                                text="Last Name",
                                                                manager=ui_manager,
                                                                container=self.panel))
        self.form_elements.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((30, 150), (200, 40)),
                                                                       manager=ui_manager,
                                                                       container=self.panel))
        self.form_elements.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 210), (200, 40)),
                                                                text="Phone Number",
                                                                manager=ui_manager,
                                                                container=self.panel))
        self.form_elements.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((30, 250), (200, 40)),
                                                                       manager=ui_manager,
                                                                       container=self.panel))
        self.form_elements.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 310), (200, 40)),
                                                                text="Email Address",
                                                                manager=ui_manager,
                                                                container=self.panel))
        self.form_elements.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((30, 350), (200, 40)),
                                                                       manager=ui_manager,
                                                                       container=self.panel))
        self.form_elements.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 410), (100, 40)),
                                                                text="Submit",
                                                                manager=ui_manager,
                                                                container=self.panel))

    def render(self, screen, ui_manager):
        if not self.form_elements:
            self.create_form(ui_manager)

        return "Rendering a form", None

    def clear_form(self):
        for element in self.form_elements:
            element.kill()
        self.form_elements = []
        if self.panel:
            self.panel.kill()
            self.panel = None

class RenderingContext:
    def __init__(self, renderer: WidgetRenderer):
        self._renderer = renderer

    def set_renderer(self, renderer: WidgetRenderer):
        self._renderer = renderer

    def render(self, screen, ui_manager):
        return self._renderer.render(screen, ui_manager)

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Renderer Strategy Pattern Example")
    ui_manager = pygame_gui.UIManager((800, 600))

    context = RenderingContext(ImageRenderer("./resources/python_design_patterns.png", size=(550, 325)))

    image_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (100, 40)),
                                                text="Image",
                                                manager=ui_manager)
    video_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 70), (100, 40)),
                                                text="Video",
                                                manager=ui_manager)
    widget_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 120), (100, 40)),
                                                text="Widget",
                                                manager=ui_manager)

    rendered_widget = None

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isinstance(context._renderer, FormRenderer):
                        context._renderer.clear_form()
                    if event.ui_element == image_button:
                        context.set_renderer(ImageRenderer("./resources/python_design_patterns.png", size=(550, 325)))
                    elif event.ui_element == video_button:
                        context.set_renderer(VideoRenderer("./resources/example_video.mp4", size=(550, 325)))
                    elif event.ui_element == widget_button:
                        context.set_renderer(FormRenderer())

            ui_manager.process_events(event)

        screen.fill((200, 200, 200))
        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)

        result_text, widget = context.render(screen, ui_manager)

        font = pygame.font.Font(None, 36)
        text = font.render(result_text, 1, (10, 10, 10))
        screen.blit(text, (300, 20))

        if rendered_widget:
            rendered_widget.kill()
        if widget:
            rendered_widget = widget

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
