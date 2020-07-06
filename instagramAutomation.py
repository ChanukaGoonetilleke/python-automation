from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get('https://www.instagram.com')
        sleep(2)
        login = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        login.send_keys(username)

        password = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        password.send_keys(pw)

        loginButton = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
        loginButton.click()
        sleep(2)

        notNowButton = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        notNowButton.click()
        sleep(4)

        notifButton = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notifButton.click()
        sleep(2)
    
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")\
        .click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")\
        .click()
        sleep(2)
        following = self._get_names()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")\
        .click()
        sleep(2)
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht,ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        close = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
        close.click()
        sleep(2)
        return names

my_bot = InstaBot('chan_goonetilleke', '29merchantsgate')
my_bot.get_unfollowers()