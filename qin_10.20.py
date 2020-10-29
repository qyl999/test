# import time
# from idlelib import browser
# from selenium.webdriver.common import actions
from selenium import webdriver

driver=webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get('http://localhost:8080/JavaPrj_6/login.do')

#报价管理错误登录
# username_error=driver.find_element_by_name('username').send_keys('admin')
# password_error=driver.find_element_by_name('password').send_keys('1234')
# login_2=driver.find_element_by_name('submit').click()

#报价管理正确登录
username=driver.find_element_by_name('username').send_keys('admin')
password=driver.find_element_by_name('password').send_keys('admin')
login_1=driver.find_element_by_name('submit').click()

#选择客户管理
# driver.switch_to.frame('Links')
# time.sleep(3)
# kehuguanli=driver.find_element_by_id('Bar_panel0_b0').click()
# time.sleep(3)
# driver.switch_to.default_content()
# time.sleep(3)
# driver.switch_to.frame('main')

#点击添加客户
# add=driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/a').click()
# add.driver.switch_to.window(driver.window_handles[-1])
#添加客户界面
# time.sleep(3)
# driver.find_element_by_name('customerNO').send_keys('1434')
# phone=driver.find_element_by_name('phone').send_keys('13112758420')
# people=driver.find_element_by_name('relationman').send_keys('huge')
# cus_name=driver.find_element_by_name('customerName').send_keys('pengyuyan')
# address=driver.find_element_by_name('address').send_keys('chongqing')
# other=driver.find_element_by_name('otherInfo').send_keys('wu')
# time.sleep(3)
# baocun=driver.find_element_by_link_text('保存客户信息').click()

#点击修改客户
# xiugai=driver.find_element_by_xpath('/html/body/center/form/table[1]/tbody/tr[3]/td[7]/a[2]').click()
#修改客户界面
# re_name=driver.find_element_by_name('customerName').send_keys('1513')
# re_address=driver.find_element_by_name('address').send_keys('chongqing')
# re_other=driver.find_element_by_name('otherInfo').send_keys('gengxin')
# re_phone=driver.find_element_by_name('phone').send_keys('19112342101')
# re_people=driver.find_element_by_name('relationman').send_keys('lingengxin')
# gengxin=driver.find_element_by_name('saveButton').click()

#查询客户界面
# chaxun=driver.find_element_by_xpath('//*[@id="Bar_panel0_b1"]/img').click()
#查询客户
# cha_id=driver.find_element_by_name('customerNO').send_keys('001')
# cha_name=driver.find_element_by_name('customerName').send_keys('阿一')
# cha_phone=driver.find_element_by_name('phone').send_keys('13112123245')
# cha_address=dri
# ver.find_element_by_name('address').send_keys('成都市')
# chaxun_cus=driver.find_element_by_name('saveButton').click()
