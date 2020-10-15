from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.douban.com')
time.sleep(1)

# print(browser.find_element_by_tag_name('iframe'))  # selenium.webdriver.remote.webelement.WebElement
# # browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
# browser.switch_to.frame()

# 只有出现 elements 都是返回 elements。其余都是可以确定的一个值，否则 NoSuchElementException 报错。
# iframe = driver.find_elements_by_tag_name("iframe")  # 返回列表，这里有一个元素。return list of WebElement
# print(len(iframe))

# 切换到 iframe，iframe 相当于一个新的页面
# 用frame的index来定位，第一个是0。Switches focus to the specified frame, by index, name, or webelement.
# driver.switch_to.frame(0)
# button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
# button.click()
#
# # xpath：//* 选取文档中的所有元素。
# # driver.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
# driver.find_element_by_id('username').send_keys('15055495@qq.com')  # return WebElement
# driver.find_element_by_id('password').send_keys('test123test456')
# time.sleep(1)
#
# # 多属性建议使用 contains
# # 比如：<div class="class1 class2">1</div> 使用 //div[contains(@class, 'class1') and contains(@class, 'class2')]
# # browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()
#
# # driver.find_element_by_xpath('//a[contains(@class, "btn") and contains(@class, "btn-account")]').click()
# # 直接定位包含第二个 class 类也可以
# driver.find_element_by_xpath('//a[contains(@class, "btn-account")]').click()  # WebElement
# cookies = driver.get_cookies()
# print(cookies)

# time.sleep(3)
# driver.close()


button = driver.find_element_by_tag_name('div')

print(button)

button = driver.find_element_by_id('anony-nav')

print(button)
