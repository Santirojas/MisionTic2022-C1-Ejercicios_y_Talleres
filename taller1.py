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
