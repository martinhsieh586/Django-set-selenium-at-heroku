Build Python Django in heroku with selenium: Getting Started
==========
 python version:3.8
Features:
=========
- login
 - suggest,visitor's mode can't collect favorite information
 - url: https://scarpygoods.herokuapp.com/login/
- register
 - url: https://scarpygoods.herokuapp.com/register/
- index
 - recently popular article
 - url: https://scarpygoods.herokuapp.com/index/
- search
 - sort by price
 - url: https://scarpygoods.herokuapp.com/search/

- This project is a dynamic web crawler and built on heroku
- First, you need to import two buildpacks in the settings in the heroku official website
 - url: https://github.com/heroku/heroku-buildpack-chromedriver
 - url: https://github.com/heroku/heroku-buildpack-google-chrome
- In this way, we can continue to use selenium to perform dynamic crawler actions

crawler method:
=========
- for goods
 - "finaly\\craweler.py"
- for articles
 - "finaly\\craweler_article.py"
- The above two crawler methods, crawler and crawler article are respectively crawling products and articles

Build steps:
=========
- The following actions are performed on the terminal
 - Download the kit file requirements.txt
  ::

   pip3 install pipreqs
   pipreqs  ./
 - Two parameters need to be set on heroku
  - Step:
  - Open your apps
  - To setting
  - Scroll down to find "Buildpacks" and add buildpacks
  - Put the two sets in
   - heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google-chrome
   - heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver

 - Login heroku
  ::

   heroku login
 - Link app
  ::

   heroku git:remote -a scarpygoods
 - Use heroku
  ::

   git add .
   git commit -am "your_message"
   git push heroku master
 - Open webpage
  ::

   heroku open

 - The above actions are executed on the terminal

The following is a link to the demo video, to quickly understand the website structure and the content of the project:
=========
- Search Articles Demonstration
 - url: https://www.youtube.com/watch?v=jXTCfQODdwU
- search for products Demonstration
 - url: https://www.youtube.com/watch?v=pRSR7oaIuRc&t=74s

technical deficiencies:
=========
- At present, it is impossible to crawl too much data at one time due to the long crawl time, at most two pages
- Because the crawling is all commodities, the price is relatively stable, and there is not much need for comparison. Later, this technology can be used to scrape commodities whose prices are more volatile, such as: stocks
- The first page must enter the login or register page, otherwise there may be an error on the server side, and the local execution of the project is ok
- This project is self-written and refers to the experience of various website masters except for the use of django presets for the structure and the reference of css parts.
- This project can crawl the in-depth pages of each website, but due to the limitation of the webpage built on heroku, the waiting time for response is too long and there are bugs, so only one page of each website can be crawled, and local operations can crawl multiple pages