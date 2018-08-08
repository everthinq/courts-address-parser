# Scrapy parser

The project parses every court name and court address from http://sudact.ru/regular/area/
The main code executes from *spiders/courts.py*

## Prerequisites

* Python 3.*
* Scrapy

### How to run

Just run *courts/main.py*

### Be careful!

I used proxy for the project because I've been blocked by nginx. But you must change proxy server or remove the following code from *spiders/courts.py*

```
meta={'proxy': 'http://83.219.137.25:41258'}
```
### Results

Results of the project you can see [here](https://github.com/everthinq/courts-address-parser/blob/master/log_processing/courts.json)