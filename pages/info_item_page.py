from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class InfoItemPage:
    BUTTON_ADD_TO_CART = Target.the("button to add an item to the cart").located_by((By.XPATH, "//a[@class='btn btn-success btn-lg']"))
    TITLE_ITEM = Target.the("Title of the item selected").located_by((By.XPATH, "//h2[@class='name']"))