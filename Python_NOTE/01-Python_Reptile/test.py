import requests
from lxml import etree

headers = {
        "User-Agent": "Mozillia/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.3554.0 Safari/537.36",
        "Referer": "https://movie.douban.com",
        }
url = "https://movie.douban.com/cinema/nowplaying/chongqing/"
rep = requests.get(url, headers=headers)
text = rep.text
html = etree.HTML(text)
ul = html.xpath("//ul[@class='list']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    region = li.xpath("@data-region")[0]
    actors = li.xpath("@data-actors")[0]
    director = li.xpath("@data-director")[0]
    liimg = li.xpath(".//img/@src")
    movie = {
            "title": title,
            "score": score,
            "region": region,
            "actors": actors,
            "director": director,
            "liimg": liimg,
            }
    movies.append(movie)
print(movies)
autocmd FileType python nnoremap <buffer> <c-d> dd
-f 
adn adn 

