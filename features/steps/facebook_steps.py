from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
def before_scenario(context, scenario):
    options = Options()
    service = Service(context.chrome_driver_path)
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://facbook.com/login")
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_path = f"reports/screenshots/{scenario.name.replace(' ', '_')}.png"
        context.driver.save_screenshot(screenshot_path)
    context.driver.quit()

@given('The user is on the Facebook login page')
def step_given_user_on_facebook_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
    context.driver.get("https://www.facebook.com/")

@when('The user enters "{email}" in the email field')
def step_when_user_enters_email(context, email):
    email_field = context.driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys(email)

@when('The user enters {password} in the password field')
def step_when_user_enters_password(context, password):
    password_field = context.driver.find_element(By.ID, "pass")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)

@when('The user clicks the "{button_text}" button')
def step_when_user_clicks_button(context, button_text):
    button = context.driver.find_element(By.NAME, "login")
    button.click()

@then('The user should be redirected to the page {page}')
def step_then_user_redirected_to_homepage(context,page):
    assert page in context.driver.current_url, "Not redirected to homepage"
    time.sleep(3)

@then('An error message {error_message} should be displayed')
def step_then_error_message_displayed(context, error_message):
    try:
        # Initialisez une variable pour stocker l'élément trouvé (ou None si introuvable)
        error_element = None

        # Attendez jusqu'à ce que l'élément d'erreur devienne visible
        error_element = WebDriverWait(context.driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, '_9ay7'))
        )

        # Vérifiez si le message attendu est contenu dans le texte de l'élément trouvé
        assert error_message in error_element.text, (
            f"Le message d'erreur attendu '{error_message}' n'est pas affiché. "
            f"Message trouvé : '{error_element.text}'"
        )
    except Exception as e:
        # Gérer les exceptions de manière plus robuste
        found_message = error_element.text if error_element else "Aucun message trouvé"
        assert False, (
            f"Une erreur s'est produite : {e}. "
            f"Message d'erreur trouvé (le cas échéant) : '{found_message}'"
        )   