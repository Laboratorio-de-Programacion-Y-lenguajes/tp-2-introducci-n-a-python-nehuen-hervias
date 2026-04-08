# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: GitHub Copilot

**Prompt usado**: Use un prompt por cada funcion para ir practicando el uso de prompts, aqui los enlisto:
----------------------------------------------------------------------------
Actuá como tutor de Python 3.13. Dame una receta paso a paso para:

que una funcion crear_saludo que tiene como parametro un nombre str, devuelva un str que diga Hola[NOMBRE]
---------------------------------------------------------------------------
ahora necesito que hagas un script que se encargue de sumar dos enteros pasados como parametros en una funcion, dame tres ejemplos de distintas formas de hacerlo y dime cual es la mas adecuada
-------------------------------------------------------------------------
ahora quiero que generes el script de una funcion que:
verifica que un parametro edad de tipo int sea mayor o igual a 18
que devuelva true si se cumple la condicion
que devuelva false en caso contrario
---------------------------------------------------------------------------
ahora quiero el script de una funcion que, al pasarle un parametro llamado valor:
devuelva un string con el tipo de dato del valor recibido
----------------------------------------------------------------------------
ahora necesito un script de una funcion que tiene como parametro un valor de tipo str que debe:
devolver el string numerico como un float
-----------------------------------------------------------------------------

**Resultado obtenido**:
Por como hice el primer prompt, la ia me genero siempre tres formas de codigo distintas enumerando sus ventajas y desventajas y donde seria mas practico utilizarlas

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual porque me parecio correcto el razonamiento que me dio para elegir la opcion simple
---

### 2 - condicionales.py

**Herramienta**: GitHub Copilot

**Prompt usado**: Esta vez probe en utilizar un prompt mas largo pero que utilice todo el archivo como referencia en vez de pasarle por el prompt cada funcion, el prompt en cuestion es este:
Quiero completar todas las funciones que estan en este archivo con las condiciones que estan escritas entre comillas en cada funcion.
Quiero que me vayas haciendo 3 preguntas por cada funcion que puedan servir para generar el codigo deseado y al terminar las tres preguntas me des el script de esa funcion antes de comenzar con las preguntas de la siguiente funcion
> 

**Resultado obtenido**: La ia me fue dando 3 preguntas de cada funcion y en base a mi respuestas creo el codigo solicitado


**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual ya que ya estaba personalizado por las preguntas

---

### 3 - listas.py

**Herramienta**: GitHub Copilot

**Prompt usado**: 
Quiero que revises todo el archivo y que por cada funcion:
1_ me preguntes si no entendiste el retorno de la funcion
2_ crees un script para resolver la funcion
3_ enumeres casos bordes que deberia testear
4_ vayas haciendo pausas entre cada funcion y me preeguntes para continuar con la siguiente
5_ dame dos opciones de script y dime porque tendria que elegir la que recomiendas

> 

**Resultado obtenido**: Tal cual lo pedi me dio un par de opciones de script enumerando los casos borde que revisar y diciendome que habia entendido del retorno


**¿Lo usaste tal cual o lo modificaste?**
Tal cual

---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: GitHub Copilot

**Prompt usado**:Quiero que revises todas las funciones de este archivo y hagas lo siguiente por cada funcion:
1_ plantear 3 enfoques distintos para resolver la funcion
2_ enumerar pros y contras y que casos NO abarca cada enfoque
3_ espera que te indique el enfoque elegido y armame el script con el enfoque mencionado
> 

**Resultado obtenido**: me paso 3 enfoques por cada funcion mostrando pros y contras y los casos que no abarcaban y yo elegi los enfoques para la generacion del script


**¿Lo usaste tal cual o lo modificaste?**
tal cual

---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
Depende mucho la forma en que lo preguntes el resultado que te dara la ia, es muy util hacerla reflexionar y pedirle pros y contras o que cuestione sus propias decisiones.
- ¿En qué casos la IA fue útil y en cuáles no?
En general fue util en todos los casos
- ¿Qué harías diferente la próxima vez?
probaria con juntar todas las preguntas que le hice
