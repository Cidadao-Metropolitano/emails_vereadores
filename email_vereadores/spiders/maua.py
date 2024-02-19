import scrapy

class MauaSpider(scrapy.Spider):
    name = "maua"
    allowed_domains = ["www.camaramaua.sp.gov.br"]
    start_urls = ["https://www.camaramaua.sp.gov.br/Vereadores/Index"]

    def parse(self, response):
        listaVereadores = response.css('.col-sm-12.col-md-3.text-center a::attr(href)').getall()
        
        for vereador in listaVereadores:
            yield response.follow(vereador, self.parse_detalhes)

    def parse_detalhes(self, response):
        dadobruto = response.css('.col-md-3 .col-12 ::text').getall()
        dadolimpo = [dado.strip() for dado in dadobruto]
        listaRemocao = ['','Partido Atual:', 'Telefone:', 'Fale com o seu vereador:', 'Email:']
        dadolimpo = [dado for dado in dadolimpo if dado not in listaRemocao]
        yield {'email': dadolimpo[3]}
