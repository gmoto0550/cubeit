from playwright.sync_api import Page,expect
BASE_URL='http://127.0.0.1:8000/cube.html'
input_number = 10
cube = input_number*input_number*input_number
def test_cube(page:Page):
    page.goto(BASE_URL)
    input_field=page.get_by_placeholder("Enter a number")
    input_field.fill(str(input_number))
    calculate_button=page.get_by_role("button",name="Calculate Cube")
    calculate_button.click()
    result=page.locator("div#result")
    expect(result).to_contain_text(f"Cube of {input_number} is {cube}")
def test_empty_input(page:Page):
    page.goto(BASE_URL)
    calculate_button=page.get_by_role("button",name="Calculate Cube")
    calculate_button.click()
    result=page.locator("div#result")
    expect(result).to_contain_text("Enter a number")



    