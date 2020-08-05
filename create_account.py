import requests
from driving import Driving
from tokenizer import Tokenizer
import random
import names
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime

init(autoreset=True)


dateTimeObj = datetime.now()
finalCount = int(input(Fore.CYAN + '[{}] How many accounts do you want to create: \n'.format(str(dateTimeObj))))
domain = input(Fore.CYAN + '[{}] Please enter your catchall domain, e.g. pengbroadbands.co.uk: \n'.format(str(dateTimeObj)))
password = input(Fore.CYAN + '[{}] Please enter the password you would like to set for all accounts: \n'.format(str(dateTimeObj)))

counter = 0

while counter < finalCount:
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Getting Cookies'.format(str(dateTimeObj)))
    myDriver = Driving()
    cookie = myDriver.getCookie()

    print(Fore.YELLOW + '[{}] Time to get the captcha token'.format(str(dateTimeObj)))
    getToken = Tokenizer()
    captcha = getToken.captchaSend()

    token = captcha['token']
    qtext = captcha['text']
    url = captcha['asset']


    myDriver.changeURL(url)
    solution = input(Fore.CYAN + '[{}] {}: '.format(str(dateTimeObj), qtext))
    print(Fore.GREEN + '[{}] Got token, closing browser'.format(str(dateTimeObj)))
    myDriver.closeDriver()



    payload = {"token": token,
    "solution": solution}

    if getToken.solution(payload) == 200:
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'Host': 'www.net-a-porter.com',
            'Origin': 'https://www.net-a-porter.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cookie': cookie
        }

        cookies = {
            'Cookie': cookie
        }

        birthDay = str(random.randint(1, 30))
        birthMonth = str(random.randint(1, 12))
        firstName = names.get_first_name()
        lastName = names.get_last_name()
        email = '{}.{}{}@{}'.format(firstName, lastName, birthDay, domain)

        dateTimeObj = datetime.now()
        print(Fore.YELLOW + '[{}] Prepping payload for {}'.format(str(dateTimeObj), email))

        payload = 'birthDay={}&birthMonth={}&captchaToken={}&confirmEmail={}&country=GB&email={}&firstName={}&lastName={}&optOutOfMailList=false&password={}'.format(birthDay, birthMonth, token, email, email, firstName, lastName, password)

        if getToken.register(headers, cookies, payload) == 200:
            with open('accounts.txt', 'a') as f:
                f.write('{} \n'.format(email))
                f.close()
            counter +=1
            dateTimeObj = datetime.now()
            print(Fore.GREEN + '[{}] Successfully created {}'.format(str(dateTimeObj), email))
        else:
            dateTimeObj = datetime.now()
            print(Fore.RED + '[{}] Failed to create account'.format(str(dateTimeObj)))
    else:
        pass
