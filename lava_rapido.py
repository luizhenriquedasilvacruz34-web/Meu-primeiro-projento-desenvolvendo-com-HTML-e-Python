from asyncio import run

from flask import Flask, render_template, request
"""from: significa buscar algo de um lugar, flask: é a biblioteca que estamos utilizando"""
"""flask: permite criar nossa aplicação"""
"""render_template: permite carregar uma pagina HTML"""
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        # Aqui você pode adicionar a lógica para processar o formulário enviado
        nome = request.form.get("nome")
        # Faça algo com o nome, como salvar em um banco de dados ou exibir em]
        veiculo = request.form.get("veiculo")
        # Faça algo com o veículo, como salvar em um banco de dados ou exibir em
        lavagem = request.form.get("lavagem")
        # Faça algo com a lavagem, como salvar em um banco de dados ou exibir em
        return f"Olá {nome}, você solicitou uma lavagem {lavagem} para seu veículo {veiculo}."
    
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)