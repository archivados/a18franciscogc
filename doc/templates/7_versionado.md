# ESTRATEXIA DE VERSIONADO

A continuación veras unha breve descrición da estratexía de ramificación e de etiquetaxe das versións operativas do software.

## Ramas

Decidín ramificar o proxecto do seguinte xeito:

| RAMA              | PROPÓSITO
|:-                 |:-
| master            | Integrar as versións listas para produción das outras ramas
| documentacion     | Desenvolvemento da documentación do proxecto
| modulo_odoo       | Desenvolvemento dó módulo de Odoo
| modulo_odoo_test  | Test das versións alfa ou beta dó módulo de Odoo antes de pasalo a rama de produción

## Etiquetas

O modelo da etiquetas para o módulo de [Odoo] describirase na seguinte táboa:

| BLOQUE        | PROPÓSITO
|:-             |:-
| prefixo       | Indicará o tipo de estabilidade e madurez da compilación do módulo
| versión Odoo  | Indicará a versión de [Odoo] para a cal está deseñado e probado o módulo
| x             | Incrementos que incorporen un cambio no modelo de datos ou que supoñan cambios importantes. Pode supoñer que sexa preciso unha migración de datos ou que cambien as dependencias do módulo
| y             | Incrementos con novas funcionalidades estables. Pode supoñer unha actualización do módulo
| z             | Incrementos que solucionen erros (bugs)
| sufixo        | No caso de existir aportará información adicional sobre a madurez da compilación

Estas etiquetas serán idénticas á versión do manifesto do módulo a excepción dos prefixos e sufixos.

Exemplo:

``` bash
a12.0.0.9.0-modulo_odoo
b12.0.0.9.3-modulo_odoo
b12.0.0.9.5rc-modulo_odoo
v12.0.1.0.0-modulo_odoo
```

Información sobre os `prefixos` e os `sufixos`:

| PREFIXOS  | PROPÓSITO
|:-         |:-
| a         | Versión en probas (alfa) aínda sen test completo
| b         | Versión en probas (beta) aínda sen test completo
| v         | Versión estable (release branch) para implementar en produción

| SUFIXOS  | PROPÓSITO
|:-         |:-
| rc        | Versión na última fase de probas antes de ser promovida como versión en produción (release candidate)

[//]: # (Listado dos links empregados)

   <!-- Enlaces a terceiros -->

   [Odoo]: <https://www.odoo.com/es_ES/>