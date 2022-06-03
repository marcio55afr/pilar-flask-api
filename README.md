# Pilar API - flask
Aplicação web utilizando Flask com duas funções principais, contagem de vogais e ordenação de palavras. Solução desenvolvida para avaliação técnica na empresa Pilar.
### Rotas:

método |  url
------ | -------------
GET    |  /
POST   |  /vowel_count
POST   |  /sort 

## Documentação Windows

### Requisitos
Python >= 3.8.8

### Instalação
```bash
python setup.py
```

### Como rodar a aplicação
```bash
 venv\Scripts\activate
(venv) flask run
```

### Como rodar os testes da aplicação
```bash
venv\Scripts\activate
(venv) pytest
```
ou
```bash
venv\Scripts\activate
(venv) pytest --cov=flaskr tests/
```

## Utilizando a aplicação

Com a aplicação rodando, é possível acessar as rotas criando funções e rodando-as nos arquivos de testes.
Uma outra alternativa é utilizando alguma aplicação, como o [Postman](https://www.postman.com/),
para fazer as requisições HTTP enviando os dados desejados com o devido método.
