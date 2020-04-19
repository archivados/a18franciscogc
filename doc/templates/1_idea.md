# IDEA DO PROXECTO

## Propósito

O propósito deste módulo para a plataforma de software ERP [Odoo] é o de extender as funcionalidades deste para adaptarse ás necesidades dunha empresa que dispoña dun **Servizo de Atención Técnica** (**SAT**) para o rexistro das súas intervencións sobre un ou varios **Equipos** relacionados cos seus **Clientes**, a consulta do histórico e a documentación das mesmas.

Este é un software que intentará a atender tódolos aspectos posibles dun SAT profesional a través das seguintes funcionalidades:

* Dar de alta novas Incidencias
* Rexistrar Actuacións sobre unha Incidencia dada
* Controlar o estado actual dunha Incidencia
* **Revisar as Incidencias rexistradas para cada Cliente e/ou para cada Equipo**
* Crear novas Accións para poder asignar a unha Actuación
* Crear Actuacións sen ser unha Acción rexistrada previamente
* Rexistrar/Editar/Borrar un Equipo
* Rexistrar/Editar/Borrar Compoñentes dun Equipo
* Cambiar o estado operacional dun Equipo rexitrado (está funcionando, reparandose, de baixa...)
* **Incluír os traballos realizados no ciclo de facturación da empresa**

## Usuarios

O grupo de usuarios ós que vai dirixida está principalmente esta ferramenta é o todas aquelas PEMES que dispoñan dun **SAT** externo (para dar servizo ós seus clientes), aínda que tamén pode ser empregado para o uso interno (para resolver as súas propias incidenicas).

## Competencia

Existen moitas solucións para cubrir as necesidades que **xestiónSAT** intenta abordar, pero despois de algo máis de 15 anos de experiencia na administrción e mantemento de equipos informáticos non atopei ningún software que se adaptase ó 100% ás necesidades que tiña para a documentación e o seguimento das actividades profesionais realizadas.

Hai software como [GLPI] ou [OCS-Inventory] que cubren e superan o propósito deste proxecto, sen embargo o problema que hai é que son demasiado grandes para o público ó cal vai destinado **xestiónSAT**. Estas solucións teñen tamén un gran hándicap e é que están pensadas só para xestionar as incidencias do parque informático dunha única empresa o cal non é adecuado para aquelas PEMES que necesiten atender a máis de un cliente.

Unha meta a longo prazo será a de integrar as excelentes funcionalidades que aportan tanto [GLPI] como [OCS-Inventory] no proxecto. Isto farase intentando empregar **xestiónSAT** como unha capa intermedia entre estas plataformas e [Odoo] para poder xeneralizar o seu emprego e así xestionar tódolos clientes de cada usuario que decida empregar esta solución.

Por outra banda, as alternativas que existen no mercado adoitan poñer o peso dunha incidencia no **equipo** sobre o cal se actúa. Este enfoque pode estar ben se pensamos en amañar un coche, unha lavadora ou incluso un ascensor, pero se pensamos nun sistema informático é claramente insuficiente, xa que un sistema informático pode estar composto por cantidade de equipos con entidade propia. Un motivo polo cal se distingue **xestiónSAT** da competencia é que o peso de toda a xestión está na **incidencia** en si mesma, que pode incluso existir sen ningún equipo asociado, ou pola contra asociarse a un número indeterminado de equipos, o cal outrogalle a flexibilidade suficiente como para adaptarse ó mercado dos seus competidores ademais de engadirlle un valor único ó permitir que sexa o usuario o que escolla o xeito de traballar en cada situación que lle xurda.

Tamén ofrece a alternativa de dividir sistemas complexos, como os informáticos, en partes máis pequenas con características propias. Así cada unha desas partes pode ser intervida por algún problema que as afecte individualmente que non necesariamente ten porque influír no normal funcionamento do sistema do que forman parte.

Todo isto fai que **xestiónSAT** teña varios puntos ó seu favor con respecto a outros programas ó adaptarse mellor a cada cliente potencial e deste xeito podese levar unha mellor documentación e control do seu SAT.

## Por que escoller Odoo como base?

Crear un proxecto de cero ten dende logo moitas ventaxas, como poden ser as seguintes:

* Defines o teu propio estándar
* Defines o seu alcance, o cal permite non facer máis do que necesitas
* Controlas mellor os cambios que sufre a plataforma

**Entón, por que escoller unha plataforma que xa está no mercado?**

É certo que perdes control se te tes que adaptar a un estándar alleo e se non formas parte da dirección do proxecto, pero dependendo da plataforma gañas moitas máis cousas das que perdes, en relación ós puntos enumerados antes podes gañar:

