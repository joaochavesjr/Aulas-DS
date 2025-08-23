from flask import Flask, jsonify

# Cria a aplicação Flask
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
