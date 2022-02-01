import requests
import bs4

responce = requests.get('http://2ip.ru')
# responce.raise_for_status()

# print(responce.text)
text = responce.text
# d_clip_pos = text.find('id="d_clip_button"')
# print(d_clip_pos)
# span_pos = text.find('<span>', d_clip_pos)
# span_end = text.find('</span>', d_clip_pos)
# print(span_pos)
# print(text[span_pos+6:span_pos+20])
# print(text[span_pos+6:span_end])

soup = bs4.BeautifulSoup(text, features='html.parser')
d_button = soup.find(id="d_clip_button")
span = d_button.find('span')
print(type(span))
print(span.text)