* **Calidade no proceso** ó ter que adaptarte a un estándar xa definido, sobre todo se é un proxecto veterano, gañas toda a experiencia que fai que este siga adiante e beneficiarte de todos eses procesos que xa están en marcha.
* **Engadir valor ó teu produto** xa que podes aproveitar todo o que xa ten o proxecto base e ademais darlle máis funcionalidades.
* **Despreocuparte do alleo o teu propósito**, xa que ó partir dunha base todo aquelo que teña que ver coa súa estabilidade e melloras de rendemento estarán coordinadas por outras persoas e ti podes dedicarte só a poñer a funcionar e mellorar a túa aplicación.

No caso de **xestiónSAT** a principal meta é a de xestionar un SAT profesional con tódalas súas complexidades, esto inclúe o ciclo de facturación das intervencións feitas pero, por que reinventar a roda? por que facer outro software máis para xestionar a facturación? realmente que se gaña?

Penso que o máis intelixente, a nivel de produtividade, é centrarte no modelo de negocio que mellor coñeces, para o que vai dirixida a túa solución e empregar toda a túa enerxía en facelo o mellor que poidas. Por iso, se tes a posibilidade de aproveitar unha plataforma que xa ten implementada parte das necesidades que pretendes cubrir, necesidades que ademais son comúns para unha gran cantidade de empresas, por que non empregala? por que non aproveitar o traballo de xente que leva anos atendendo un mercado de xeito solvente?

Está claro que [Odoo] é moito máis grande do que este proxecto pretende, pero ten a ventaxa de que é modular, instalas e empregas só o que necesitas. Por iso considero que non é nigunha desventaxa a magnitude de [Odoo], todo o contrario, permite chegar a máis público, empresas que teñan máis requisitos dos que podes atender, podese empregar [Odoo] para case calquer sector empresarial que te poidas plantexar instalando os módulos que sexan precisos para cada propósito.

Outra ventaxa importante é o plantexamento multiplataforma de [Odoo]. Ó ser un aplicativo que ten unha interface web permite que te esquezas de facer unha solución distinta para cada plataforma de escritorio e incluso móbil. Ó dispoñer dun framework propio para crear as pantallas coas que interactua o usuario (vistas) dá unha sensación de uniformidade entre tódalos módulos instalados, o cal dá unha transmite unha idea de integración entre con tódals aplicacións que xestionan incorporadas á plataforma e axuda ó usuario a aprender a interactuar do mesmo xeito con todas.

En resumo, a decisión de empregar [Odoo] como base para **xestiónSAT** foi tomada para:

* Poder centrarme no desenvolvemento dunha solución para o mercado que pretendo `tocar`
* Para ter a garantía dunha base sólida sobre a cal apoiarme
* Para aproveitar a flexibilidade de adaptación da plataforma para adaptarse a calquer mercado e así abrir oportunidades que non me plantexase de inicio
* Non discriminar ningunha plataforma de execución posible
* E dar a sensación de ter un produto que forma parte de algo máis grande

## Oportunidade de negocio

Ó ser un módulo para a plataforma de software [Odoo] este pode ser un bo "gancho" para recomendar a instalacion de **xestiónSAT** xa que non só se poderá levar a xestión das incidencias do **parque de equipos** dos **clientes** senón que tamén poderá centralizarse toda a xestión das súas **empresa** dende o propio [Odoo]: vendas, compras, facturación, contabilidade, xestión de persoal... e con **xestiónSAT** o seu SAT. Debido a isto penso que si é viable acadar un rendemento económico deste proxecto por varias vías:

* Instalación do aplicativo en empresas que xa teñan instalado [Odoo]
* Instalación do aplicativo en empresas do mercado ó que vai dirixido xunto con [Odoo] e neste caso a maiores abrense as seguintes oportunidades:
  * Ofrecer o servizo de instalación dos módulos precisos da plataforma para levar a xestión comercial da empresa
  * Migrar información de outras plataformas a [Odoo]
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

Este último bloque depende en gran medida da aceptación e promoción que se lle dea ó proxecto dentro da comunidade de software libre, pero aínda que non se acadesen estes beneficios, obtelos só sería posible por medio desta vía de licenzamento e no peor dos casos non implicaría ningún custe adicional sobre a inversión necesaria para a mesma solución cunha licenza totalmente pechada, é polo tanto un punto de valor engadido o mero feito de ter a posibilidade de conseguir o apoio de máis xente para o mantemento e evolución do proxecto.

[//]: # (Listado dos links empregados)

   <!-- Enlaces a terceiros -->

   [Odoo]: <https://www.odoo.com/es_ES/>

   [GLPI]: <https://glpi-project.org/es/>

   [OCS-Inventory]: <https://ocsinventory-ng.org/?lang=en>