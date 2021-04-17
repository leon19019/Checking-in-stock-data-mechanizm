from selenium import webdriver
from telegram.ext import Updater, CommandHandler
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
import telegram_send


def get_is_in_stock_data(url = "https://www.computeruniverse.net/ru/asrock-barebone-4x4-box-v1000m-cpu-v1605b-5xusb2xdphdmi", class_name = "div.product-stock__delivery-text"):

    firefox_options = Options()
    firefox_options.add_argument("--headless")

    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=firefox_options)

    browser.get(url)
    time.sleep(2)

    a = browser.find_element_by_css_selector(class_name).text

    telegram_send.send(messages = [a])


    browser.close()


    return


get_is_in_stock_data()

