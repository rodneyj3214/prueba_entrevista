# prueba_entrevista

## EJERCICIO 1.
1. Consultar el valor de cambio de una de las siguientes opciones en 5 días diferentes de la
siguiente página https://finance.yahoo.com/:
Euros a dólares
Pesos chilenos a dólares
Soles a dólares
2. Almacenar los datos de valor de cambio en una base de datos.
3. Desarrollar un prototipo de API REST que permita consultar el valor de cambio almacenado
en la base de datos
4. Al finalizar el proceso que golpee el webhook con URL
https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2 con un body que incluya el valor
de cambio consultado

### NOTA: 
- Ejecutar  el script para crear BD de postgres en el archivo `init.sql`
- Configurar Usuario y contraseña de BD en el archivo `bd_properties.conf` .  Dar permisos necesarios a este archivo para poder ser leido por el programa.
- Ejecutar el archivo `api.py` para  desplegar un servicio REST, al ejecutarse consulta guarda y golpea el hook, retorna el array con la moneda de cambio, fecha y valor de cambio a Dolares.

## EJERCICIO 2.
1. Desarrollar una función Lambda que consulte a la página https://dweet.io/follow/thecore los
valores de “temperature” y “humidity” cada minuto durante 15 minutos
2. Almacenar los valores consultados en una base de datos
3. Pasados los quince minutos, que la función Lambda de forma automática golpee el webhook
URL https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2 con un body que
incluya todos los valores almacenados en la base de datos

### NOTA: 
- Ejecutar  el script para crear BD de postgres en el archivo `init.sql`
- Configurar Usuario y contraseña de BD en el archivo `bd_properties.conf` .  Dar permisos necesarios a este archivo para poder ser leido por el programa.
- Ejecutar el archivo `consumo.py` el cual abrira un navegador Chrome de la version `90.0.4430.^` refrescará el navegador cada minuto durante 15 minutos  y guardara su información en una BD , al finalizar golpeara un webhook con la información recaudada.

## LAMBDA EJERCICIO 2.
1. Desarrollar una función Lambda que consulte a la página https://dweet.io/follow/thecore los
valores de “temperature” y “humidity” cada minuto durante 15 minutos
2. Almacenar los valores consultados en una base de datos
3. Pasados los quince minutos, que la función Lambda de forma automática golpee el webhook
URL https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2 con un body que
incluya todos los valores almacenados en la base de datos

### NOTA: 
- TODO: V1: Al subir archivo zip. falta instalar chrome.
- TODO: V2: Contenedor de prueba, sin acceso a subir a AWS - S3
