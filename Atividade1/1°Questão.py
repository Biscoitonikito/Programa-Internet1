import requests

class RequestInformacao:
    def __init__(self, url):
        self.url = url

    def status(self):
        requests.get(self.url).status_code

    def headers(self): 
        return requests.get(self.url).headers

    def tamanho(self):
        texto = requests.get(self.url).headers
        return len(texto)

    def corpo(self):
        return requests.get(self.url).content

if __name__ == '__main__':
    url = input("Digite a url: ")
    str(url)
    print(RequestInformacao(url).status())
    print(RequestInformacao(url).headers())
    print(RequestInformacao(url).tamanho())
    print(RequestInformacao(url).corpo())
