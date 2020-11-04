from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://rkchals.fluxfingers.net/code/captcha.php')

    # Get captcha numbers
    captcha_form = driver.find_element_by_xpath('/html/body/form')
    captcha_number_1 = captcha_form.text.split()[7]
    captcha_number_2 = captcha_form.text.split()[9]

    # Calculate result
    result = int(captcha_number_1) + int(captcha_number_2)

    # Select checkbox
    checkbox = driver.find_element_by_id('id-flag')
    checkbox.click()

    # Insert right answer
    input_field = driver.find_element_by_xpath('/html/body/form/input[2]')
    input_field.send_keys(result)
    input_field.submit()
    submit_button = driver.find_element_by_xpath('/html/body/form/input[3]')
