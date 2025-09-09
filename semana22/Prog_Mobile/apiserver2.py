from flask import Flask, jsonify

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal que retorna um JSON
@app.route("/api/relatorio", methods=["GET"])
def get_valores():
    dados = [
	{"aluno": "Ana Carolina - 2D",
	 "livro": "01/09/2025: Vidas Secas",
         "turma": "2D"},

	{"aluno": "Bruno Marques - 2E",
	 "livro": "03/09/2025: Dom Casmurro",
         "turma": "2E"},

	{"aluno": "Carlos Eduardo - 3D",
	 "livro": "02/09/2025: O Cortiço",
         "turma": "2D"},

	{"aluno": "Diana Lima - 1E",
	 "livro": "05/09/2025: Memórias Póstumas de Brás Cubas",
         "turma": "3D"}
    ]
    return jsonify(dados)

# Rota simples de teste
@app.route("/", methods=["GET"])
def home():
    return "<h1>API de Exemplo 🚀</h1><p>Acesse /api/valores para ver os dados em JSON.</p>"

if __name__ == "__main__":
    app.run(debug=True)
