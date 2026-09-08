from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time
options = UiAutomator2Options()
options.platform_name="Android"
options.device_name="Android"
options.automation_name="uiautomator2"
options.app_package="com.google.android.calculator"
options.app_activity="com.android.calculator2.Calculator" 
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"7").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"plus").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"5").click()                                                                                                     
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"equals").click()
result = driver.find_element(By.ID, "com.google.android.calculator:id/result_final").text
assert result == "12", f"Expected 12, got {result}"
print("Test Passed: 7 + 5 = 12")
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"7").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"minus").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"5").click()                                                                                                     
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"equals").click()
result = driver.find_element(By.ID, "com.google.android.calculator:id/result_final").text
assert result == "2", f"Expected 2, got {result}"
print("Test Passed: 7 - 5 = 2")
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"7").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"multiply").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"5").click()                                                                                                     
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"equals").click()
result = driver.find_element(By.ID, "com.google.android.calculator:id/result_final").text
assert result == "35", f"Expected 35, got {result}"
print("Test Passed: 7 * 5 = 35")
time.sleep(2)
driver.quit()

