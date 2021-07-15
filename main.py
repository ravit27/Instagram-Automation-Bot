from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import urllib
import os
import requests
from bs4 import BeautifulSoup
from time import sleep
import wget


class Instabot:
    def __init__(self,username,password):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(8)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hellooooooooo")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div[1]/div[2]").click()
        sleep(3)

        url = 'https://instagram.fixc4-1.fna.fbcdn.net/v/t51.2885-15/e35/152838756_716076835770556_8251087165423181980_n.jpg?tp=1&_nc_ht=instagram.fixc4-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=iY791jXYGxIAX--7I5K&ccb=7-4&oh=77c79084fea28e79092c0e0c24e77cff&oe=60879677&_nc_sid=4f375e'
        wget.download(url, 'ravit1.jpg')
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").click()
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys("Niceeeee")
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/button/div").click()
        sleep(3)

        url = 'https://instagram.fixc4-1.fna.fbcdn.net/v/t51.2885-15/e35/152142057_193072439000714_1637663903873367160_n.jpg?tp=1&_nc_ht=instagram.fixc4-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=PsbyNJGRvpoAX_j2oSe&ccb=7-4&oh=4fd629dfeb6ae3ffe293be083253b533&oe=6088A11E&_nc_sid=4f375e'
        wget.download(url, 'ravit2.jpg')
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/button[2]/div").click()
        sleep(3)

        url = 'https://instagram.fixc4-1.fna.fbcdn.net/v/t51.2885-15/e35/152459871_776887549877451_2163586117600752914_n.jpg?tp=1&_nc_ht=instagram.fixc4-1.fna.fbcdn.net&_nc_cat=103&_nc_ohc=i9tBVDnjjFUAX9RUaEj&ccb=7-4&oh=ba30494e56efc803f157b4103fac9ddf&oe=6087BB9C&_nc_sid=4f375e'
        wget.download(url, 'ravit3.jpg')
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/button[2]/div").click()
        sleep(3)

        url = 'https://instagram.fixc4-1.fna.fbcdn.net/v/t51.2885-15/e35/152503706_385895859507245_7748363756536644828_n.jpg?tp=1&_nc_ht=instagram.fixc4-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=m8WaQUXWuFMAX-Gra3d&ccb=7-4&oh=ba971046df9d3d2a606e855c214b8766&oe=608614D2&_nc_sid=4f375e'
        wget.download(url, 'ravit4.jpg')
        sleep(3)



    def searchHashtag(self, hashtag):

        self.driver.get('https://www.instagram.com/explore/tags/' + hashtag)

    def followlikePhotos(self, amount):
        self.driver.find_element_by_class_name('eLAPa').click()
        i = 0
        while i < amount:
        	sleep(5)
        	like = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        	self.driver.execute_script("arguments[0].click();", like)
        	button = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
        	self.driver.execute_script("arguments[0].click();", button)
        	sleep(3)
        	self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        	i += 1
        self.driver.close()

    

def main():
   login=Instabot('demoacc_rg','sneha@2001') 
   login.searchHashtag('cars')
   login.followlikePhotos(5)


main()
