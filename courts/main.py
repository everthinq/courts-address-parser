from scrapy.cmdline import execute

def main():
    #execute(['scrapy', 'crawl', 'courts', '-s', 'LOG_ENABLED=0'])
    execute(['scrapy', 'crawl', 'courts'])

if __name__ == '__main__':
    main()