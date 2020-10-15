from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://movie.douban.com/subject/1292052/')
time.sleep(1)

# id 只有一个，所以写成 * 也是可以的。
driver.find_element_by_xpath('//*[@id="hot-comments"]/a').click()

time.sleep(2)
print(driver.page_source)

