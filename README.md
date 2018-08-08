# Scrapy parser

The project parses http://sudact.ru/regular/area/

## Be careful!

The project used proxy. You must remove or change following code from spiders/courts.py

```
meta={'proxy': 'http://83.219.137.25:41258'}
```