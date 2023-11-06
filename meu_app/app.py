from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_juros_simples', methods=['POST'])
def calcular_juros_simples():
    try:
        principal = float(request.form['principal'])
        taxa_juros = float(request.form['taxa_juros']) / 100
        tempo = int(request.form['tempo'])
        
        juros = principal * taxa_juros * tempo
        montante = principal + juros

        return render_template('index.html', resultado=f'O montante é: R${montante:.2f}')
    except Exception as e:
        return render_template('index.html', resultado=f'Erro: {str(e)}')
if __name__ == '__main__':
    app.run(debug=True)