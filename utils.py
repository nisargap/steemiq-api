import re
from bs4 import BeautifulSoup
from markdown import markdown
# Cleanhtml code courtesy of https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# Clean Markdown code courtesy of https://stackoverflow.com/questions/761824/python-how-to-convert-markdown-formatted-text-to-text
def cleanmarkdown(raw_text):
  html = markdown(raw_text)
  text = ''.join(BeautifulSoup(html, "html.parser").findAll(text=True))
  return text
