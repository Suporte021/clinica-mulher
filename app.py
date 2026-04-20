from flask import Flask,render_template,request,url_for
from database import SessionLocal, engine, Base
from models import User

app = Flask(__name__)

# cria tabela no banco
Base.metadata.create_all(bind=engine)

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
    session = SessionLocal()

    if request.method == "POST":
        username = request.form["usuario"]
        password = request.form["senha"]

        user = User(username=username, password=password)

        session.add(user)
        session.commit()

        
        usuario = f"Email: {username}"
    return render_template("resultado.html",usuario=usuario)
    
if __name__ == "__main__":
    app.run(debug=True)    