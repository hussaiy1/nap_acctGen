from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class Driving(object):
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get('https://www.net-a-porter.com/gb/en/')

    def getCookie(self):
        cookies = self.driver.get_cookies()
        cookie = ''
        for i in range(len(cookies)):
            if cookies[i]['name'] == 'bm_sz' or cookies[i]['name'] == '_abck':
                cookie += '{name}={value}; '.format(
                    name=cookies[i]['name'],
                    value=cookies[i]['value']
                )
        return cookie

    def changeURL(self, url):
        self.driver.get(url)
    
    def closeDriver(self):
        self.driver.close()