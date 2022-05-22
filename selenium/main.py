from selenium import webdriver

url = "https://centralnovel.com/series/supreme-magus/"

vol7_xpath = '//*[@id="post-8353"]/div[4]/div[4]/div/ul'


# navegadorChrome = webdriver.Chrome()
navegadorEdge = webdriver.Edge() # abrir navegador

navegadorEdge.maximize_window()

navegadorEdge.get(url) # navegar para pagina

vol7 = navegadorEdge.find_element_by_xpath(vol7_xpath)


# navegadorEdge.close()

# 125
