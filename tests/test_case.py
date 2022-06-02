
class TestHomePage:
    def test_home_page(self, client):
        assert client.get('/').status_code == 200


class TestVowelCount:    
    def test_inputs(self, client):
        
        input_none = None
        input_empty = {}
        input_words_none = {'words': None}
        input_words_integers = {'words': [0,1,2,3]}
        
        input_words_empty = {'words': []}
        input_expected= {'words':['w1','w2']}

        url = '/vowel_count'
        
        res_none = client.post(url, json=input_none)
        res_empty = client.post(url, json=input_empty)
        res_words_none = client.post(url, json=input_words_none)
        res_input_words_empty = client.post(url, json=input_words_empty)
        res_input_words_integers = client.post(url, json=input_words_integers)
        res_input_expected = client.post(url, json=input_expected)
        
        assert res_none.status_code == 400
        assert res_empty.status_code == 400
        assert res_words_none.status_code == 400
        assert res_input_words_integers.status_code == 400
        
        assert res_input_words_empty.status_code == 200
        assert res_input_expected.status_code == 200
    
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
    
    def test_sorting_words_asc(self, client):
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
        