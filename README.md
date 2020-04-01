# Instagram Comments Scraper

## Install dependencies
This program requires python installed on your machine. From your Linux/Mac terminal, install the dependencies by running :
`$ pip install -r requirements.txt`

## Install Chrome Web Driver
Download latest Chrome web driver from https://sites.google.com/a/chromium.org/chromedriver/downloads  
Or if you on Linux/Ubuntu <br>
`wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip`  
Extract the binary then move to `/usr/local/bin/`by issuing : <br>
`$ sudo mv chromedriver /usr/local/bin/chromedriver` <br>
`$ sudo chown root:root /usr/local/bin/chromedriver` <br>
`$ sudo chmod +x /usr/local/bin/chromedriver`

## Run
From your Linux/Mac terminal run : <br>
`$ python scraper.py <post-url> <total-load-more-click>`

Change the URL with your post target  
For Example : <br>
`$ python scraper.py https://www.instagram.com/p/BqUfulwH6O4/ 5`

# License
This project is under the [MIT License](https://github.com/AgiMaulana/instagram-comments-scraper/blob/master/LICENSE.md)
