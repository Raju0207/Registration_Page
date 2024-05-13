from pages.base_page import Base_Page
from locators.locators import Locators
from validate_email import validate_email


class Registration_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def enter_first_name(self, firstname):
        self.enter_at(self.locator.firstName, firstname)

    def enter_last_name(self):
        self.get_element(self.locator.lastName)

    def enter_address(self):
        self.get_element(self.locator.address)

    def enter_email(self):
        self.get_element(self.locator.emailAddress)

    def is_valid_email(self):
        return validate_email(self)

    email = "example@example.com"
    if is_valid_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")

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
