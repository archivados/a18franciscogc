# IDEA DO PROXECTO

## Propósito

O propósito deste módulo para a plataforma de software ERP [Odoo] é o de extender as funcionalidades deste para adaptarse ás necesidades dunha empresa que dispoña dun **Servizo de Atención Técnica** (**SAT**) para o rexistro das súas intervencións sobre un ou varios **Equipos** relacionados cos seus **Clientes**, a consulta do histórico e a documentación das mesmas.

Este é un software que intentará a atender tódolos aspectos posibles dun SAT profesional a través das seguintes funcionalidades:

* Dar de alta novas Incidencias
* Rexistrar Actuacións sobre unha Incidencia dada
* Crear novas Accións para poder asignar a unha Actuación
* Crear Actuacións sen ser unha Acción rexistrada previamente
* Dar de alta Equipos novos
* Rexistrar/Editar/Borrar Compoñentes dun Equipo
* Cambiar o estado operacional dun Equipo rexitrado (está funcionando, reparandose, de baixa...)
* **Incluír os traballos realizados no ciclo de facturación da empresa**

## Usuarios

O grupo de usuarios ós que vai dirixida está principalmente esta ferramenta é o todas aquelas PEMES que dispoñan dun **SAT** externo (para dar servizo ós seus clientes), aínda que tamén pode ser empregado para o uso interno (para resolver as súas propias incidenicas).

## Competencia

Existen moitas solucións para cubrir as necesidades que **xestiónSAT** intenta abordar, pero despois de algo máis de 15 anos de experiencia na administrción e mantemento de equipos informáticos non atopei ningún software que se adaptase ó 100% ás necesidades que tiña para a documentación e o seguimento das actividades profesionais realizadas.

Hai software como [GLPI] ou [OCS-Inventory] que cubren e superan o propósito deste proxecto, sen embargo o problema que é que son demasiado grandes para o público ó cal vai destinado. Estas solucións teñen tamén un gran hándicap e é que están pensadas só para xestionar as incidencias do parque informático dunha única empresa o cal non é adecuado para aquelas PEMES que necesiten atender a máis de un cliente.

Unha meta a longo prazo será a de integrar as excelentes funcionalidades que aportan tanto [GLPI] como [OCS-Inventory] no proxecto. Isto farase intentando empregar **xestiónSAT** como unha capa intermedia entre estas plataformas e [Odoo] para poder xeneralizar o seu emprego e así xestionar tódolos clientes de cada usuario.

Por outra banda, as alternativas que existen no mercado adoitan poñer o peso dunha incidencia no **equipo** sobre o cal se actúa. Este enfoque pode estar ben se pensamos en amañar un coche, unha lavadora ou incluso un ascesor, pero se pensamos nun sistema informático é claramente insuficiente, xa que un sistema informático pode estar composto por cantidade de equipos con entidade propia. Un motivo polo cal se distingue **xestiónSAT** da competencia é que o peso de toda a xestión está na **incidencia** en si mesma, que pode incluso existir sen ningún equipo asociado, ou pola contra asociarse a un número indeterminado de equipos, o cal outrogalle a flexibilidade suficiente como para adaptarse ó mercado dos seus competidores ademais de engadirlle un valor mís ó permitir que sexa o usuario o que escolla o xeito de traballar en cada situación.

Tamén ofrece a alternativa de dividir sistemas complexos, como os informáticos, en partes máis pequenas con entidade propia. Así poden ser intervidas por algún problema que non inflúa no normal funcionamento do sistema do que forman parte.

Isto fai que teña un gran punto ó seu favor con respecto a outros programas ó adaptarse mellor a cada cliente potencial e deste xeito podese levar unha mellor documentación e control do seu SAT.

## Oportunidade de negocio

Penso que si é viable acadar un rendemento económico deste proxecto por varias vías:

* Instalación do aplicativo en empresas do mercado ó que vai dirixido
* Mantemento das instalacións do aplicativo, ben sexa un mantemento resolutivo ou preventivo
* Dar soporte a tercerias empresas que decidan implementar este módulo, para si mesmos ou para os seus clientes
* Adaptación das funcionalidades do software a casuísticas particulares, axudando así a medrar o nicho de mercado
* Abrir a oportunidade de negocio ó ofrecerlle a posibilidade de adaptar outras características de [Odoo] ás necesidades particulares dos clientes ou xerar novos módulos para os mesmo demostrando ser especialistas nesta plataforma
* Ofrecer servizos de mantemento e soporte para [Odoo] en xeral

Tamén é posible sacar un rendemento ecónomico indirecto grazas as características do software libre, se logra ter certa acollida por parte da comunidade, como por exemplo:

* Minimizar os custes de mantemento e actualización do módulo xa que o desenvolvemento de novas características e a resolución de bugs estaría en mans, potencialmente, dun gran número de programadores e programadoras
* Posibiliddade de abarcar máis sectores de mercado xa que calquera podería partir deste proxecto como base para adaptalo a un uso que non se contemplase inicialmente
* Detección máis rápida de erros ó ter acceso a este software usuarios de todo o mundo, o cal facilita a súa solución
* Mellora das capacidades profesionais propias ó ter acceso ó código escrito por multitude de persoas e así ver disintas solucións a un problema dado (esto tamén se pode aplicar a calquera que vexa o código deste proxecto)

Este último bloque depende en gran medida da aceptación e promoción que se lle dea ó proxecto dentro da comunidade de software libre, pero aínda que non se acadesen estes beneficios, obtelos só sería posible por medio desta vía de licenzamento e no peor dos casos non implicaría ningún custe a adicional sobre a inversión necesaria para unha solución cunha licenza totalmente pechada, é polo tanto un punto de valor engadido o mero feito de ter a posibilidade de conseguir o apoio de outra xente para o mantemento do proxecto.

[//]: # (Listado dos links empregados)

   <!-- Enlaces a terceiros -->

   [Odoo]: <https://www.odoo.com/es_ES/>

   [GLPI]: <https://glpi-project.org/es/>

   [OCS-Inventory]: <https://ocsinventory-ng.org/?lang=en>