from flask import Flask, render_template, request

import math

app = Flask(__name__)

def calcular_tempo_necessario(principal, taxa, aporte_mensal, montante_desejado):
    taxa_decimal = taxa / 100.0
    tempo = 0
    while principal < montante_desejado:
        principal = (principal + aporte_mensal) * (1 + taxa_decimal)
        tempo += 1
    return tempo

@app.route('/')
def index():
    return render_template('index_tempo_aporte.html')

@app.route('/calcular_tempo', methods=['POST'])
def calcular_tempo():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        taxa = float(request.form['taxa'])
        aporte_mensal = float(request.form['aporte_mensal'])
        montante_desejado = float(request.form['montante_desejado'])

        tempo_necessario = calcular_tempo_necessario(principal, taxa, aporte_mensal, montante_desejado)
        
        return render_template('resultado_tempo_aporte.html', tempo=tempo_necessario)

if __name__ == '__main__':
    app.run(debug=True)
