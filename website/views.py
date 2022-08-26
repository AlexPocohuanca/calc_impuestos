from flask import Blueprint, render_template, request, redirect
from flask import Flask
#from calc import proyeccion_anual

def ImpuestoAnualProyectado(RNA,UIT):
    if(RNA<=5*UIT):
        IAP=RNA*0.08
    elif(RNA<=20*UIT):
        IAP=RNA*0.14
    elif(RNA<=35*UIT):
        IAP=RNA*0.17
    elif(RNA<=45*UIT):
        IAP=RNA*0.2
    else:
        IAP=RNA*0.3
    return IAP

def proyeccion_anual(sueldo,Grat_Julio,Grat_Diciembre,Vec_Grat_Adicionales,mesinicio):

    UIT = 4600
    #sueldo=float(input("Inserte sueldo: "))

    """
    GJ=float(input("Inserte gratificacion de Julio: "))
    GD=float(input("Inserte gratificacion de Diciembre: "))
    AdiEnero=float(input("Inserte gratificacion adicional de Enero (en caso haya): "))
    AdiFebrero=float(input("Inserte gratificacion adicional de Febrero (en caso haya): "))
    AdiMarzo=float(input("Inserte gratificacion adicional de Marzo (en caso haya): "))
    AdiAbril=float(input("Inserte gratificacion adicional de Abril (en caso haya): "))
    AdiMayo=float(input("Inserte gratificacion adicional de Mayo (en caso haya): "))
    AdiJunio=float(input("Inserte gratificacion adicional de Junio (en caso haya): "))
    AdiJulio=float(input("Inserte gratificacion adicional de Julio (en caso haya): "))
    AdiAgosto=float(input("Inserte gratificacion adicional de Agosto (en caso haya): "))
    AdiSetiembre=float(input("Inserte gratificacion adicional de Setiembre (en caso haya): "))
    AdiOctubre=float(input("Inserte gratificacion adicional de Octubre (en caso haya): "))
    AdiNoviembre=float(input("Inserte gratificacion adicional de Noviembre (en caso haya): "))
    AdiDiciembre=float(input("Inserte gratificacion adicional de Diciembre (en caso haya): "))
    """

    GJ = Grat_Julio if mesinicio<=7 else 0
    GD = Grat_Diciembre if mesinicio<=12 else 0


    RBA=sueldo*(13-mesinicio)+GJ+GD
    RNA=RBA-7*UIT
    if(RNA<=0):
        #print("No paga impuestos\n")
        paga_impuestos = 'No'
        RNA=0
        IAP=0
    else:
        IAP=ImpuestoAnualProyectado(RNA,UIT)
        paga_impuestos = 'Sí'
        
    """
    AdicionalEnero=ImpuestoAnualProyectado(AdiEnero+RNA)-IAP
    AdicionalFebrero=ImpuestoAnualProyectado(AdiFebrero+RNA)-IAP
    AdicionalMarzo=ImpuestoAnualProyectado(AdiMarzo+RNA)-IAP
    AdicionalAbril=ImpuestoAnualProyectado(AdiAbril+RNA)-IAP
    AdicionalMayo=ImpuestoAnualProyectado(AdiMayo+RNA)-IAP
    AdicionalJunio=ImpuestoAnualProyectado(AdiJunio+RNA)-IAP
    AdicionalJulio=ImpuestoAnualProyectado(AdiJulio+RNA)-IAP
    AdicionalAgosto=ImpuestoAnualProyectado(AdiAgosto+RNA)-IAP
    AdicionalSetiembre=ImpuestoAnualProyectado(AdiSetiembre+RNA)-IAP
    AdicionalOctubre=ImpuestoAnualProyectado(AdiOctubre+RNA)-IAP
    AdicionalNoviembre=ImpuestoAnualProyectado(AdiNoviembre+RNA)-IAP
    AdicionalDiciembre=ImpuestoAnualProyectado(AdiDiciembre+RNA)-IAP
    """

    AdicionalEnero=ImpuestoAnualProyectado(Vec_Grat_Adicionales[0]+RNA,UIT)-IAP if mesinicio<=1 else 0
    AdicionalFebrero=ImpuestoAnualProyectado(Vec_Grat_Adicionales[1]+RNA,UIT)-IAP if mesinicio<=2 else 0
    AdicionalMarzo=ImpuestoAnualProyectado(Vec_Grat_Adicionales[2]+RNA,UIT)-IAP if mesinicio<=3 else 0
    AdicionalAbril=ImpuestoAnualProyectado(Vec_Grat_Adicionales[3]+RNA,UIT)-IAP if mesinicio<=4 else 0
    AdicionalMayo=ImpuestoAnualProyectado(Vec_Grat_Adicionales[4]+RNA,UIT)-IAP if mesinicio<=5 else 0
    AdicionalJunio=ImpuestoAnualProyectado(Vec_Grat_Adicionales[5]+RNA,UIT)-IAP if mesinicio<=6 else 0
    AdicionalJulio=ImpuestoAnualProyectado(Vec_Grat_Adicionales[6]+RNA,UIT)-IAP if mesinicio<=7 else 0
    AdicionalAgosto=ImpuestoAnualProyectado(Vec_Grat_Adicionales[7]+RNA,UIT)-IAP if mesinicio<=8 else 0
    AdicionalSetiembre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[8]+RNA,UIT)-IAP if mesinicio<=9 else 0
    AdicionalOctubre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[9]+RNA,UIT)-IAP if mesinicio<=10 else 0
    AdicionalNoviembre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[10]+RNA,UIT)-IAP if mesinicio<=11 else 0
    AdicionalDiciembre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[11]+RNA,UIT)-IAP if mesinicio<=12 else 0

    ImpEnero=IAP/12 if mesinicio==1 else 0
    ImpFebrero=IAP/12 if mesinicio<=2 else 0
    ImpMarzo=IAP/12 if mesinicio<=3 else 0
    IAP=IAP-(ImpEnero+ImpFebrero+ImpMarzo)
    ImpAbril=IAP/9 if mesinicio<=4 else 0
    IAP=IAP-ImpAbril
    ImpMayo=IAP/8 if mesinicio<=5 else 0
    ImpJunio=IAP/8 if mesinicio<=6 else 0
    ImpJulio=IAP/8 if mesinicio<=7 else 0
    IAP=IAP-(ImpMayo+ImpJunio+ImpJulio)
    ImpAgosto=IAP/5 if mesinicio<=8 else 0
    IAP=IAP-ImpAgosto
    ImpSetiembre=IAP/4 if mesinicio<=9 else 0
    ImpOctubre=IAP/4 if mesinicio<=10 else 0
    ImpNoviembre=IAP/4 if mesinicio<=11 else 0
    IAP=IAP-(ImpSetiembre+ImpOctubre+ImpNoviembre)
    ImpDiciembre=IAP if mesinicio<=12 else 0


    ImpEnero=ImpEnero+AdicionalEnero
    ImpFebrero=ImpFebrero+AdicionalFebrero
    ImpMarzo=ImpMarzo+AdicionalMarzo
    ImpAbril=ImpAbril+AdicionalAbril
    ImpMayo=ImpMayo+AdicionalMayo
    ImpJunio=ImpJunio+AdicionalJunio
    ImpJulio=ImpJulio+AdicionalJulio
    ImpAgosto=ImpAgosto+AdicionalAgosto
    ImpSetiembre=ImpSetiembre+AdicionalSetiembre
    ImpOctubre=ImpOctubre+AdicionalOctubre
    ImpNoviembre=ImpNoviembre+AdicionalNoviembre
    ImpDiciembre=ImpDiciembre+AdicionalDiciembre

    return [ImpEnero,ImpFebrero,ImpMarzo,ImpAbril,ImpMayo,ImpJunio,ImpJulio,ImpAgosto,ImpSetiembre,ImpOctubre,ImpNoviembre,ImpDiciembre,paga_impuestos]




views = Blueprint('views', __name__)


#definir ruta
@views.route('/')
def inicio():
    print('inicio')
    return render_template("inicio.html")

@views.route('/calculadora_impuestos')
def calculadora_impuestos():
    print('calculadora')
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
            print('resultados')
            return render_template("resultados.html",res=res)
        except:
            print('redirecting')
            return redirect ('/calculadora_impuestos')
            #return render_template("calculadora.html",err_msg='Ingrese valores numéricos en todos los campos')

    








