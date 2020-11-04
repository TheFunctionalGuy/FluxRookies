from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://rkchals.fluxfingers.net/code/minefield.php')

    counter = 500
    found = False

    while not found:
        name_field = driver.find_element_by_css_selector('body > form:nth-child(2) > input:nth-child(2)')
        name_field.send_keys('m1LL1')
        name_field.submit()

        sleep(0.5)

        print(f'Now trying to click on bomb number {counter}')

        bomb = driver.find_element_by_css_selector(f'body > div > form > button:nth-child({counter})')
        bomb.click()

        try:
            sleep(0.5)
            elem = driver.find_element_by_css_selector('body > h1:nth-child(2)')

            if elem.text == 'BOOOM':
                found = False
                counter += 1

                driver.find_element_by_css_selector('body > a:nth-child(4)').click()
                sleep(0.5)
            else:
                found = True
        except NoSuchElementException:
            found = True

    print(f'Found dead bomb. It was bomb number: {counter}')

    input('Press enter to close...')
    driver.quit()
