import re

from bs4 import BeautifulSoup
import requests


class Provider:
    pass


class DLC(Provider):

    SEARCH_URL = 'http://mdlc.iec.cat/results.asp?txtEntrada={word}&operEntrada=0'
    ENTRY_URL = 'http://mdlc.iec.cat/accepcio.asp?Id={id}'

    def __init__(self):
        self._session = requests.Session()

    def find(self, word):
        search_url = self.SEARCH_URL.format(word=word)
        search_response = self._session.get(search_url)
        word_id = self._get_id(search_response.content)

        entry_url = self.ENTRY_URL.format(id=word_id)
        entry_response = self._session.get(entry_url)
        definition = self._get_definition(entry_response.content)

        return definition

    def _get_id(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find('ul', id='listaresults')

        item = results.find('li')
        return item.attrs.get('id')

    def _get_definition(self, html):
        html = html.decode('utf-8')
        html = html.replace('xmlns:fo="http://www.w3.org/1999/XSL/Format"', '')
        html = re.sub(r'<br\s*[\/]?>', '\n', html)
        soup = BeautifulSoup(html, 'lxml')
        return soup.get_text()
