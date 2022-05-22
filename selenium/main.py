from selenium import webdriver

# abrir navegador:
# navegadorChrome = webdriver.Chrome()
navegadorEdge = webdriver.Edge()
# navegar para pagina:
navegadorEdge.get("https://centralnovel.com/series/supreme-magus/")

xpath = '//*[@id="post-8353"]/div[4]/div[4]/div/ul'
vol7 = navegadorEdge.find_element_by_xpath(xpath)

lis = vol7.find_elements_by_class_name("dlpdf")
print(f"lis: {len(lis)}")


navegadorEdge.close()

# 125