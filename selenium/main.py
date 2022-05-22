from selenium import webdriver

url = "https://centralnovel.com/series/supreme-magus/"

navegadorEdge = webdriver.Edge() # abrir navegador

navegadorEdge.get(url) # navegar para pagina

volumes = navegadorEdge.find_elements_by_class_name("eplister")

pdfsVol7 = volumes[2].find_elements_by_class_name("dlpdf")

length = len(pdfsVol7)

for i in range(0, 2):
  href = pdfsVol7[i].get_property("href")
  navegadorEdge.execute_script(f"window.open('{href}', '_blank')")
