def CDT(usuario:str,capital:int,tiempo:int):
    valor_interes=capital*0.03*tiempo/12
    if tiempo<= 2:
        valor_perder=capital*0.02
        valor_total=(capital-valor_perder)
    else:
        valor_total=(valor_interes+capital)
    mensaje=f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}'
    return mensaje
usuario1=str('AB1012')
monto1=int(1000000)
tiempo1=int(3)
CDT(usuario1,monto1,tiempo1)

usuario2=str('ER3366')
monto2=int(650000)
tiempo2=int(2)
CDT(usuario2,monto2,tiempo2)
