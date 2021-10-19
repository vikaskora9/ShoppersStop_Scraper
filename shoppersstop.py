from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import re
driver = webdriver.Edge('C:/Users/vikas/Downloads/edgedriver_win64/msedgedriver')
product_img = []
product_name = []
brand_link = []
Price_lst = []
product_url = []
for g in range(1, 30):
    print(g)
    driver.get('https://www.shoppersstop.com/men-clothing/c-A1010?page=' + str(g))
    driver.implicitly_wait(30)
    brand = driver.find_elements_by_class_name('Brand-name')
    Product = driver.find_elements_by_class_name('pro-name')
    for u in range(len(brand)):
        brand_link.append(brand[u].text)
        product_name.append(Product[u].text)
    for _ in range(1, len(brand)+1):
        prod_url = driver.find_element_by_xpath('//*[@id="qv-drop"]/li[' + str(_) + ']/div/div[3]/a').get_attribute('href')
        product_url.append(prod_url)
        try:
            price = driver.find_element_by_xpath('//*[@id="qv-drop"]/li['+str(_)+']/div/div[3]/a/div[2]/span/div/ul/li[1]/meta').get_attribute('content')
            Price_lst.append('Rs ' + str(price))
        except NoSuchElementException:
            price = driver.find_element_by_xpath('//*[@id="qv-drop"]/li[' + str(_) + ']/div/div[3]/a/div[2]/div[1]').text
            Price_lst.append(re.sub('MRP', '', price))
        prod_img = driver.find_element_by_id(str(_) + 'HashPosition')
        prod_img_link = prod_img.find_element_by_id('primaryImage').get_attribute('src')
        product_img.append(prod_img_link)
        
Detail = {
    'Product Name': product_name,
    'Product Image Link': product_img,
    'Brand': brand_link,
    'Price': Price_lst,
    'Url': product_url
}

df = pd.DataFrame(Detail)
df.to_csv('Shoppers.csv', mode='a')

driver.close()

