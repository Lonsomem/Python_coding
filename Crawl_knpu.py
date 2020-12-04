from selenium import webdriver
import requests
from bs4 import BeautifulSoup

path = "D:/python-coding/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttp%253A%252F%252Ftop.cafe.daum.net%252F')
assert "카카오계정" in driver.title
assert "No results found." not in driver.page_source
emailid = driver.find_element_by_name("email")
emailid.clear()
emailid.send_keys("hclee0730@gmail.com")
pw = driver.find_element_by_name("password")
pw.clear()
pw.send_keys("1234asdf")
driver.find_element_by_css_selector("button.btn_g.btn_confirm.submit").click()
assert "No results found." not in driver.page_source
n = 2
t = 1
while "NO results found." not in driver.page_source:
    driver.get("http://cafe.daum.net/knpuarchive/IDfT/{}".format(n))
    assert "No results found." not in driver.page_source
    driver.implicitly_wait(3)
    driver.switch_to.frame('down')
    webpage = driver.page_source
    soup = BeautifulSoup(webpage, "html.parser") 

    f = open("D:/python-coding/files/textfile{}.txt".format(t), 'w', encoding='utf-8')
    f.close()
    f = open("D:/python-coding/files/textfile{}.txt".format(t), 'a', encoding='utf-8')

    t += 1

    while True:    
        titles = soup.select('#user_contents > p:nth-child(%d)'%(n))
        if titles != []:
            if titles[0].get_text() == '':
                break
            else:
                f.write(titles[0].get_text())
                n += 1
        else:
            break
    f.close()