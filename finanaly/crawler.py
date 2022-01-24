import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from time import sleep
import re

#爬取博客來
def books(search):
    try:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        driver.get("https://www.books.com.tw/?loc=tw_logo_001")
        keyword = driver.find_element_by_id("key")
        keyword.send_keys(search)
        keyword.submit()
        ###隱含等待(最多十秒)
        driver.implicitly_wait(10)
        ##爬取四頁資料
        pages = 3
        df = {}
        df = pd.DataFrame(df)
        nameli = []
        priceli = []
        urlli = []
        srcli = []
        ### 設定爬取目標之xpath
        name_xpath = '//tr//td//h4//a'
        price_xpath = '//ul[@class="list-nav clearfix"]//li'
        src1_xpath = "//img[@class='b-lazy b-loaded']"
        src2_xpath = "//img[@class='b-lazy']"
        for page in range(1, pages + 1):
            # 隱含等待最多十秒進行下頁擷取
            driver.implicitly_wait(10)
            ### 抓取商品名稱欄位
            for name in driver.find_elements(By.XPATH, name_xpath):
                nameli.append(name.text)
            ### 抓取商品價格欄位
            for price in driver.find_elements(By.XPATH, price_xpath):
                trans = re.sub(r',', '', price.text)
                # 擷取商品價格方便之後比較
                numbers = [int(s) for s in re.findall(r'-?\d+\.?\d*', trans)]
                if len(numbers) > 1:
                    priceli.append(numbers[1])
                else:
                    priceli.append(numbers[0])
            ### 抓取商品超連結
            for url in driver.find_elements(By.XPATH, name_xpath):
                urlli.append(url.get_attribute("href"))
            ### 抓取商品圖片1超連結
            for src1 in driver.find_elements(By.XPATH, src1_xpath):
                srcli.append(src1.get_attribute("src"))
            ### 抓取商品圖片2超連結--因博客來圖片未滑至該商品時會以b-lazy顯示，class中會無b-loaded，所以需以不同class名稱再抓取一次
            for src2 in driver.find_elements(By.XPATH, src2_xpath):
                srcli.append(src2.get_attribute("data-src"))
            # 點擊下頁
            driver.find_element_by_xpath("//ul[@class='page']//a[@class='next']").click()
            # 隱含等待最多十秒進行下頁擷取
            driver.implicitly_wait(10)
        df['圖片'] = srcli
        df['商品名稱'] = nameli
        df['商品價格'] = priceli
        df['url'] = urlli
        df.insert(4, column="商品所屬網站", value="博客來")
        driver.close()
        return df
    except:
        driver.quit()
#爬取天瓏書局
def tanlong(search):
    try:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        driver.get("https://www.tenlong.com.tw")
        key_xpath = '/html/body/div[3]/nav[1]/nav/div/form/input[2]'
        key_nodes = driver.find_element(By.XPATH, key_xpath)
        key_nodes.send_keys(search)
        key_nodes.submit()
        ###隱含等待(最多十秒)
        driver.implicitly_wait(10)
        ##爬取四頁資料
        pages = 3
        df = {}
        df = pd.DataFrame(df)
        nameli = []
        priceli = []
        urlli = []
        srcli = []
        ### 設定爬取目標之xpath
        name_xpath = '//div//strong//a'
        price_xpath = '//span[@class="price"]'
        src_xpath = "//a[@class='cover w-full']//img"
        ###開始進行分頁爬蟲
        for page in range(1, pages + 1):
            ### 抓取商品名稱欄位
            for name in driver.find_elements(By.XPATH, name_xpath):
                nameli.append(name.text)
            ### 抓取商品價格欄位
            for price in driver.find_elements(By.XPATH, price_xpath):
                trans = re.sub(r',', '', price.text)
                numbers = [int(s) for s in re.findall(r'-?\d+\.?\d*', trans)]
                priceli.append(numbers[0])
            ### 抓取商品超連結
            for url in driver.find_elements(By.XPATH, name_xpath):
                urlli.append(url.get_attribute("href"))
            ### 抓取商品圖片超連結
            for src in driver.find_elements(By.XPATH, src_xpath):
                srcli.append(src.get_attribute("src"))
            # 點擊下頁
            driver.find_element_by_xpath("//a[@class='next_page']").click()
            # 隱含等待最多十秒進行下頁擷取
            driver.implicitly_wait(10)
        df['圖片'] = srcli
        df['商品名稱'] = nameli
        df['商品價格'] = priceli
        df['url'] = urlli
        df.insert(4, column="商品所屬網站", value="天瓏書局")
        driver.close()
        return df
    except:
        driver.quit()
