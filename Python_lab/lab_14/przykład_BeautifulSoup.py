from bs4 import BeautifulSoup


html_doc = """
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tytył</title>
    </head>
    <body>
        <p>Paragraf1</p>
        <p><b>Paragraf2</b></p>
        <p id="identydikator3">Paragraf3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.title)
print(soup.findAll("p")[1].b)
print(soup.select("#identydikator3")[0].text)