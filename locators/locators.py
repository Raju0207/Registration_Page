from selenium.webdriver.common.by import By


class Locators:
    # Locators for Login
    userName = (By.ID, 'user-name')
    password = (By.ID, 'password')
    submitButton = (By.ID, 'login-button')
    swagLabsText = By.XPATH, '//div[@class ="app_logo"]'
    burgerMenu = By.ID, 'react-burger-menu-btn'
    logoutButton = By.ID, 'logout_sidebar_link'
    userName1 = (By.ID, 'user-name')
    password1 = (By.ID, 'password')
    TextMessage = By.XPATH, '//h3'
    userName2 = (By.ID, 'user-name')
    password2 = (By.ID, 'password')

    # Locators for Registration
    firstName = By.XPATH, '(//input[@placeholder= "First Name"])'
    lastName = By.XPATH, '(//input[@placeholder= "Last Name"])'
    address = By.XPATH, '(//textarea[@class="form-control ng-pristine ng-valid ng-touched"])'
    emailAddress = By.XPATH, '(//input[@type="email"])'
    phone = By.XPATH, '(//input[@type="tel"])'
    maleRadioButton = By.XPATH, '(//input[@name="radiooptions"])[1]'
    feMaleRadioButton = By.XPATH, '(//input[@name="radiooptions"])[2]'

    cricket = By.ID, 'checkbox1'
    movies = By.ID, 'checkbox2'
    hockey = By.ID, 'checkbox3'

