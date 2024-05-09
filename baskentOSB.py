from sifre import Passw
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("https://www.baskentosb.org/tr/firmalar/")
browser.maximize_window()
mailAdresleri = []
time.sleep(5)
def sayfaKaydir(_sayfaKaydirmaParametresi):
    denememXPATHIM = f'//*[@id="bosb-page-wrapper"]/div/div/div/div/div[3]/div[{i}]/div/div/div[3]/div/div[3]/span[2]/a'
    denemeXPATH = browser.find_element(By.XPATH,denememXPATHIM) 
    try:
        print("sayfa scroll ediliyor . . .")
        time.sleep(1)
        browser.execute_script("arguments[0].scrollIntoView();",denemeXPATH)
        print("Sayfa Scroll Edildi . . .")
        time.sleep(1)
    except:
        print("scroll edilemedi X X X X")
    denememXPATHIM = f'//*[@id="bosb-page-wrapper"]/div/div/div/div/div[3]/div[{i + 10}]/div/div/div[3]/div/div[3]/span[2]/a'
    denemeXPATH = browser.find_element(By.XPATH,denememXPATHIM) 
    try:
        print("sayfa scroll ediliyor . . .")
        time.sleep(1)
        browser.execute_script("arguments[0].scrollIntoView();",denemeXPATH)
        print("Sayfa Scroll Edildi . . .")
        time.sleep(1)
    except:
        print("scroll edilemedi X X X X")

for i in range(1,445):
    time.sleep(1)
    # if i % 10 == 0:
    #     sayfaKaydir(i)
    try:
        aTAGXPATH = f'//*[@id="bosb-page-wrapper"]/div/div/div/div/div[3]/div[{i}]/div/div/div[3]/div/div[3]/span[2]/a'
        time.sleep(1)
        emailTag = browser.find_element(By.XPATH, aTAGXPATH)
        href = emailTag.get_attribute("href")
        print(href)
        mailAdresleri.append(href)
    except:
        print("Mail Adresi Bulunamadi")
def mailto_sil(email_list):
    cleaned_emails = []
    for email in email_list:
        if email.startswith("mailto:"):
            cleaned_emails.append(email[7:])
        else:
            cleaned_emails.append(email)
    return cleaned_emails
cleaned_emails = mailto_sil(mailAdresleri)
import pandas as pd
def listToDataFrame3(_mailList):
    df1 = pd.DataFrame(_mailList, columns=["Mail Listesi"])
    print(df1)
    with pd.ExcelWriter(r"BaskentOSBMail.xlsx") as writer:
        df1.to_excel(writer, sheet_name="mailList")
print(cleaned_emails)
listToDataFrame3(cleaned_emails)

browser.close()
