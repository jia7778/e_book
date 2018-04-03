from selenium import webdriver
import time
import re
wb = webdriver.Firefox()
wb.get("https://read.qidian.com/chapter/y9YT1cy0yo01/faS3sBjQ6OA1")
wb.implicitly_wait(30)
wb.find_element_by_link_text("关闭").click()
time.sleep(1)
wb.find_element_by_link_text("下一章").click()
html = wb.page_source
title =re.findall('<h3 class="j_chapterName">(.*\s.*)</h3>',html)[0]
body = re.findall("<p>(.*?)</p>",html)
print(title)
for txt in  body:
    print(txt)
