from flask import Flask, jsonify, send_from_directory
#from flask_cors import CORS

# Cria a aplicação Flask
app = Flask(__name__, static_folder='static')
#CORS(app)

# Rota principal que retorna um JSON
@app.route("/api/relatorio", methods=["GET"])
def get_valores():
    dados = {
        "Alunos": ["Ana Carolina", "Bruno Marques", "Carlos Eduard", "Diana Lima", 
                   "José Silva", "Marcos Souza", "Ed Lima"],
        "Livros": ["Vidas Secas", "Dom Casmurro", "O Cortiço", "Memórias Póstumas de Brás Cubas",
                   "Vidas Secas", "Dom Casmurro", "O Cortiço"],
        "Turma": ["3D", "2D", "2E", "3A", "3D", "2D", "2D"]
    }
    return jsonify(dados)

# Rota simples de teste
@app.route("/", methods=["GET"])
def home():
    return "<h1>API de Exemplo 🚀</h1><p>Acesse /api/valores para ver os dados em JSON.</p>"

@app.route("/imagem", methods=["GET"])
def get_imagem():
    return jsonify({'url': 'http://10.0.2.2:5000/static/images/clean_code.jpg'})

@app.route("/static/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(app.static_folder + '/images', filename) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
