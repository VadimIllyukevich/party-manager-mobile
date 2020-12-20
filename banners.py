from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import kivy.utils


class LabelButton(ButtonBehavior, Label):
    pass


class LikedUserEstablishmentBanner(GridLayout):
    def __init__(self, **kwargs):
        app = App.get_running_app()
        self.rows = 1
        super().__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#AB3C36")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        left = GridLayout()
        left.cols = 2
        left_image = Image(source='images/' + kwargs['photo_establishment'], size_hint=(1, 0.8),
                           pos_hint={'top': 1, 'left': 1})
        left_label = LabelButton(text=str(kwargs['descriptions']), font_size=20, size_hint=(1, 0.2),
                                 pos_hint={'top': 0.2, 'left': 1},
                                 on_press=lambda x: app.change_screen('establishment_page_window'),
                                 color=(0, 1, 0, 1), outline_color=(126 / 255, 5 / 255, 0 / 255, 1), outline_width=3)
        left.add_widget(left_image)
        left.add_widget(left_label)
        self.add_widget(left)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class EstablishmentBanner(GridLayout):

    def __init__(self, **kwargs):
        app = App.get_running_app()
        self.rows = 1
        super().__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#AB3C36")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        left = GridLayout()
        left.cols = 2
        left_image = Image(source='images/' + kwargs['photo'], size_hint=(1, 0.8),
                           pos_hint={'top': 1, 'left': 1})
        left_label = LabelButton(text=str(kwargs['name']), font_size=20, size_hint=(1, 0.2),
                                 pos_hint={'top': 0.2, 'left': 1},
                                 on_press=lambda x: print(app.change_screen('establishment_page_window')),
                                 color=(0, 1, 0, 1), outline_color=(126 / 255, 5 / 255, 0 / 255, 1), outline_width=3)
        left.add_widget(left_image)
        left.add_widget(left_label)
        self.add_widget(left)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class BoozeBanner(GridLayout):

    def __init__(self, **kwargs):
        app = App.get_running_app()
        self.rows = 1
        super().__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#AB3C36")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        left = GridLayout()
        left.cols = 2
        left_image = Image(source='images/' + kwargs['photo_booze'], size_hint=(1, 0.8),
                           pos_hint={'top': 1, 'left': 1})
        left_label = LabelButton(text=str(kwargs['descriptions']), font_size=20, size_hint=(1, 0.2),
                                 pos_hint={'top': 0.2, 'left': 1},
                                 on_press=lambda x: print(app.change_screen('booze_page_window')),
                                 color=(0, 1, 0, 1), outline_color=(126 / 255, 5 / 255, 0 / 255, 1), outline_width=3)
        left.add_widget(left_image)
        left.add_widget(left_label)
        self.add_widget(left)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class SnackBanner(GridLayout):

    def __init__(self, **kwargs):
        app = App.get_running_app()
        self.rows = 1
        super().__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#AB3C36")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        left = GridLayout()
        left.cols = 2
        left_image = Image(source='images/' + kwargs['photo_booze'], size_hint=(1, 0.8),
                           pos_hint={'top': 1, 'left': 1})
        left_label = LabelButton(text=str(kwargs['descriptions']), font_size=20, size_hint=(1, 0.2),
                                 pos_hint={'top': 0.2, 'left': 1},
                                 on_press=lambda x: print(app.change_screen('booze_page_window')),
                                 color=(0, 1, 0, 1), outline_color=(126 / 255, 5 / 255, 0 / 255, 1), outline_width=3)
        left.add_widget(left_image)
        left.add_widget(left_label)
        self.add_widget(left)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
