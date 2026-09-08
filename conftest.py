import os
os.makedirs("reports", exist_ok=True)
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.google.android.calculator"
    options.app_activity = "com.android.calculator2.Calculator"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        screenshot_path = os.path.join("reports", f"{item.name}.png")
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")