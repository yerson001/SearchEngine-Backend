from flask import Flask, render_template, request, redirect, url_for
import os

"""-------------------"""
#No se si vaya a servir, debido a que no almacenamos
#internamente el documento
def abrirDocumento(nombreDocumento:str)->str:
    pathDocumento=os.getcwd()+"/"+nombreDocumento
    return open(pathDocumento,'r').read()


"""-------------------"""
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new",methods=['POST'])
def consulta():
    resultados={}
    consulta=request.form['busqueda']
        #documento=abrirDocumento(consulta)
    #pagerank
        #os.system(consulta)
    #inverted index
        #os.system(consulta)
    #
    
    for i in range(20):
        resultados[f"{consulta} - {i}"]="#"
    
    return render_template("resultados.html",
        busqueda=consulta,
        resultados=resultados
        )

if __name__ == "__main__":
    app.run()