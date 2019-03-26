import requests

class Download:

    def __init__(self):
        pass

    def download_jpg(self,url,nome):
        a = requests.get(url)
        arquivo = nome+'.jpg'
        with open( arquivo, 'wb') as f:
            f.write(a.content)
        

if __name__ == '__main__':
    url = input("Digite a url: ")
    nome = input("Nome do arquivo: ")

    Download().download_jpg(url,nome)
