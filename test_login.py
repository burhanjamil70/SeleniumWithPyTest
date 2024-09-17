
import pytest
from selenium.common import NoSuchElementException

from main import setup, teardown
from selenium.webdriver.common.by import By
url = "http://practice.automationtesting.in/"


def test_login_with_valid_username_and_password():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("burhan.jamil50@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Qwerty7@1234")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    actual_logout_ext = driver.find_element(By.LINK_TEXT, "Logout").text
    assert "Logout" == actual_logout_ext
    teardown(driver)

def test_login_with_invalid_username_and_password():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("burhan.jamil5000000@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Qwerty7@1234777")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
    assert "Error:" == error.find_element(By.TAG_NAME, "Strong").text
    teardown(driver)


def test_login_with_valid_username_and_empty_password():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("burhan.jamil50@gmail.com")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
    assert error.text.__contains__("Password is required")
    teardown(driver)


def test_login_with_empty_username_and_valid_password():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("Qwerty7@1234")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
    assert error.text.__contains__(".Username is required")
    teardown(driver)

@pytest.mark.xfail
def test_login_with_empty_username_and_empty_password():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
    assert error.text.__contains__("Username is required")
    teardown(driver)


@pytest.mark.xfail
def test_login_password_should_be_masked():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("123456")
    assert "passwords" == password_field.get_attribute("type")
    teardown(driver)


@pytest.mark.skip
def test_login_with_case_changed():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("Burhan.jamil50@gmail.com")
    driver.find_element(By.ID, "password").send_keys("qwerty7@1234")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    error_label = driver.find_element(By.TAG_NAME, "Strong").text
    assert "Error:" == error_label
    teardown(driver)

def test_login_with_authentication():
    driver = setup()
    driver.get(url=url)
    driver.find_element(By.LINK_TEXT, 'My Account').click()
    driver.find_element(By.ID, "username").send_keys("burhan.jamil50@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Qwerty7@1234")
    driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    driver.back()
    try:
        driver.find_element(By.LINK_TEXT, "Logout")
        assert False
    except NoSuchElementException as e:
        assert True
    teardown(driver)