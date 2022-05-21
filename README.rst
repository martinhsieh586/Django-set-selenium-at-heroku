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

Project introduction:
=========
- Since this project is based on the comparison target of various bookstore websites, there is no need to capture too much data to prevent the data availability from being reduced.
- This website is maintained every other month to prevent the html structure of the crawled website from being updated and the data cannot be crawled.
- This website is continuously updated, the goal is to improve the response speed of the web page and the variety of crawled data.