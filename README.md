# flask-on-iis #

* Tutorial completo em andamento:

Baseado em : 
- [Deploying Flask app on IIS](https://medium.com/@rajesh.r6r/deploying-a-python-flask-rest-api-on-iis-d8d9ebf886e9)

- [wfastcgi 3.0.0](https://pypi.org/project/wfastcgi/)

- [Flask - Run with a Production Server](https://flask.palletsprojects.com/en/1.0.x/tutorial/deploy/#run-with-a-production-server)


1. criar e ativar ambiente virtual (env no exemplo)
2. instalar as dependências
3. habilitar o wfastcgi
ele ira gerar o caminho dos executáveis, para usar no webconfig

Exemplo:

``c:\webserver\flask-on-iis\env\scripts\python.exe|c:\webserver\flask-on-iis\env\lib\site-packages\wfastcgi.py``

4. Alterar no webconfig o 'scriptProcessor' com o caminho obtido acima

5. Efetuar a configuração no IIS