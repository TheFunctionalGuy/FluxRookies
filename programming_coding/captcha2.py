from time import sleep

from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://rkchals.fluxfingers.net/code/captcha2.php')

    for _ in range(4):
        # Get captcha numbers
        captcha_form = driver.find_element_by_xpath('/html/body/form')
        captcha_number_1 = int(captcha_form.text.split()[7])
        operation = captcha_form.text.split()[8]
        captcha_number_2 = int(captcha_form.text.split()[9])

        # Calculate result
        if operation == '+':
            result = captcha_number_1 + captcha_number_2
        elif operation == '-':
            result = captcha_number_1 - captcha_number_2
        elif operation == '*':
            result = captcha_number_1 * captcha_number_2
        elif operation == '%':
            result = captcha_number_1 % captcha_number_2
        else:
            result = captcha_number_1 ^ captcha_number_2

        # Select checkbox
        checkbox = driver.find_element_by_id('id-flag')
        checkbox.click()

        # Insert right answer
        input_field = driver.find_element_by_xpath('/html/body/form/input[2]')
        input_field.send_keys(result)
        input_field.submit()
        submit_button = driver.find_element_by_xpath('/html/body/form/input[3]')

        sleep(1)

    sleep(20)
