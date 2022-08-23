from flask import Blueprint, render_template, request, redirect

from calc import proyeccion_anual

views = Blueprint('views', __name__)


#definir ruta
@views.route('/')
def inicio():
    return render_template("inicio.html")

@views.route('/calculadora_impuestos')
def calculadora_impuestos():
    return render_template("calculadora.html")


@views.route('/calculadora_impuestos/resultado', methods = ['POST'])
def resultado():
    print(request.method)
    
    if request.method == 'POST':
        try:
            sueldo = float(request.form["sueldo"])
            Grat_Julio = float(request.form["Grat_Julio"])
            Grat_Diciembre = float(request.form["Grat_Diciembre"])
            vec = []
            vec.append(float(request.form["g_ene"]))
            vec.append(float(request.form["g_feb"]))
            vec.append(float(request.form["g_mar"]))
            vec.append(float(request.form["g_abr"]))
            vec.append(float(request.form["g_may"]))
            vec.append(float(request.form["g_jun"]))
            vec.append(float(request.form["g_jul"]))
            vec.append(float(request.form["g_aug"]))
            vec.append(float(request.form["g_set"]))
            vec.append(float(request.form["g_oct"]))
            vec.append(float(request.form["g_nov"]))
            vec.append(float(request.form["g_dic"]))

            # def proyeccion_anual(sueldo,Grat_Julio,Grat_Diciembre,Vec_Grat_Adicionales):
            res = proyeccion_anual(sueldo,Grat_Julio,Grat_Diciembre,vec)
            print(res)
            return render_template("resultados.html",res=res)
        except:
            return redirect ('/calculadora_impuestos')
            #return render_template("calculadora.html",err_msg='Ingrese valores numéricos en todos los campos')

    








