from pages.base_page import Base_Page
from locators.locators import Locators


class Registration_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def select_male(self):
        self.click_element(self.locator.maleRadioButton)

    def select_female(self):
        self.click_element(self.locator.feMaleRadioButton)

    def is_male_radio_button_selected(self):
        return self.is_selected(self.locator.maleRadioButton)

    def is_female_radio_button_selected(self):
        return self.is_selected(self.locator.feMaleRadioButton)

    def select_cricket(self):
        self.click_element(self.locator.cricket)

    def is_cricket_checkbox_selected(self):
        return self.is_selected(self.locator.cricket)

    def select_movies(self):
        self.click_element(self.locator.movies)

    def is_movies_checkbox_selected(self):
        return self.is_selected(self.locator.movies)

    def select_hockey(self):
        self.click_element(self.locator.hockey)

    def is_hockey_checkbox_selected(self):
        return self.is_selected(self.locator.hockey)
