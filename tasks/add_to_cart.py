from screenpy import Actor, Eventually
from screenpy_selenium.actions import Click, Wait, AcceptAlert
from pages.info_item_page import InfoItemPage

class AddItemToCart:
    def __init__(self):
        pass
    
    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Wait.for_the(InfoItemPage.BUTTON_ADD_TO_CART).to_appear(),
            Click.on(InfoItemPage.BUTTON_ADD_TO_CART),
            Eventually(AcceptAlert())
        )