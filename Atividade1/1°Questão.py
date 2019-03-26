import requests

class RequestInformacao:
    def __init__(self, url):
        self.url = url

    def status(self):
        requests.get(self.url).status_code

    def headers():
        requests.get(self.url)
        return response.headers

    def tamanho():
        requests.get(self.url)
        return response.headers['content-lenght']

    def corpo():
        requuests.get(self.url)
        return response.content

if __name__ == '__main__':
    url = input("Digite a url")
    str(url)
    print(RequestInformacao(url).status())
    print(RequestInformacao(url).self.headers())
    print(RequestInformacao(url).tamanho())
    print(RequestInformacao(url).corpo())
