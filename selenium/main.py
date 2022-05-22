from selenium import webdriver

url = "https://centralnovel.com/series/supreme-magus/"

navEdge = webdriver.Edge() # abrir navegador

navEdge.get(url) # navegar para pagina

volumes = navEdge.find_elements_by_class_name("eplister")

pdfsVol7 = volumes[2].find_elements_by_class_name("dlpdf")

length = len(pdfsVol7)

for i in range(0, 2):
  href = pdfsVol7[i].get_property("href")
  navEdge.execute_script(f"window.open('{href}', '_blank')")

navEdge.close()