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

def proyeccion_anual(sueldo,Grat_Julio,Grat_Diciembre,Vec_Grat_Adicionales):

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

    GJ = Grat_Julio
    GD = Grat_Diciembre


    RBA=sueldo*12+GJ+GD
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

    AdicionalEnero=ImpuestoAnualProyectado(Vec_Grat_Adicionales[0]+RNA,UIT)-IAP
    AdicionalFebrero=ImpuestoAnualProyectado(Vec_Grat_Adicionales[1]+RNA,UIT)-IAP
    AdicionalMarzo=ImpuestoAnualProyectado(Vec_Grat_Adicionales[2]+RNA,UIT)-IAP
    AdicionalAbril=ImpuestoAnualProyectado(Vec_Grat_Adicionales[3]+RNA,UIT)-IAP
    AdicionalMayo=ImpuestoAnualProyectado(Vec_Grat_Adicionales[4]+RNA,UIT)-IAP
    AdicionalJunio=ImpuestoAnualProyectado(Vec_Grat_Adicionales[5]+RNA,UIT)-IAP
    AdicionalJulio=ImpuestoAnualProyectado(Vec_Grat_Adicionales[6]+RNA,UIT)-IAP
    AdicionalAgosto=ImpuestoAnualProyectado(Vec_Grat_Adicionales[7]+RNA,UIT)-IAP
    AdicionalSetiembre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[8]+RNA,UIT)-IAP
    AdicionalOctubre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[9]+RNA,UIT)-IAP
    AdicionalNoviembre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[10]+RNA,UIT)-IAP
    AdicionalDiciembre=ImpuestoAnualProyectado(Vec_Grat_Adicionales[11]+RNA,UIT)-IAP

    ImpEnero=IAP/11
    ImpFebrero=IAP/11
    ImpMarzo=IAP/11
    IAP=IAP-ImpEnero*3
    ImpAbril=IAP/9
    IAP=IAP-ImpAbril
    ImpMayo=IAP/8
    ImpJunio=IAP/8
    ImpJulio=IAP/8
    IAP=IAP-ImpMayo*3
    ImpAgosto=IAP/5
    IAP=IAP-ImpAgosto
    ImpSetiembre=IAP/4
    ImpOctubre=IAP/4
    ImpNoviembre=IAP/4
    IAP=IAP-ImpSetiembre*3
    ImpDiciembre=IAP


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






"""
res = proyeccion_anual(4000,1000,1000,[1,1,1,1,1,1,1,1,1,1,1,1])

print(res[0:11])
print("Paga impuestos: " + res[12])
"""

"""
    print("Impuesto de Enero: "+str(ImpEnero)+"\n")
    print("Impuesto de Febrero: "+str(ImpFebrero)+"\n")
    print("Impuesto de Marzo: "+str(ImpMarzo)+"\n")
    print("Impuesto de Abril: "+str(ImpAbril)+"\n")
    print("Impuesto de Mayo: "+str(ImpMayo)+"\n")
    print("Impuesto de Junio: "+str(ImpJunio)+"\n")
    print("Impuesto de Julio: "+str(ImpJulio)+"\n")
    print("Impuesto de Agosto: "+str(ImpAgosto)+"\n")
    print("Impuesto de Setiembre: "+str(ImpSetiembre)+"\n")
    print("Impuesto de Octubre: "+str(ImpOctubre)+"\n")
    print("Impuesto de Noviembre: "+str(ImpNoviembre)+"\n")
    print("Impuesto de Deciembre: "+str(ImpDiciembre)+"\n")
"""