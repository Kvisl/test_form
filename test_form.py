from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()  # Создание объекта ChromeOptions, если нужны доп. опции
    service = Service(ChromeDriverManager().install())  # Установка драйвера с помощью Service
    driver = webdriver.Chrome(service=service, options=options)  # Передача service и options отдельно
    driver.maximize_window()
    yield driver
    driver.quit()


def test_example(driver):
    driver.get("https://demoqa.com/automation-practice-form")


    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Doe")


    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("john.doe@example.com")


    gender = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
    gender.click()


    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")


    date_of_birth_input = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth_input.click()


    date_of_birth_input.clear()
    date_of_birth_input.send_keys("4 sep 1904")
    date_of_birth_input.send_keys("\n")  # Нажатие Enter для закрытия календаря


    subjects_input = driver.find_element(By.CSS_SELECTOR, "#subjectsInput")
    subjects_input.send_keys("Maths")
    subjects_input.send_keys("\n")


    hobbies = driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]")
    hobbies.click()


    picture_upload = driver.find_element(By.ID, "uploadPicture")
    picture_upload.send_keys("/home/dog/Загрузки/0_0.jpg")


    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("1234 Elm Street")


    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys("NCR")
    state.send_keys("\n")

    city = driver.find_element(By.CSS_SELECTOR, "#react-select-4-input")
    city.send_keys("Delhi")
    city.send_keys("\n")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

