# Courts parser

The project parses every court name and court address from [here](http://sudact.ru/regular/area/)

## Prerequisites

* [Python 3](https://www.python.org/)
* [Scrapy](https://scrapy.org/)

### How to run

Just run *courts/main.py*

### Be careful!

I used proxy for the project because I've been blocked by nginx, but you must change proxy server or remove the following code from *spiders/courts.py*

```
meta={'proxy': 'http://83.219.137.25:41258'}
```
### Results

Results of the project you can see [here](https://github.com/everthinq/courts-address-parser/blob/master/log_processing/courts.json)