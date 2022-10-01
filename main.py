from flask import Flask, redirect, url_for, render_template, request, jsonify
from json import dumps
import requests
import time
import json



app = Flask(__name__)


def clearstr(site): # Private functions
    return None

def perguntas(url): # Private functions
    return None

def outradef(site): # Private functions
    return None

def api_out(pergunta): # Private functions
    return None

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        user = request.form['nm']
        print(user)
        #as cegas
        hllp = user
        hllp = hllp.split('passeidireto.com')
        print('tamanho:', len(hllp))
        if len(hllp) <= 1:
            print('chamou')
            user = api_out(user)
        else:
            print('não chamou')
        #fim as cegas
        a = requests.get(user)
        a = a.text
        b = a.split('"QAPage"')
        if len(b) > 1:
            resposta = perguntas(user)
            resposta = resposta
        else:
            resposta = outradef(user)
        # resposta = resposta.replace('\n', '<br/>')
        return resposta
    else:
        return render_template('resposta_site2.html')

@app.route('/privacypolicy')
def privacy():
    return render_template('PrivacyPolicy.html')

@app.route('/terms')
def terms():
    return render_template('Terms.html')

@app.route('/<arquivo>/<numero>/<materia>')
def uepa(arquivo, numero, materia):
    link = 'https://www.passeidireto.com' + '/' + arquivo + '/' + numero + '/' + materia
    # print(link)
    resposta = outradef(link)
    # resposta = resposta.replace('\n', '<br/>')

    return resposta

@app.route('/<arquivo>/<numero>/<materia>/<lixo>')
def uepa2(arquivo, numero, materia, lixo):
    link = 'https://www.passeidireto.com' + '/' + arquivo + '/' + numero + '/' + materia
    # print(link)
    resposta = outradef(link)
    # resposta = resposta.replace('\n', '<br/>')
    return resposta

@app.route('/pergunta/<numero>/<materia>')
def ratinho(numero, materia):
    link = 'https://www.passeidireto.com/pergunta/' + numero + '/' + materia
    resposta = perguntas(link)
    # resposta = resposta.replace('\n', '<br/>')
    return resposta

@app.route('/api/<pergunta>')
def api(pergunta):
    api_json = {
        'txt': 'nada_aqui',
        'img': ''
    }
    link = api_out(pergunta)

    try:
        address = link.split('/')
        numero = address[4]
        materia = address[5]

        adrrs = 'https://www.passeidireto.com/arquivo/' + numero + '/' + materia

        limite = 0
        a = requests.get(adrrs)
        a = a.text
        a = a.split('https://files.passeidireto.com')
        a = a[5]
        a = a.split('/')
        a = a[1]
        url_img = 'https://files.passeidireto.com/' + a + '/'
        for c in range(1, 100):
            a = requests.get(url_img + 'bg{}.png'.format(c))
            b = str(a)
            if b == '<Response [200]>':
                pass
            else:
                limite = str(c)
                break

        # print('o limite é {}'.format(str(limite)))
        limite = str(int(limite) - 1)
        # print(url_img + 'bg{}.png'.format(limite))
        bera = str(int(limite) - 1)
        limite = int(limite)
        limite = limite
        text_img = []
        for c in range(1, limite + 1):
            text_img.append(url_img + 'bg{}.png'.format(c))

        links = text_img


    except:
        links = []

    txt = clearstr(link)
    txt = txt.replace('<br>', '\n')
    a = api_json
    a['txt'] = txt
    a['img'] = links
    return a

@app.route('/api')
def docs():
    return render_template('api_docs.html')

if __name__ == "__main__":
    app.run(debug=True)