#爬取金石堂
def kingstone(search):
    try:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        driver.get("https://www.kingstone.com.tw")
        keyword = driver.find_element_by_class_name("headerSearchBar")
        keyword.send_keys(search)
        keyword.submit()
        ###隱含等待(最多十秒)
        driver.implicitly_wait(10)
        ##爬取四頁資料
        pages = 3
        df = {}
        df = pd.DataFrame(df)
        nameli = []
        priceli = []
        urlli = []
        srcli = []
        ### 設定爬取目標之xpath
        name_xpath = '//div//h3//a'
        price_xpath = "//div[@class='buymixbox']"
        src1_xpath = "//div[@class='coverbox']//a//img[@class=' lazyloaded']"
        src2_xpath = "//div[@class='coverbox']//a//img[@class=' lazyloading']"
        src3_xpath = "//div[@class='coverbox']//a//img[@class=' ls-is-cached lazyloaded']"
        for page in range(1, pages + 1):
            ### 抓取商品名稱欄位
            for name in driver.find_elements(By.XPATH, name_xpath):
                nameli.append(name.text)
            ### 抓取商品價格欄位
            for price in driver.find_elements(By.XPATH, price_xpath):
                trans = re.sub(r'\n', '', price.text)
                # 擷取商品價格方便之後比較
                numbers = [int(s) for s in re.findall(r'-?\d+\.?\d*', trans)]
                if len(numbers) > 1:
                    priceli.append(numbers[1])
                else:
                    priceli.append(numbers[0])
            ### 抓取商品超連結
            for url in driver.find_elements(By.XPATH, name_xpath):
                urlli.append(url.get_attribute("href"))
            ### 抓取商品圖片1超連結
            for src1 in driver.find_elements(By.XPATH, src1_xpath):
                srcli.append(src1.get_attribute("src"))
            ### 抓取商品圖片2超連結--圖片未滑到時，class名為lazyloading
            for src2 in driver.find_elements(By.XPATH, src2_xpath):
                srcli.append(src2.get_attribute("src"))
            ### 抓取商品圖片3超連結--圖片未滑到時，class名為 ls-is-cached lazyloaded
            for src3 in driver.find_elements(By.XPATH, src3_xpath):
                srcli.append(src3.get_attribute("src"))
            # 點擊下頁
            driver.find_element_by_xpath("//li[@class='pageNext']").click()
            # 隱含等待最多十秒進行下頁擷取
            driver.implicitly_wait(10)
        df['圖片'] = srcli
        df['商品名稱'] = nameli
        df['商品價格'] = priceli
        df['url'] = urlli
        df.insert(4, column="商品所屬網站", value="金石堂")
        driver.close()
        return df
    except:
        driver.quit()
