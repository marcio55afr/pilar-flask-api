from flaskr.case_validation import valid_dict_key, valid_string_list, valid_order_param

class Test_ValidDictKey:    
    def test_invalid_types(self):
        input_none = None, None
        input_dict_none = {}, None
        input_none_str = None, 'string'
        
        result_none = valid_dict_key(*input_none)
        result_dict_none  = valid_dict_key(*input_dict_none)
        result_none_str  = valid_dict_key(*input_none_str)

        expected_result = False
        assert result_none == expected_result
        assert result_dict_none == expected_result
        assert result_none_str == expected_result
    
    def test_invalid_key(self):
        input_invalid = {'key':'value'}, 'not present key'
        
        result = valid_dict_key(*input_invalid)
        
        assert result == False
        
    def test_valid_values(self):
        input_key_string = {'key_test':None}, 'key_test'
        input_key_int = {1:['word']}, 1
        
        result_key_string = valid_dict_key(*input_key_string)
        result_key_int  = valid_dict_key(*input_key_int)
        
        assert result_key_string == True
        assert result_key_int == True
        
    
class Test_ValidStringList:
    def test_invalid_types(self):
        input_None = {'key_test':None}, 'key_test'
        input_dict = {'key_test':{}}, 'key_test'
        input_string = {'key_test':'string'}, 'key_test'
        
        result_None  = valid_string_list(*input_None)
        result_dict  = valid_string_list(*input_dict)
        result_string  = valid_string_list(*input_string)

        expected_result = False
        assert result_None == expected_result
        assert result_dict == expected_result
        assert result_string == expected_result
    
    def test_invalid_list(self):
        input_int_list = {'key_test':[1,2,3]}, 'key_test'
        input_mixed_list = {'key_test':['word','text','',0]}, 'key_test'
        
        result_int_list  = valid_string_list(*input_int_list)
        result_mixed_list  = valid_string_list(*input_mixed_list)

        expected_result = False        
        assert result_int_list == expected_result
        assert result_mixed_list == expected_result
        
    def test_valid_values(self):        
        input_empty_list = {'test_key':[]}, 'test_key'
        input_string_list = {'key_test':['word1', 'word2']}, 'key_test'
        
        result_iinput_empty_list  = valid_string_list(*input_empty_list)
        result_string_list  = valid_string_list(*input_string_list)
        
        expected_result = True        
        assert result_iinput_empty_list == expected_result
        assert result_string_list == expected_result

class Test_OrderParam:
    def test_invalid_types(self):
        input_None = {'key_test':None}, 'key_test'
        input_list = {'key_test':[]}, 'key_test'
        
        result_None  = valid_order_param(*input_None)
        result_list  = valid_order_param(*input_list)

        expected_result = False
        assert result_None == expected_result
        assert result_list == expected_result
        
    def test_invalid_param(self):
        input_asc_upper = {'key_test':'ASC'}, 'key_test'
        input_desc_upper = {'key_test':'DESC'}, 'key_test'
        input_random = {'key_test':'any value'}, 'key_test'
        input_wrong_key = {'key_test':None, 'wrong_key':'asc'}, 'key_test'
        
        result_asc_upper  = valid_order_param(*input_asc_upper)
        result_desc_upper  = valid_order_param(*input_desc_upper)
        result_random  = valid_order_param(*input_random)
        result_wrong_key = valid_order_param(*input_wrong_key)

        expected_result = False        
        assert result_asc_upper == expected_result
        assert result_desc_upper == expected_result
        assert result_random == expected_result
        assert result_wrong_key == expected_result
    
    def test_valid_values(self):
        input_asc = {'key_test':'asc'}, 'key_test'
        input_desc = {'test_key':'desc'}, 'test_key'
        
        result_asc = valid_order_param(*input_asc)
        result_desc  = valid_order_param(*input_desc)

        expected_result = True        
        assert result_asc == expected_result
        assert result_desc == expected_result