from selenium import webdriver
from time import sleep
from secrets import phonenumber

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):

        self.driver.get("https://tinder.com")
        sleep(7)
        
        bt1 = self.driver.find_element_by_xpath("""//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[1]/button""")
        bt1.click()
        sleep()
        phone_in = self.driver.find_element_by_xpath("""//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input""")
        phone_in.send_keys(phonenumber)
        bt2 = self.driver.find_element_by_xpath("""//*[@id="modal-manager"]/div/div/div[2]/button""")
        bt2.click()
        sleep(15)

    def like(self):
        like_btn = self.driver.find_element_by_xpath("""//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]""")     
        like_btn.click()

    def close_popup(self):
        close_btn = self.driver.find_element_by_xpath("""//*[@id="modal-manager"]/div/div/div[2]/button[2]""")
        close_btn.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


    def loop(self):
        while True:
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()






bot = TinderBot()
bot.login()
bot.loop()
