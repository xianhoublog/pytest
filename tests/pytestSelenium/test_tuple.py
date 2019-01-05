from selenium import webdriver
import  pytest


@pytest.fixture()
def test_setup():
    global driver

    driver = webdriver.Chrome(executable_path="C:/Users/nduan/TAF/selenium/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    print("test completed")


def test_login(test_setup):
    driver.get("http://google.com")
    driver.find_element_by_name("q").send_keys("test")
    driver.find_element_by_name("btnK")
