# MELLORAS

Por falta de tempo, e por estar fora do alcance inicialmente plantexado para o proxecto, non puiden impentar tódalas opcións que me gustaría neste traballo, aquí listo algunha(s).

## xestiónSAT-Contratos

Aínda que **xestiónSAT** pode axudarnos a controlar o noso Servizo de Asistencia Técnica (SAT) hai algunhas tarefas que poden ser algo tediosas se non se automátizan. Unha das tarefas máis comúns nun SAT é a de xestionar os contratos de mantemento con algún dos teus clientes, no que anticipe o pago dun servizo aínda non prestado.

Para cubrir esta necesidades (posta de manifesto por Javier Fernández Peón), pensei en desenvolver un módulo de [Odoo] a maiores de **xestiónSAT**, **xestiónSAT-Contratos**. Este módulo dependería, obviamente, do módulo principal do proxecto pero ademais do módulo [Crontract] da [OCA] que implementa dun xeito bastante eficicaz este aspecto.

O seguinte Diagrama de secuencia mostra a grandes rasgos as operacións necesarias para levar a cabo a integración:

![Diagrama Secuencia]

[//]: # (Listado dos links empregados)

   <!-- Enlaces a terceiros -->

   [Odoo]: <https://www.odoo.com/es_ES/>

   [OCA]: <https://odoo-community.org/>

   [Crontract]: <https://github.com/OCA/contract/tree/12.0/contract>

   <!-- Enlaces proxecto -->

   [Diagrama Secuencia]: <doc/img/9_melloras/Diagrama_xestionSATcontratos.png>