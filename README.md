# PyServer

## IMC & IAC RESTFull WEB SERVER em Python

Este projeto calcula IMC(Índice de massa corporal) e IAC(Índice de adiposidade corporal) usando Python Flask.

### Instruções para instalação

Em um terminal dentro da pasta do projeto:
 - Crie ambiente virtual do python `$ virtualenv venv`
 - Ative o ambiente virtual `$ source venv/bin/activate`
 - Instale os requisitos `$ pip install -r requirements.txt`
 - Rode o projeto `$ python server.py`
 
 ### Usando o WEB SERVER
  
  Com as configurações padrões do flask o servidor será iniciado em: `http://0.0.0.0:5000/`.

 
 #### Como usar a API de IAC:<br/> 

`POST http://0.0.0.0:5000/api/IAC`

 Com um json com os seguintes paramêtros:
 
 - circ_quadril `# Número maior do que zero.`
 - altura `# Número maior do que zero.`
 - sexo `# m para masculino e f para feminino.`
 
 Obs: Valores diferentes do citado geraram requisições bem sucedidas, mas retornará mensagem de erro no corpo da resposta.
 
 Exemplo de corpo de requisição:
 ~~~json
 {
    "circ_quadril": 92,
    "altura": 1.65,
    "sexo": "f"
}
 ~~~
 
 Exemplo de resposta:
 ~~~json
 {
  "condicao": "Normal",
  "iac": 27.29
}
~~~

 #### Como usar a API de IMC:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`POST http://0.0.0.0:5000/api/IMC`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com um json com os seguintes paramêtros: <br/>
 - peso `# Número maior do que zero.`
 - altura `# Número maior do que zero.`
 
 Obs: Valores diferentes do citado geraram requisições bem sucedidas, mas retornará mensagem de erro no corpo da resposta.
 
 Exemplo de corpo de requisição:
 ~~~json
 {
    "peso": 72,
    "altura": 1.75
}
 ~~~
 
 Exemplo de resposta:
 ~~~json
{
  "condicao": "Peso normal",
  "imc": 23.51
}
~~~
 
