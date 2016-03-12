from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders.init import InitSpider
from scrapy.http import Response,FormRequest,Request
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule
from selenium import webdriver
from scrapy.selector import Selector

class myfacebookcookies(BaseSpider):
    name = 'myfacebookcookies'
    start_urls = ['https://www.facebook.com/search/top/?q=0103998543']

    def get_cookies(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        base_url = "http://www.facebook.com/login.php"
        driver.get(base_url)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("0149324322")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("B0$y2907")
        driver.find_element_by_name("login").click()
        cookies = driver.get_cookies()
        driver.close()
        return cookies

    def parse(self, response):
        return Request(url="https://www.facebook.com/search/top/?q=0103998543",
            cookies=self.get_cookies(),
            callback=self.login)

    def login(self,response):
        return [FormRequest.from_response(response,
            formname='login_form',
            formdata={'email': '0149324322', 'pass': 'B0$y2907'},
            callback=self.after_login)]

    def after_login(self, response):
        #hxs = HtmlXPathSelector(response)
	print 'here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>===...<<<<>>>>>>'
	f = open('login_.html','w')
        f.write(response.body)
	#print response.body.selector.xpath('html/head/title/text()').extract()
	#body = response.body
	#print Selector(text=body).xpath('/html/body').extract()
	#yield Selector(text=body).xpath('/html/head').extract()
	print response.xpath('//title/text()').extract()
	print response.xpath('//div[@class="_42ef"]').extract()
	#('//div[@class="short_holder"]    /h2/a/text()').extract()
	#//div[@class='product']
	print 'ending here <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
	'''for sel in response.xpath('html/head/title'):
        #print hxs.select('/html/head/title').extract()
            item = DmozItem()
            item['title'] = sel.xpath().extract()
            item['link'] = 'dummmmmm'
            item['desc'] = sel.xpath('text()').extract()
            yield item'''



