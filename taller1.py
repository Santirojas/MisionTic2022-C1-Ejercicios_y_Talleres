## Reto 1: Los cinco doses
##¿Sabrías obtener los números del 0 al 10 utilizando cinco 2's y los signos suma (+), resta (-),  multiplicación (x) y división (/) y paréntesis? Te regalamos el ejemplo para el 0 y el resto deberás calcularlos tú mismo y comprobarlos en Python. ¡Ánimo!

cero = (2 - 2) * 2 * 2 * 2
uno = (2-2)*2+(2/2)
dos = (2-2)+(2-2)+2
tres = ((2*2*2)-2)/2
cuatro = (2+2)+(2-2)*2
cinco = ((2*2*2)+2)/2
seis = (2+2+2)+(2-2)
siete = (2*2*2)-(2/2)
ocho =(2*2*2) +(2-2)
nueve = ((2*2*2*2)+2)/2
diez = 2+2+2+2+2
print(cero,uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez)

## Reto 2: ¿Cuánto costará el teléfono?
#El IVA es un Impuesto sobre el Valor Añadido de un servicio o producto. En España disponemos de varios tipos de IVA (21%, 10% y 4%). Este impuesto grava sobre el precio neto del producto, es decir, el precio total o bruto corresponde al precio neto del producto más el impuesto que se le aplica.

##Estamos interesados en comprar un nuevo teléfono móvil y en el escaparate de una tienda aparece que el móvil cuesta 420€. El problema es que si nos esperamos a comprarlo al día siguiente sufrirá un incremento porcentual del 20%. ¿Cuánto costará entonces el teléfono si nos esperamos?
precio=420
precio_nuevo=precio*1.20
print(precio_nuevo)

## Reto 3: ¿Cuántas vueltas dará un Fidget Spinner?
#El spinner es un juguete que cabe en la palma de la mano y consiste en tres aros unidos entre sí. En el centro hay un círculo que hace las veces de eje giratorio y permite que los aros de vueltas y más vueltas, como las hélices de un helicóptero.
#Sabemos que un Fidget Spinner da 147 vueltas por minuto ¿Cuántas vueltas dará en 640 segundos? Para este ejercicio se desprecia el rozamiento con el aire.

vueltas=147*(1/60)*(640)
print(vueltas)

## Reto 4: ¿Cuántas latas de refresco sobran?
#Un acto de graduación es la ceremonia oficial que clausura el curso escolar y sirve de reconocimiento a los estudiantes que han completado los requisitos académicos de un plan de estudios y, por lo tanto, se han hecho merecedores del título académico.
#Para organizar una fiesta de graduación del instituto se compran 9 cajas de refrescos, donde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas y queremos que todas y cada una de ellas consuman la misma cantidad de refrescos ¿Cuántas latas de refresco sobrarán?
cajas=9
latas=24
personas=56
total_latas=cajas*latas
latas_persona=total_latas//personas
total_consumido=latas_persona*personas
sobran=total_latas-total_consumido
print(sobran)

## Ejercicio 5: ¿Cuánto te ha costado el ordenador?
# El videojuego en el ordenador está viviendo una nueva época de oro con un montón de juegos exclusivos. Para comprarte un PC Gamer deberás fijarte principalmente en el procesador, la tarjeta gráfica, la memoria RAM... pero sobre todo en los accesorios como el teclado y ratón.
# Estás interesado en comprarte un nuevo PC y en la tienda de tu barrio cuesta 660€ con todos los accesorios incluidos. Sin embargo, el vendedor te descuenta el 10% por pronto pago ¿Cuánto tienes que pagar en total por el ordenador con todos los accesorios?
Precio_original=660
Precio_final=Precio_original-Precio_original*0.1
print(Precio_final)


## Ejercicio 6: ¿Qué precio tenían antes del descuento?
# En España, las rebajas de invierno suelen comenzar entre los días 1 y 7 de enero y finalizan a final de marzo. Por otro lado, las rebajas de verano empiezan durante la primera semana del mes de julio y finalizan durante el mes de septiembre.
# Para aprovechar la temporada de rebajas he salido de compras. He pagado 34€ por unos pantalones que tenían un descuento del 15%. ¿Qué precio tenían antes de aplicar el descuento?
precio_pantalones=34
precio_sindescuento_pantalones=precio_pantalones+precio_pantalones*0.15
print(precio_sindescuento_pantalones)
