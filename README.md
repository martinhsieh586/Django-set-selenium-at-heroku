# Python Django with selenium: Getting Started

### 本次專案進行網頁動態爬蟲，並建置於heroku上
### 需要再heroku的setting中引入兩個buildpacks
https://github.com/heroku/heroku-buildpack-chromedriver
https://github.com/heroku/heroku-buildpack-google-chrome
### 如此才能以selenium進行動態爬蟲的動作

###爬蟲兩套件，craweler、crawler_article分別是爬取商品及文章，皆是自寫套件

##以下動作在終端機執行
### 需將此參數設置於heroku上
heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google-chrome
heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver

### 如有修改資料，或第一次使用需下載request.txt中套件
git add .
git commit -am "your_message"
git push heroku master

### 再來登入heroku
heroku login
### 開啟網頁
heroku open

##以上動作在終端機執行

##以下為demo影片連結，更快速了解網站架構，及專案內涵

###目前因技術上問題無法一次爬取過多資料，最多兩頁
###因爬取皆是商品，價格較穩定，之後可用此技術爬取價格較易變動的商品，如:股票
###第一頁必須進入login 或register頁，否則server端會有問題，本地執行該專案皆正常
###該專案除架構為django預設，以及css部分參考外，皆為自寫