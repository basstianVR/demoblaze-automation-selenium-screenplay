from screenpy import Actor
from screenpy_selenium.actions import Click
from pages.navbar import NavBar

class GoToCart:
    def __init__(self):
        pass

    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Click.on(NavBar.CART_BUTTON)
        )
        