from tests.app import client
from flask import url_for



class TestHomePage:
    def test_home_page(self, client):
        assert client.get('/').status_code == 200


class TestVowelCount:    
    def test_inputs(self, client):
        
        input_none = None
        input_empty = {}
        input_words_none = {'words': None}
        input_words_empty = {'words': []}
        input_words_integers = {'words': [0,1,2,3]}
        
        response = client.post('/vowel_count', json=input)
        
        assert response.status_code == 200
    
    def test_counting(self, client):
        input = {'words': ['word', 'text', 'phrase','872134','!#(¨$!', '', 'eiaueoaiu']}
        expected = {'word':1, 'text':1, 'phrase':2, '872134':0, '!#(¨$!':0, '':0, 'eiaueoaiu':9}
        
        response = client.post('/vowel_count', json=input)
        
        assert client.post('/vowel_count', json=input).status_code == 200
        assert response.json == expected