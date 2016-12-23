from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from html import parser
from requests import get
from urllib import request
from urllib.request import urlopen
import re
import time
import json
phantomjs_path=r'C:\Users\KDFB\Pictures\phantomjs-2.1.1-windows\bin\phantomjs.exe'
driver = webdriver.PhantomJS(phantomjs_path)
url = "http://www.target.com/c/toy-blasters-outdoor-toys/-/N-5xtaa?lnk=toyblasters"

def getAmazonInfoFromUPC( ItemUpc ):
    "Get Amazon Item name, sale price, list price, ASIN number, rate from UPC number"
    Adriver = webdriver.PhantomJS(phantomjs_path)
    AmazonUrl="https://www.amazon.com/ref=nav_logo"
    Adriver.get(AmazonUrl)
    search= Adriver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    search.send_keys(ItemUpc)
    search.submit()

    time.sleep(2)
    #Adriver.find_elements_by_class_name('nav-search-submit-text nav-sprite').click()
    #search upc result page
    print ('Amazon Search Page: '+Adriver.current_url)
    #get result page url & click it
    Adriver.get(Adriver.current_url)
    time.sleep(5)
    axpath = '//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/a/h2'
    print (axpath)
    Adriver.find_element_by_xpath(axpath).click()
    #itempage = Adriver.find_element_by_xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/h2')
    #itempage.click()
    # get Item page
    print('Item url: '+Adriver.current_url)
    ItemName = Adriver.find_element_by_xpath('//*[@id="productTitle"]') 
    ItemSalePrice =Adriver.find_element_by_xpath('//*[@id="priceblock_ourprice"]')
    ItemListPrice = Adriver.find_element_by_xpath('//*[@id="price"]/table/tbody/tr[1]/td[2]/span')
    ReviewStars = Adriver.find_element_by_xpath('//*[@id="reviewStarsLinkedCustomerReviews"]/i/span') 
    time.sleep(3)
    productInfo =Adriver.find_element_by_xpath('//*[@id="productDetails_detailBullets_sections1"]').text
    BestSellerIndex = productInfo.index("#")
    BestSeller = productInfo[BestSellerIndex+5:BestSellerIndex+17]
    ItemReview = Adriver.find_element_by_xpath('//*[@id="averageCustomerReviews"]')
    ReviewNumber = Adriver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')


    print('Item Name: '+ItemName.text)
    print('Item List Price: '+ItemListPrice.text)
    print('Item Sale Price: '+ItemSalePrice.text)
    print('review star: '+ ReviewStars.text)
    print('Item Review Number: '+ReviewNumber.text)
    print('Item Sellers Rank: '+BestSeller)
    Adriver.close()
    return 
getAmazonInfoFromUPC('630509422982')

xpathList=[]
for i in range(1,4):
    itemxpath='//*[@id="plp"]/section[1]/div[2]/div/ul/li['+str(i)+']/div[1]/h3/a' 
    xpathList.append(itemxpath);

#upcList=[]
#for xpath in xpathList:
#    driver.get(url)
#    time.sleep(1)
#    item = driver.find_element_by_xpath(xpath).click()
#    driver.get(driver.current_url)
#    time.sleep(0.5)
#    itemprice= driver.find_element_by_xpath('//*[@id="js-product-sr-id"]/div/span[1]')
#    itemdetail = driver.find_element_by_xpath('//*[@id="itemdetails----toggle"]').click()
#    time.sleep(0.3)
#    itemDetail = driver.find_element_by_xpath('//*[@id="product-attributes"]/ul/li[1]/section').text
#    UpcIndex = itemDetail.index("UPC:")
#    UPC = itemDetail[UpcIndex+5:UpcIndex+17]
#    print ('target price: '+itemprice.text)
#    print ('upc: '+ UPC)
#    upcList.append(UPC)

#AmazonList = []  
#for UPC in upcList:


#Adriver.find_elements_by_class_name('nav-search-submit-text nav-sprite').click()
#search upc result page
#print ('Amazon Search Page: '+Adriver.current_url)

#get result page url & click it
#Adriver.get(Adriver.current_url)
#Adriver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/a/h2').click()
# get Item page
#print('Item url: '+Adriver.current_url)

#driver.close()

