import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print("Um erro aconteceu!")
else:
    print("Site acessado com sucesso!")
    print(site.read())