# 爬取誠品
def eslite(search):
    try:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        driver.get("https://www.eslite.com")
        key_xpath = '//div[@class="header-search-bar"]//form//input[@class="form-control"]'
        key_nodes = driver.find_element(By.XPATH, key_xpath)
        key_nodes.send_keys(search)
        key_nodes.submit()
        ###隱含等待(最多十秒)，及更新頁面(誠品有時第一次進入會報錯)
        driver.implicitly_wait(10)
        driver.refresh();
        ##爬取三頁資料
        pages = 3
        df = {}
        df = pd.DataFrame(df)
        nameli = []
        priceli = []
        urlli = []
        srcli = []
        ### 設定爬取目標之xpath
        name_xpath = '//a[@class="item-image-link"]'
        price_xpath = '//span[@class="price"]'
        src_xpath = "//div[@class='item-image-wrap']//img"
        for page in range(1, pages + 1):
            time.sleep(3)
            ### 抓取商品名稱欄位
            for name in driver.find_elements(By.XPATH, name_xpath):
                nameli.append(name.get_attribute("title"))
            ### 抓取商品價格欄位
            for price in driver.find_elements(By.XPATH, price_xpath):
                trans = re.sub(r',', '', price.text)
                matched = re.search("[^\d]", trans)
                if matched == None and trans != '':
                    trans = int(trans)
                    priceli.append(trans)
                else:
                    priceli.append(null)

            ### 抓取商品超連結
            for url in driver.find_elements(By.XPATH, name_xpath):
                urlli.append(url.get_attribute("href"))
            ### 抓取商品圖片超連結
            for src in driver.find_elements(By.XPATH, src_xpath):
                srcli.append(src.get_attribute("data-src"))
            # 點擊下頁
            driver.find_element_by_xpath("//span[@class='icon-fa-chevron-right']").click()
        df['圖片'] = srcli
        df['商品名稱'] = nameli
        df['商品價格'] = priceli
        df['url'] = urlli
        df.insert(4, column="商品所屬網站", value="誠品")
        driver.close()
        return df
    except:
        driver.quit()
# 爬取墊腳石
def tcsb(search):
    try:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        driver.get("https://www.tcsb.com.tw")
        driver.find_element_by_xpath("//div[@class='sc-LzLrX eBAuqO']").click()
        time.sleep(3)
        key_xpath = '//input[@class="ns-search-input"]'
        key_nodes = driver.find_element(By.XPATH, key_xpath)
        key_nodes.send_keys(search)
        driver.find_element_by_xpath("//div[@class='search-wrapper']//a").click()
        ###隱含等待(最多十秒)
        driver.implicitly_wait(10)
        pages = 3
        df = {}
        df = pd.DataFrame(df)
        nameli = []
        priceli = []
        urlli = []
        srcli = []
        ### 設定爬取目標之xpath
        name_xpath = "//div[@class='cabinet-middle blind-top']//h3[@class='cabinet-instruction blind-instruction']"
        price_xpath = "//div[@class='product-card-bottom']//div[@class='price cms-moneyColor']"
        url_xpath = "//a[@class='product-card']"
        src_xpath = "//div[@class='cabinet-top blind-left']"
        for page in range(1, pages + 1):
            ### 抓取商品名稱欄位
            for name in driver.find_elements(By.XPATH, name_xpath):
                nameli.append(name.text)
            ### 抓取商品價格欄位
            for price in driver.find_elements(By.XPATH, price_xpath):
                trans = re.sub(r',', '', price.text)
                numbers = [int(s) for s in re.findall(r'-?\d+\.?\d*', trans)]
                if len(numbers) > 1:
                    priceli.append(numbers[1])
                else:
                    priceli.append(numbers[0])
            ### 抓取商品超連結
            for url in driver.find_elements(By.XPATH, url_xpath):
                urlli.append(url.get_attribute("href"))
            ### 抓取商品圖片超連結
            for src in driver.find_elements(By.XPATH, src_xpath):
                img = (src.get_attribute("style").split('"'))[1]
                srcli.append(img)
            # 點擊下頁
            driver.find_element_by_xpath("//ul[@class='pagination']//li//a[@class='page-link']").click()
            ###強制等待三秒，待所有東西載入完成
            sleep(3)
        df['圖片'] = srcli
        df['商品名稱'] = nameli
        df['商品價格'] = priceli
        df['url'] = urlli
        df.insert(4, column="商品所屬網站", value="墊腳石")
        driver.close()
        return df
    except:
        driver.quit()