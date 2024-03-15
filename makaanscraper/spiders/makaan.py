import scrapy
from makaanscraper.items import Makaanscrape

class MakaanSpider(scrapy.Spider):
    name = "makaan"
    allowed_domains = ["www.makaan.com"]

    custom_settings = {
        'FEEDS': {
            'makaandata.json': {'format': 'json', 'overwrite': True},
        }
    }

    def start_requests(self):
        start_page = 1
        end_page = 3
        for page_number in range(start_page, end_page + 1):
            url = f'https://www.makaan.com/bangalore-residential-property/buy-property-in-bangalore-city?page={page_number}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        listings = response.css('li.cardholder')
        for list in listings:
            yield self.parse_data(list)

    def parse_data(self, listing):
        makaanitem = Makaanscrape()
        makaanitem['name'] = listing.xpath(".//span[@class='project-wrap']/strong/a[@class='projName']/span/text()").extract_first()
        makaanitem['price'] = listing.xpath("//span[@itemprop='offers']/text()").get()
        makaanitem['price_sufix'] = listing.xpath("//td[@class='price']/div[@data-type='price-link']/span[@class='unit']/text()").extract_first
        makaanitem['per_area_price'] = listing.xpath("//tr[@class='hcol']/td[@class='lbl rate']/text()").extract_first()
        makaanitem['area'] = listing.xpath(".//tr[@class='hcol']/td[@class='size']/span[@class='val']/text()").extract_first()
        makaanitem['area_sufix'] = listing.xpath(".//tr[@class='hcol']/td[@class='lbl']/text()").extract_first()
        makaanitem['status'] = listing.xpath(".//tr[@class='hcol w44']/td[@class='val']/text()").extract_first()
        return makaanitem



# ***********************************************************************************************************************

# import scrapy
# import requests
# import random
# from makaanscraper.items import Makaanscrape

# class MakaanSpider(scrapy.Spider):
#     name = "makaan"
#     allowed_domains = ["www.makaan.com"]
#     start_urls = ['https://www.makaan.com/bangalore-residential-property/buy-property-in-bangalore-city']
    

#     custom_settings = {
#         'FEEDS' : {
#             'makaandata.json' : {'format':'json','overwrite':True},
#         }
#     }

#     def parse(self, response):
#         listings = response.css('li.cardholder')
#         for list in listings:
#             # pg_number = response.xpath("//div/div[3]/div[1]/div/ul/li[2]/a/text()").extract()
#             list_url = 'https://www.makaan.com/bangalore-residential-property/buy-property-in-bangalore-city'
#             yield response.follow(list_url,callback = self.parse_data)   #headers= {'User-Agent':self.userAgents[random.randint(0,len(self.userAgents)-1)]})                      #random.choice(self.userAgents)})
        
#     def parse_data(self,response):
#         # data_ls = response.css('div.loc-wrap')

#         makaanitem = Makaanscrape()
        
#         makaanitem['name'] = response.xpath("//span[@class='project-wrap']/strong/a[@class='projName']/span/text()").extract(),
#         makaanitem['price'] = response.xpath("//div/span[1]/text()").extract(),
#         makaanitem['price_sufix'] = response.xpath("//table/tbody/tr[2]/td[1]/div/span[2]/text()").extract(),
#         makaanitem['per_area_price'] = response.xpath("//div/div[3]/table/tbody/tr[2]/td[2]/text()").extract(),
#         makaanitem['area'] = response.xpath("//tr[@class='hcol']/td[@class='size']/span[@class='val']/text()").extract(),
#         makaanitem['area_sufix'] = response.xpath("//tr[@class='hcol']/td[@class='lbl']/text()").extract(),
#         makaanitem['status'] = response.xpath("//tr[@class='hcol w44']/td[@class='val']/text()").extract(),
        

#         yield makaanitem
        


# ************************************************************************************************************************************

        # # list user agents
    # userAgents = [

    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)',
    # 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)',
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    # 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    # ]

    # # Resquests 
    # data_request = requests.get('https://www.makaan.com/bangalore-residential-property/buy-property-in-bangalore-city',headers= {'User-Agents':random.choice(userAgents)})

    #  = data_request

    # # Status code
    # print(start_urls.status_code)

    # # headers
    # print(start_urls.request.headers)