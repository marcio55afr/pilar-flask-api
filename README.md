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

### Configuração do Ambiente
```bash
git clone https://github.com/marcio55afr/pilar-flask-api/
cd pilar-flask-api
virtualenv venv
venv\Scripts\activate
```

### Instalação
```bash
python setup.py install
```

### Como rodar a aplicação
```bash
C:\..\pilar-flask-api\> venv\Scripts\activate
(venv) C:\..\pilar-flask-api\> flask run
```

### Como rodar os testes da aplicação
```bash
C:\..\pilar-flask-api\> venv\Scripts\activate
(venv) C:\..\pilar-flask-api\> pytest
```
ou
```bash
C:\..\pilar-flask-api\> venv\Scripts\activate
(venv) C:\..\pilar-flask-api\> pytest --cov=flaskr tests/
```

## Utilizando a aplicação

Com a aplicação rodando, é possível acessar as rotas criando funções e rodando-as nos arquivos de testes.
Uma outra alternativa é utilizando alguma aplicação, como o [Postman](https://www.postman.com/),
para fazer as requisições HTTP enviando os dados desejados com o devido método.
