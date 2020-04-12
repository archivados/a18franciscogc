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

O modelo da etiquetas será o seguinte `<prefixo><número versión odoo><número versión módulo><compilación>-<nome da rama><sufixo>`, exemplo:

```
a12.9.0-modulo_odoo
b12.9.3-modulo_odoo
b12.9.5rc-modulo_odoo
v12.1.0-modulo_odoo
```

| PREFIXOS  | PROPÓSITO
|:-         |:-
| a         | Versión en probas (alfa) aínda sen test completo
| b         | Versión en probas (beta) aínda sen test completo
| v         | Versión estable (release branch) para implementar en produción


| SUFIXOS  | PROPÓSITO
|:-         |:-
| rc        | Versión na última fase de probas antes de ser promovida como versión en produción (release candidate)

