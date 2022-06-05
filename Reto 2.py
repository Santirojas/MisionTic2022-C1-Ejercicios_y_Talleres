def cliente(informacion:dict)->dict:
    if  informacion['primer_ingreso']==True:
        if informacion['edad']>18:
            atraccion='X-Treme'
            valor=20000
            desc=valor*0.05
            total=valor-desc
            
        elif informacion['edad']>=15 and informacion['edad']<=18:
            atraccion='Carros chocones'
            valor=5000
            desc=valor*0.07
            total=valor-desc
            
        elif informacion['edad']>=7 and informacion['edad']<15:
            atraccion='Sillas voladoras'
            valor=10000
            desc=valor*0.05
            total=valor-desc
    else:
        
        if informacion['edad']>18:
            atraccion='X-Treme'
            valor=20000
            total=valor
        
        elif informacion['edad'] >=15 and informacion['edad']<=18:
            atraccion='Carros chocones'
            valor=5000
    
            total=valor
            
        elif informacion['edad']>=7 and informacion['edad']<15:
            
            atraccion='Sillas voladoras'
            valor=10000
            total=valor
    
    if (informacion['edad']>18) or (informacion['edad']>=15 and informacion['edad']<=18) or informacion['edad']>=7 and informacion['edad']<15:
        apto=True
        
    else:
        apto=False
        atraccion='N/A'
        total='N/A'
        
    return {'nombre':informacion['nombre'] , 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':apto, 'primer_ingreso':informacion['primer_ingreso'] , 'total_boleta':total }


a={'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':True}
cliente(a)