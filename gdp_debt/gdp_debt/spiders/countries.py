import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//table[@class='jsx-1487038798 table table-striped tp-table-body']/tbody/tr")
        for country in countries:
            country_name = country.xpath(".//text()").get()
            country_debt_gdp_ratio = country.xpath(".//td[position()=2]/text()").get()

            yield {
                'country_name': country_name,
                'country_debt_gdp_ratio': country_debt_gdp_ratio
            }
