import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urlparse2, random

class Linkedin(object):

    def __browser_factory(self):
        options = Options()
        options.binary_location = self.__chrome_dir
        return webdriver.Chrome(options=options)


    def __search_by(self, page):
        self.__browser.get("https://www.linkedin.com/search/results/people/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&page={}".format(self.__keyword, page))
        
    def __scroll_entry_page(self):
        pagedowns = 20
        page_body = self.__browser.find_element_by_tag_name("body")
        while pagedowns:
            page_body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            pagedowns-=1

    def __find_action_buttons(self, verbose=False):
        people_list = self.__browser.find_element_by_xpath('//ul[@class="search-results__list list-style-none mt2"]')
        people_buttons = people_list.find_elements_by_tag_name('button')
        if verbose:
            print("found: {} buttons".format(len(people_buttons)))
        return people_buttons

    # TODO: verify how can i return a condition
    def __is_connector_button(self, button):
        word_button = 'Connect'
        if self.__language is 'pt-br':
            word_button = 'Conecte-se'
        if word_button in button.get_attribute("aria-label"):
            return True
        return False
    
    def set_keyword(self, word):
        self.__keyword = word

    def set_chrome_dir(self, cdir):
        self.__chrome_dir = cdir

    def set_language(self, language):

        if language not in ['pt-br','en']:
            raise Exception('Only "pt-br" or "en" languages are accept')
        self.__language = language
        


    def login(self, email, password):
        self.__browser = self.__browser_factory()
        self.__browser.get('https://www.linkedin.com/uas/login')
        time.sleep(random.uniform(5,15))
        email_input = self.__browser.find_element_by_id('username')
        email_input.send_keys(email)
        password_input = self.__browser.find_element_by_id('password')
        password_input.send_keys(password)
        password_input.submit()

    def __send_invite(self):
        modal_element = self.__browser.find_element_by_class_name('send-invite__actions')
        invite_button = modal_element.find_element_by_xpath('//button[@class="button-primary-large ml1"]')
        invite_button.click()

    def crawller_it_on(self, page):
        self.__scroll_entry_page()

        self.__search_by(page)
        time.sleep(random.uniform(3,6))

        self.__scroll_entry_page()
        time.sleep(random.uniform(3,6))

        action_buttons = self.__find_action_buttons(verbose=True)
        len_buttons = len(action_buttons)-1
        for i in range(0, len_buttons):
            print(' -------------------- Page {} | Button {}/{} -------------------- '.format(page, i,len_buttons))
            try:
                if not self.__is_connector_button(action_buttons[i]):
                    print('its not a connector button')
                    continue

                time.sleep(random.uniform(5,10))
                action_buttons[i].click()

                time.sleep(random.uniform(3,6))
                self.__send_invite()
                
                print('User invited')
            except Exception as e: 
                print('Error: {}'.format(e))
                continue