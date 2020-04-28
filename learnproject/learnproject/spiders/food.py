import scrapy

class FoodRoger(scrapy.Spider):
    name='food'

    start_urls = [
        'https://www.happyfresh.id/super-indo-cinere/fresh-produce-2/'
    ]

    def parse(self, response):
        title = response.xpath("//h2[@class='jsx-906838217']/text()").extract_first()
        yield {"titletext":title}

        for food in response.xpath("//div[@class='jsx-2751153571 root small PLP-Common-fresh-produce-2-product-container']"):
            title=food.xpath(".//h2[@class='jsx-2751153571 jsx-717190455']/text()").extract_first()
            unit=food.xpath(".//div[@class='jsx-2751153571 jsx-717190455 unit']/text()").extract_first()
            price=food.xpath(".//div[@class='jsx-2751153571 jsx-717190455 price PLP-Common-fresh-produce-2-discount-price']/text()").extract_first()
            unitprice=food.xpath(".//div[@class='jsx-2751153571 jsx-717190455 unit-price']/text()").extract_first()
            unitimg=food.css('img').xpath('@src').extract_first()

            yield {
                'title': title,
                'unit': unit,
                'price': price,
                'unitprice': unitprice,
                'unitimg': unitimg
            }



