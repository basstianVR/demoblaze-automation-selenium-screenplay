from screenpy import Actor
from screenpy_selenium.actions import Click, Wait, AcceptAlert, Pause
from pages.home_page import HomePage
from pages.info_item_page import InfoItemPage

class AddItemToCart:
    def __init__(self,name_item):
        self.name_item = name_item
    
    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Click.on(HomePage.ITEM_BY_NAME(self.name_item)),
            Wait.for_the(InfoItemPage.BUTTON_ADD_TO_CART).to_appear(),
            Click.on(InfoItemPage.BUTTON_ADD_TO_CART),
            Pause.for_(2).seconds_because("Waiting for the alert"),
            AcceptAlert()
        )