import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
         arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY,
          arcade.color.GREEN, arcade.color.LIGHT_BLUE,
          arcade.color.LIGHT_PINK, arcade.color.LIGHT_YELLOW,
          arcade.color.MEDIUM_BLUE, arcade.color.MEDIUM_RED_VIOLET]


class Cercle:
    def __init__(self, rayon, center_x, center_y, color):
        self.rayon = rayon
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []

    def setup(self):
        for _ in range(20):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            self.liste_cercles.append(Cercle(rayon, center_x, center_y, color))

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for cercle in self.liste_cercles:
                if cercle.center_x - cercle.rayon <= x <= cercle.center_x + cercle.rayon and cercle.center_y - cercle.rayon <= y <= cercle.center_y + cercle.rayon:
                    self.liste_cercles.remove(cercle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            for cercle in self.liste_cercles:
                if cercle.center_x - cercle.rayon <= x <= cercle.center_x + cercle.rayon and cercle.center_y - cercle.rayon <= y <= cercle.center_y + cercle.rayon:
                    cercle.color = random.choice(COLORS)


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
