# coding: utf8

import scrapy
from bs4 import BeautifulSoup as BS

class courts(scrapy.Spider):
	name = 'courts' # name of spider must be the same as filename
	start_urls = ['http://sudact.ru/regular/area/']

	def parse(self, response): # overrided parse method for recursive requests
		soup = BS(response.text, 'html.parser')
		global_court_hrefs = soup.find_all(class_ = 'wos')

		for each in global_court_hrefs:            
			full_url = 'http://sudact.ru' + each.a['href']
			yield scrapy.Request(
									full_url, 
 									callback = self.parse_local_courts,
									meta={'proxy': 'http://83.219.137.25:41258'}
								)
			#break

	def parse_local_courts(self, response):
		soup = BS(response.text, 'html.parser')

		div_block = soup.find('div', class_ = 'h-col2-inner1')

		courts_list = []
		for each in div_block:
			if 'Перечень судов общей юрисдикции' in each.text:
				continue
			if 'Телефон:' in each.text:
 				continue
			if 'График работы:' in each.text:
				continue
			if len(each.text) == 0:
				continue

			if 'военный суд' in each.text:
				continue
			if 'Кандалакшский районный суд (Мурманская область)' in each.text:
				continue
			if 'Полярный районный суд (Мурманская область)' in each.text:
				continue
			if 'Североморский районный суд (Мурманская область)' in each.text:
				continue
			if 'Старорусский районный суд (Новгородская область)' in each.text:
				continue
			if 'Ясненский районный суд (Оренбургская область)' in each.text:
				continue
			if 'Баунтовский районный суд (Республика Бурятия)' in each.text:
				continue
			if 'Апелляционный суд города Севастополя (Город Севастополь)' in each.text:
				continue
			if 'Усть-Янский районный суд (Республика Саха (Якутия))' in each.text:
				continue
			if 'Сафоновский районный суд (Смоленская область)' in each.text:
				continue
			if 'Буденновский городской суд (Ставропольский край)' in each.text:
				continue
			if 'Богородицкий районный суд (Тульская область)' in each.text:
				continue
			if 'Воткинский районный суд (Удмуртская Республика)' in each.text:
				continue
			if 'Можгинский районный суд (Удмуртская Республика)' in each.text:
				continue

			courts_list.append(each.text)

		fh = open('..\\log.txt', 'a', encoding='utf-8')

		for i in range(0, len(courts_list)):
			if 'Адрес' in courts_list[i]:
				fh.write(courts_list[i-1] + ';delimiter;' + courts_list[i][7::] + '\n')

		fh.close()