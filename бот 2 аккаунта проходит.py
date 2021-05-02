# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from inspect import stack
#!/usr#!/usr/bin/env python3
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import webbrowser
import unittest
import multiprocessing
from multiprocessing import Process
import names
import random
#import socks
#from selenium.webdriver.chrome.options import Options
#import random
#  pastbin
#import schedule
#import datetime
#import pyautogui as pag
#from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options

t = 0
code = "2dkd145xjd" #z8zcqp49zv  3pv3zqbcyl u7oc85cd8d


options = Options()
options.binary_location ='\\chrome.exe'
brawser = webdriver.Chrome(chrome_options=options, executable_path=r"\chromedriver90.exe")

if (t == 0) :
    def jo():
        log = 'email'
        pas2 = 'password'
        as1 = "пароль" #пароль
        mail = "мыло" #мыло
        textarea1 = brawser.find_element_by_class_name(log)
        textarea1.send_keys(mail)
        textarea = brawser.find_element_by_class_name(pas2)
        textarea.send_keys(as1)
        time.sleep(1)
        submit = brawser.find_element_by_css_selector('body > main > section > section.top > div > div > div:nth-child(2) > div > div.login-wrapper.wrapper.bg-1 > button').click()
        time.sleep(3)


    def joj():
        log = 'email' #form-control
        pas2 = 'password'
        as1 = "12" #пароль
        mail = "мыло@iop" #мыло@i
        textarea1 = brawser.find_element_by_class_name(log)
        textarea1.send_keys(mail)
        textarea = brawser.find_element_by_class_name(pas2)
        textarea.send_keys(as1)
        submit = brawser.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button')
        submit.click()
        time.sleep(3)





    # Форма для ввода промокода
    def roll_func():
        textarea = brawser.find_element_by_class_name("form-control")
        textarea.send_keys(code)
        submit = brawser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[1]/div/div/span/button")
        submit.click()
        submit = brawser.find_element_by_xpath("/html/body / header / div / div[1] / nav / a / img").click()


    # Нажатие самой кнопки ролл
    def r():
        joj()
        time.sleep(4)
        #roll_func()функция для промокодов
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/main/div/div/div/div/div/div[5]/button"))).click()

        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable([By.XPATH,
                                        "/html/body/main/div/div/div/div/div/div[2]/div[1]/div"])).click()


    def ry():
        jo()
        time.sleep(4)
       # roll_func()# функция для промокодов
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "/html/body/main/div/div/div/div/div/div[5]/button"))).click()
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable([By.XPATH,
                                                                     "/html/body/main/div/div/div/div/div/div[2]/div[1]/div"])).click()

    def ri():
        log = 'email'  # form-control
        pas2 = 'password'
        as1 = "111111"  # 111111
        mail = "mail@mail.ru"  #
        textarea1 = brawser.find_element_by_class_name(log)
        textarea1.send_keys(mail)
        textarea = brawser.find_element_by_class_name(pas2)
        textarea.send_keys(as1)
        submit = brawser.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button')
        submit.click()
        time.sleep(3)
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "/html/body/main/div/div/div/div/div/div[5]/button"))).click()
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable([By.XPATH,
                                                                     "/html/body/main/div/div/div/div/div/div[2]/div[1]/div"])).click()

    def rpy():
        log = 'email'  # form-control
        pas2 = 'password'
        as1 = "пароль"  # 123457789
        mail = "мыло"  #
        textarea1 = brawser.find_element_by_class_name(log)
        textarea1.send_keys(mail)
        textarea = brawser.find_element_by_class_name(pas2)
        textarea.send_keys(as1)
        submit = brawser.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button')
        submit.click()
        time.sleep(3)
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "/html/body/main/div/div/div/div/div/div[5]/button"))).click()
        WebDriverWait(brawser, 10).until(EC.element_to_be_clickable([By.XPATH,
                                                                     "/html/body/main/div/div/div/div/div/div[2]/div[1]/div"])).click()


    def main():
        brawser.get("https://freesteam.io/")
        r()
        brawser.get("https://freebitcoin.io/")
        r()
        brawser.get("https://freenem.com/")
        r()
        brawser.get("https://freeusdcoin.com")
        r()
        brawser.get("https://freetether.com/")
        r()
        brawser.get("https://freechainlink.io/")
        r()
        brawser.get("https://freecardano.com/")
        r()
        # nen njhvjpbn
        brawser.get("https://free-tron.com/")
        r()
        brawser.get("https://freedash.io/")
        r()
        brawser.get("https://freeneo.io/")
        r()
        brawser.get("https://free-ltc.com/")
        r()
        brawser.get("https://free-doge.com")
        r()
        brawser.get("https://freebinancecoin.com")
        ri()

    def main2():
        brawser.get("https://free-ltc.com/")
        ry()
        brawser.get("https://freesteam.io/")
        ry()
        brawser.get("https://freebitcoin.io/")
        ry()
        brawser.get("https://freenem.com/")
        ry()
        brawser.get("https://freeusdcoin.com")
        ry()
        brawser.get("https://freetether.com/")
        ry()
        brawser.get("https://freechainlink.io/")
        ry()
        brawser.get("https://freecardano.com/")
        ry()
        # nen njhvjpbn
        brawser.get("https://free-tron.com/")
        ry()
        brawser.get("https://freedash.io/")
        ry()
        brawser.get("https://freeneo.io/")
        ry()
        brawser.get("https://freebinancecoin.com")
        rpy()
        brawser.get("https://free-doge.com")
        ry()




    def timeout():
        textarea = brawser.find_element_by_class_name("timeout-container")
        textareaq = brawser.find_element_by_class_name("digits")
        tro = textareaq.text
        print(tro)
        
    def exit():
        brawser.quit()



    try:
        while True:
            main()
            exit()
            brawser = brawser
            main2()
            exit()

            if __name__ == '__main__' :
                p1 = Process(name='Worker 1', target=main())
                p2 = Process(name='Worker 2', target=main2())

                p1.start()
                p2.start()

                p1.join()
                p2.join()
            time.sleep(3600)


    except Exception as e:
        print("exception:", e)
