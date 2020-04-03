Xestión SAT 
==========

Proxecto SXE: Curso 2019 - 2020
------------------------------


Fco. Javier González Campos
---------------------------

a18franciscogc@iessanclemente.net

<https://github.com/a18franciscogc/xestionSAT.git>

## 1. Plantexamento
   
### 1.1. Propósito

Preténdese modelar un módulo que facilite o rexistro das intervencións técnicas sobre un ou varios Equipos relacionados cuns clientes (Partners) e a consulta do histórico das mesmas.

### 1.2. Funcionalidades

 * Dar de alta unha Incidencia
 * Rexistrar unha Actuación sobre unha Incidencia dada
 * Crear novas Accións para poder asignar a unha Actuación
 * Crear Actuacións sen ser unha Acción rexistrada
 * Dar de alta un Equipo
 * Rexistrar/Editar/Borrar un Compoñente dun Equipo
  
### 2.3. Táboas

#### 3.1 Táboas modificadas

* ProductTemplate (Incluír tipo de produto `Acción de SAT`)

#### 3.2. Táboas creadas

* Equipos
* ComponhentesEquipo
* Incidencias
* EstadosIncidencia
* LugaresIncidencia
* ActuacionsIncidencia (sobre as incidencias, serán produtos asociados)
 
## 2. Estratexia de ramificación e etiquetaxe

### 2.1. Ramas

Decidín ramificar o proxecto do seguinte xeito:

| RAMA              | PROPÓSITO
|:-                 |:-
| master            | Integrar as versións listas para produción das outras ramas
| documentacion     | Desenvolvemento da documentación do proxecto
| modulo_odoo       | Desenvolvemento dó módulo de Odoo

### 2.2. Etiquetas

O modelo da etiquetas será o seguinte `<prefixo><número versión>-<nome da rama>`, exemplo:

```
a0.9.0-modulo_odoo
v1.0.0-modulo_odoo
```

| PREFIXOS  | PROPÓSITO
|:-         |:-
| a         | Versión en probas (alfa) aínda sen test completo
| v         | Versión estable (release branch) para implementar en produción


## 3. Chagelog

[changelog]

[//]: # (Listado dos links empregados)

   [changelog]: <doc/changelog.md>

   <!-- Cógigo fonte -->

   [Buffer.java]: <../../src/main/java/psp/ejercicio01/Buffer.java>

   [Consumidor.java]: <../../src/main/java/psp/ejercicio01/Consumidor.java>

   [Productor.java]: <../../src/main/java/psp/ejercicio01/Productor.java>