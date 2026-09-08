from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def click_7(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.google.android.calculator:id/digit_7"))
        ).click()

    def click_plus(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.google.android.calculator:id/op_add"))
        ).click()

    def click_5(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.google.android.calculator:id/digit_5"))
        ).click()

    def click_1(self):
        self.driver.find_element(By.ID, "com.google.android.calculator:id/digit_1").click()

    def click_equals(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.google.android.calculator:id/eq"))
        ).click()

    def get_result(self):
        return self.driver.find_element(
            By.ID,
            "com.google.android.calculator:id/result_final"
        ).text

    def click_minus(self):
        self.driver.find_element(By.ID, "com.google.android.calculator:id/op_sub").click()

    def click_multiply(self):
        self.driver.find_element(By.ID, "com.google.android.calculator:id/op_mul").click()

    def click_divide(self):
        self.driver.find_element(By.ID, "com.google.android.calculator:id/op_div").click()