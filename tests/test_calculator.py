from pages.calculator_page import CalculatorPage

def test_addition(driver):

    calc = CalculatorPage(driver)

    calc.click_7()
    calc.click_plus()
    calc.click_5()
    calc.click_equals()

    result = calc.get_result()
    print(f"Calculator result: {result}")
    assert result == "12"
print("Running addition test")
def test_subtraction(driver):
    calc = CalculatorPage(driver)
    calc.click_7()
    calc.click_minus()
    calc.click_5()
    calc.click_equals()

    result = calc.get_result()
    print(f"Calculator result: {result}")
    assert result == "2"

def test_multiplication(driver):
    calc = CalculatorPage(driver)

    calc.click_7()
    calc.click_multiply()
    calc.click_5()
    calc.click_equals()

    result = calc.get_result()
    print(f"Calculator result: {result}")
    assert result == "35"

def test_division(driver):
    calc = CalculatorPage(driver)

    calc.click_7()
    calc.click_divide()
    calc.click_1()
    calc.click_equals()

    result = calc.get_result()
    print(f"Calculator result: {result}")
    assert result == "7"