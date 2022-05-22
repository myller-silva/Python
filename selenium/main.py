from selenium import webdriver
from time import sleep
navEdge = webdriver.Edge()  # abrir navegador


c = 629
f = 744

navEdge.get(f"https://centralnovel.com/supreme-magus-capitulo-{c}/pdf/")  # navegar para pagina
c+=1

for i in range(c, f+1):
  url = f'https://centralnovel.com/supreme-magus-capitulo-{i}/pdf/'
  # navEdge.get(url)  # navegar para pagina
  navEdge.execute_script(f"window.open('{url}', '_blank')")
  sleep(5)

sleep(60)

navEdge.close()
