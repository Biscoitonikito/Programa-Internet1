import urllib.request
import requests

class Download:

    def __init__(self):
        pass

    def download_jpg(self,url,path,nome):
        full_patch = patch + nome + '.jpg'
        urllib.request.urlretrieve(url,full_patch)
        

if __name__ == '__main__':
    url = input("Digite a url: ")
    nome = input("Nome do arquivo: ")
    patch = "Documentos/"
    

    Download().download_jpg(url,patch,nome)
    
