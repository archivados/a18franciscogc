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

Existen moitas solucións para cubrir as necesidades que **xestiónSAT** intenta aportar pero despois de algo máis de 15 anos de experiencia na administrción e mantemento de equipos informáticos non atopei ningún software, alo menos libre, que se adaptase ó 100% ás necesidades que tiña para a documentación e o seguimento das actividades profesionais realizadas. Hai software como [GLPI] ou [OCS-Inventory] que cubren e superan o propósito deste proxecto, sen embargo o problema que é que son demasiado grandes para o público ó cal vai destinado este proxecto e un gran inconveniente é que están pensadas só para xestionar as incidencias do parque informático só da propia empresa o cal non é adecuado para aquelas PEMES que necesiten atender a máis de un cliente.

Unha meta a longo prazo será a de integrar as excelentes funcionalidades que aportan tanto [GLPI] como [OCS-Inventory] intentando empregar **xestiónSAT** como unha capa intermedia entre estas plataformas para poder xeneralizar o seu emprego para varios clientes.

## Oportunidade de negocio

Penso que si é viable acadar un rendemento económico deste proxecto por varias vías:

* Instalación do aplicativo no mercado ó que vai dirixido
* Mantemento das instalacións do aplicativo, ben sexa un mantemento resolutivo ou preventivo
* Dar soporte a tercerias empresas que decidan implementar este módulo, para si mesmos ou para os seus clientes
* Adaptación das funcionalidades do software a casuísticas particulares, axudando así a medrar o nicho de mercado
* Abrir a oportunidade de negocio ó ofrecerlle a posibilidade de adaptar outras características de [Odoo] ás necesidades particulares dos clientes ou xerar novos módulos para a mesma demostrando ser especialista nesta plataforma
* Ofrecer servizos de mantemento e soporte para [Odoo] en xeral

Tamén é posible sacar un rendemento ecónomico indirecto grazas as características do software libre se logra ter certa acollida por parte da comunidade, como por exemplo:

* Minimizar os custes de mantemento e actualización do módulo xa que o desenvolvemento de novas características e a resolución de bugs estaría en mans, potencialmente, dun gran número de programadores e programadoras
* Posibiliddade de abarcar máis sectores de mercado xa que calquera podería partir deste proxecto como base para adaptalo a un uso que non se contemplase
* Detección máis rápida de erros ó ter acceso a este software usuarios de todo o mundo, o cal facilita a súa solución
* Mellora das capacidades profesionais propias ó ter acceso ó código escrito por multitude de persoas

Este último bloque depende en gran medida da aceptación e promoción que se lle dea ó proxecto pero aínda que non se acaden estes beneficios son posibilidades que só se poden obter con esta vía, no peor dos casos non implicaría nngún custe a maoires ós dunha solución pechada.

[//]: # (Listado dos links empregados)

   <!-- Enlaces a terceiros -->

   [Odoo]: <https://www.odoo.com/es_ES/>

   [GLPI]: <https://glpi-project.org/es/>

   [OCS-Inventory]: <https://ocsinventory-ng.org/?lang=en>