from screenpy import Actor
from screenpy_selenium.actions import Click

class DeleteItem:
    def __init__(self, delete_button):
        self.delete_button = delete_button
    
    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Click.on_the(self.delete_button)
        )
    
    