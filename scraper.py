from selenium import webdriver
import time
import sys

URL = sys.argv[1]
LOADER = sys.argv[2]
#fname = URL + '.xlsx'


driver = webdriver.Chrome()
driver.get(URL)
time.sleep(3)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button')
    i = 0
    while load_more_comment.is_displayed() and i < LOADER:
        load_more_comment.click()
        i += 1
        time.sleep(3)
except:
    pass

user_names = []
user_comments = []
user_date = []
comment = driver.find_elements_by_class_name('gElp9 ')
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    datetime = container.find_element_by_tag_name('time').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)
    user_date.append(datetime)


user_names.pop(0)
user_comments.pop(0)
user_date.pop(0)
import excel_exporter
excel_exporter.export(user_names, user_comments, user_date)

driver.close()
