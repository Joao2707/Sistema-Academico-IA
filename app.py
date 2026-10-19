from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="app/static"
)

@app.route("/")
def incio():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/alunos")
def alunos():
    return render_template("alunos.html")

@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    curso = request.form["curso"]
    email = request.form["email"]

    conexao = sqlite3.connect("Sistema_academico.db")

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO alunos (nome, matricula, curso, email)
    VALUES (?, ?, ?, ?)
    """, (nome, matricula, curso, email))

    conexao.commit()
    conexao.close()

    return redirect("/alunos")

@app.route("/professores")
def professores():
    return render_template("professores.html")

if __name__ == "__main__":
     app.run(debug=True)




