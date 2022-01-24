import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import os

#爬取博客來okapi熱門討論文章
def okapi():
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")                               #背景執行
    chrome_options.add_argument('--no-sandbox')                             #解决DevToolsActivePort文件不存在的報錯
    chrome_options.add_argument('--disable-gpu')                            #google需要加上來該屬性迴避bug
    chrome_options.add_argument('blink-settings=imagesEnabled=false')       #禁止加載圖片
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://okapi.books.com.tw/list/123?loc=nav_10_000")
    ###隱含等待(最多十秒)
    driver.implicitly_wait(10)
    ##爬取三頁資料
    pages = 3
    df = {}
    df = pd.DataFrame(df)
    titleli = []
    contentli = []
    infoli = []
    browseli = []
    urlli = []
    srcli = []
    ### 設定爬取目標之xpath(目標:標題、內容概要、超連結、圖片連結、文章介紹、瀏覽量)
    title_xpath = '//div[@class="content"]//h3//a'
    content_xpath = '//p[@class="brief"]'
    src_xpath = "//section[@class='list collect-btn']//ul//li//p[@class='img']//a//img"
    info_xpath = "//p[@class='article-info']"
    for page in range(1, pages + 1):
        # 隱含等待最多十秒進行下頁擷取
        driver.implicitly_wait(10)
        ### 抓取標題
        for title in driver.find_elements(By.XPATH, title_xpath):
            article_title = re.sub(r'\n', '', title.text)
            titleli.append(article_title)
        ### 抓取內容概要
        for content in driver.find_elements(By.XPATH, content_xpath):
            article_content = re.sub(r'\n', '', content.text)
            contentli.append(article_content)
        ### 抓取文章介紹
        for info in driver.find_elements(By.XPATH, info_xpath):
            article_info = re.sub(r'\n', '', info.text)
            infoli.append(article_info)
            # 擷取瀏覽次數(表示是否為熱門文章)
            browse = [int(s) for s in re.findall(r'-?\d+\.?\d*', article_info)]
            browseli.append(browse[3])
        ### 抓取文章超連結
        for url in driver.find_elements(By.XPATH, title_xpath):
            urlli.append(url.get_attribute("href"))
        ### 抓取商品圖片超連結
        for src in driver.find_elements(By.XPATH, src_xpath):
            srcli.append(src.get_attribute("src"))
        # 進入下頁
        driver.get(driver.find_element_by_xpath("//li[@class='next']//a").get_attribute("href"))
        # 隱含等待最多十秒進行下頁擷取
        driver.implicitly_wait(10)
    df['title'] = titleli
    df['content'] = contentli
    df['info'] = infoli
    df['browse'] = browseli
    df['url'] = urlli
    df['imgsrc'] = srcli
    df.insert(6, column="company", value="博客來okapi")
    driver.close()
    return df