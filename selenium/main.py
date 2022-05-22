from selenium import webdriver
url = "https://centralnovel.com/series/supreme-magus/"

navEdge = webdriver.Edge() # abrir navegador

navEdge.get(url) # navegar para pagina

volumes = navEdge.find_elements_by_class_name("eplister")

pdfsVol7 = volumes[2].find_elements_by_class_name("dlpdf")

length = len(pdfsVol7)
print(f"length: {length}")

primeiro = 619
ultimo = len(pdfsVol7)

for i in range(primeiro, ultimo+1):
  print()





# for i in range(0, 3):
#   href = pdfsVol7[i].get_property("href")
#   numCap = href.__str__()
#   numCap = numCap[numCap.find("capitulo", 0) : ]
#   numCap = numCap[numCap.find("-", 0)+1 : ]
#   numCap = numCap[: numCap.find("/", 0) ]

#   print(f"str: {numCap}")
#   print(f"href: {href}")


# navEdge.close()
  # navEdge.execute_script(f"window.open('{href}', '_blank')")
