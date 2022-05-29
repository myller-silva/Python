from selenium import webdriver
from time import sleep
navEdge = webdriver.Edge()  # abrir navegador


c = 771
f = 1083

navEdge.get(f"https://centralnovel.com/supreme-magus-capitulo-{c}/pdf/")  # navegar para pagina
c+=1
sleep(5)

for i in range(c, f+1):
  url = f'https://centralnovel.com/supreme-magus-capitulo-{i}/pdf/'
  navEdge.execute_script(f"window.open('{url}', '_self')")
  sleep(5)
sleep(60)

navEdge.close()
