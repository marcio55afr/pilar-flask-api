from flask import Blueprint, request, render_template, abort, jsonify, Response
from flaskr.case_validation import valid_string_list, valid_order_param
from typing import Union

bp = Blueprint('functions', __name__)


@bp.route("/")
def home_page() -> str:
    """Rota de acesso à HomePage da aplicação definada em um arquivo .html

    Returns:
        str: Retorna um arquivo .html renderizado.
    """
    return render_template('index.html')


@bp.route("/vowel_count", methods=['POST'])
def vowel_count() -> Union[dict, str]:
    """Rota de acesso à função de contagem de vogais.
    É esperado que os dados a serem processados sejam enviados
    através de um JSON.

    Returns:
        dict: Retorna a quantidade de vogais de cada palavra em um
        dicionário no formato palavra:qnt.
        str: Em caso de erro retorna uma mensagem com o status 400.
    """
    data = request.get_json()
    
    # check data if data is valid
    if (not valid_string_list(data, 'words')):
        return "Input data is unacceptable", 400
    
    # count the number of vowels in each word and build a list of it
    words = data['words']
    vowels = ['a','e','i','o','u']
    vowels_count = [len([v for v in word if v in vowels]) for word in words]
    
    # build a answer
    result = dict(zip(words, vowels_count))
    
    return result


@bp.route("/sort", methods=['POST'])
def sort() -> Union[Response, str]:
    """Rota de acesso à função de ordenação de palavras.
    A ordenção pode ser definada ascendente (asc) ou descendente (desc),
    enviando o parametro junto dos dados através de um JSON.

    Returns:
        Response: Retorna uma lista ordenada em formato flask.Response.
        str: Em caso de erro retorna uma mensagem com o status 400.
    """
    data = request.get_json()
    
    # check data if data is valid
    if (not valid_string_list(data, 'words') or
        not valid_order_param(data, 'order')):
        return "Input data is unacceptable", 400
    
    # get the list and the direction
    words = data['words']
    reverse = data['order'] == 'desc'
    
    # sort the list (regarding the direction) and build the Response
    return jsonify(sorted(words, reverse=reverse))
