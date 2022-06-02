
class TestHomePage:
    def test_home_page(self, client):
        assert client.get('/').status_code == 200

class TestVowelCount:    
    def test_status_code_400(self, client):
        input_invalid = {'words': ['invalid list',0,2,3]}
        
        response= client.post('/vowel_count', json=input_invalid)
        
        assert response.status_code == 400
    
    def test_counting_no_words(self, client):        
        input_no_words = {'words': []}
        expected_count = {}
        
        response= client.post('/vowel_count', json=input_no_words)
        
        assert response.status_code == 200
        assert response.json == expected_count
    
    def test_counting_words(self, client):
        input_words = {'words': ['word', 'text', 'phrase','872134','!#(¨$!', '', 'eiaueoaiu']}
        expected_words_count = {'word':1, 'text':1, 'phrase':2, '872134':0, '!#(¨$!':0, '':0, 'eiaueoaiu':9}
        
        response = client.post('/vowel_count', json=input_words)
        
        assert response.status_code == 200
        assert response.json == expected_words_count


class TestSort:
    def test_status_code_400(self, client):
        input_invalid = {'words': ['invalid list', 1],
                     'order': 'asc'}
        
        response =  client.post('/sort', json=input_invalid)
        
        assert response.status_code == 400
    
    def test_sorting_asc(self, client):
        input_asc = {'words': ['word', 'text', 'rice', '1usual'],
                     'order': 'asc'}
        expected = ['1usual', 'rice', 'text', 'word']
        
        response = client.post('/sort', json=input_asc)
        
        assert sorted(input_asc['words']) == expected
        assert response.status_code == 200
        assert response.json == expected
    
    
    def test_sorting_words_desc(self, client):
        input_desc = {'words': ['word', 'text', 'rice', '1usual'],
                     'order': 'desc'}
        expected = ['word', 'text', 'rice', '1usual']
        
        response = client.post('/sort', json=input_desc)
        
        assert sorted(input_desc['words'], reverse=True) == expected
        assert response.status_code == 200
        assert response.json == expected
        