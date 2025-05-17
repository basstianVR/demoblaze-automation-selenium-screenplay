from screenpy import Actor
from screenpy_selenium.actions import Click, Pause
from pages.home_page import HomePage

class SelectItem:
    def __init__(self, name_item):
        self.name_item = name_item
    
    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Click.on(HomePage.ITEM_BY_NAME(self.name_item))
        )