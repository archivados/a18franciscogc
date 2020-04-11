[![logo]][repositorio deste proxecto]

# Proxecto fin de ciclo: **Xestión SAT**

## Descrición

Este módulo para a plataforma de software ERP [Odoo] pretende extender as funcionalidades deste para adaptarser a unha empresa que dispoña dun Servizo de Atención Técnica (SAT) e facilitar o rexistro das súas intervencións sobre un ou varios Equipos relacionados cos seus Clientes e a consulta do histórico das mesmas.

### Funcionalidades

 * Dar de alta unha Incidencia
 * Rexistrar unha Actuación sobre unha Incidencia dada
 * Crear novas Accións para poder asignar a unha Actuación
 * Crear Actuacións sen ser unha Acción rexistrada
 * Dar de alta un Equipo
 * Rexistrar/Editar/Borrar un Compoñente dun Equipo

## Instalación / Posta en marcha

Para a posta en marcha deste módulo precisase instalar a plataforma de software [Odoo], recomendo a versión base da [OCA] (Odoo Community Association) dispoñible no seguinte enlace: [OCB]

Podese instalar todo o necesario por un dos seguintes métodos:

**1. Instalación automatizada:** Para facilitar a súa instalación ofrezo un [repositorio despregue de Odoo] cun script para a automatización da descarga, instalación e parametrización do servizo de Odoo para un entorno GNU/Linux. Unha vez descargado o contido do repositorio é recomendable modificar o seu contido para unha parametrización máis adecuada a cada escenario de emprego.

**2. Instalación manual:** Se non se quixese facer uso destes repositorios de GIT para a posta a punto dos requisitos recomendo que sigan as instrucións da fonte oficial para a [instalación de Odoo]. Despois do cal será necesario descargar o contido do [repositorio deste proxecto] nun direcctorio de addons accesible dende a instancia de Odoo configurada.

**Opcional:** Se se quixese empregar Odoo como un servizo en liña ou na intranet da empresa podese facer uso do seguinte [repositorio drepregue nginx] para facilitar a súa configuración. Do mesmo xeito que co [repositorio despregue de Odoo] é interesante a parametrización personalizada dos ficheiros descargados para unha mellor adaptación á causística partitular de despregue.

Despois de poñer en marcha [Odoo] por calquera dos xeitos anteriormente descritos hai que ir á sección de aplicacións e buscar o módulo de nome `xestionSAT` na lista e instalalo dende ahí para (é necesario quitar calquera filtro preconfigurado por Odoo).

## Emprego

> *TODO*: Es este apartado describe brevemente cómo se usará el software que proyectas. Si tiene una interfaz de terminal, describe aquí su sintaxis. Si tiene una interfaz gráfica de usuario, describe aquí **sólo el uso** (a modo de sumario) **de los aspectos más relevantes de su funcionamiento** (máxima brevedad, como si fuese un anuncio reclamo o comercial).
> 
> Si tu proyecto es documental, realiza una especificación de cómo planteas estas interfaces, con ejemplos incluso o esquemas de diseño. En otras palabras, realiza este apartado independientemente que no haya implementación.

## Sobre o autor

**Contacto:** a18franciscogc@iessanclemente.net

O meu nome é **Fco. Javier González Campos** e son técnico superior en ASI (Administración de Sistemas Informáticos) e DAM (Desenvolvemento de Aplicacións Multiplataforma) `(espero que en breve)`.

As tecnoloxías que domino son:

* Sistemas GNU/Linux e Windows
* Administración de redes
* Linguaxes de programacións: `Java, Python, VB.NET, C#, C/C++ e Pascal`
* Sistemas Xestores de BD: `MySQL, MS SQL Server, MongoDB, PostgreSQL e Oracle`

Despois de algo máis de 15 anos de experiencia na administrción e mantemento de equipos informáticos non atopei ningún software, alo menos libre, que se adaptase ó 100% ás necesidades que tiña para a documentación e o seguimento das actividades profesionais realizadas. Por ese motivo decidín iniciar este proxecto e así tentar cubrir esas demandas intentando xeneralizar o proxecto todo o posible para cubrir tódolos sectores posibles.

## Licenza

> Este licenzamento non é definitivo, teño que estudialo en profundidade polo cal de momento non é a licencia aplicable.

Este software licensase baixo as condicións descritos no ficheiro [LICENSE.md] que se incormpora na raíz desde repoisitorio. Dito ficheiro describe unha licenza [GNU-AGPL] da [FSF] (Free Software Foundation).


## Índice

1. [Idea]
2. [Necesidades]
3. [Análise]
4. [Deseño]
5. [Planificación]
6. [Implantación]
7. [Estratexia de versionado]
8. [Changelog]


## Guía de contribución

> *TODO*: Tratándose de un proyecto de software libre, es muy importante que expongas cómo se puede contribuir con tu proyecto. Algunos ejemplos de esto son realizar nuevas funcionalidades, corrección y/u optimización del código, realización de tests automatizados, nuevas interfaces de integración, desarrollo de plugins, etc. etc. Sé lo más conciso que puedas.

## Links

| ENLACE                            | DESTINO
|:-                                 |:-
| [FSF]                             | Free Software Foundation
| [GNU-AGPL]                        | Licenza GNU-AGPL
| [Odoo]                            | Software ERP Odoo
| [Instalación de Odoo]             | Documentación oficial de instalación de Odoo
| [OCA]                             | Odoo Community Association
| [OCB]                             | Repositorio do software de Odoo Community Base
| [Repositorio deste proxecto]      | Repositorio deste proxecto
| [Repositorio despregue de Odoo]   | Repositorio con script e ficheiros de configuración para a automatización do despregue da [OCB]
| [Repositorio drepregue nginx]     | Repositorio con script e ficheiros de configuración para o despregue dunha intranet con [nginx]

[//]: # (Listado dos links empregados)

   <!-- Licencia -->

   [LICENSE.md]: <LICENSE.md>

   <!-- Enlaces a terceiros -->

   [FSF]: <https://www.fsf.org/es>

   [GNU-AGPL]: <https://www.gnu.org/licenses/agpl-3.0.html>

   [Odoo]: <https://www.odoo.com/es_ES/>

   [Instalación de Odoo]: <https://www.odoo.com/documentation/12.0/setup/install.html>

   [OCA]: <https://odoo-community.org/>

   [OCB]: <https://github.com/OCA/OCB>

   [nginx]: <https://www.nginx.com/>

   <!-- Índice -->

   [Idea]: <doc/templates/1_idea.md>

   [Necesidades]: <doc/templates/2_necesidades.md>

   [Análise]: <doc/templates/3_analise.md>

   [Deseño]: <doc/templates/4_deseño.md>

   [Planificación]: <doc/templates/5_planificacion.md>
   
   [Implantación]: <doc/templates/6_implantacion.md>

   [Estratexia de versionado]: <doc/templates/7_versionado.md>

   [changelog]: <CHANGELOG.md>

   <!-- Enlaces proxecto -->

   [logo]: <doc/img/logo/xestionSAT_200x200.png>

   [repositorio deste proxecto]: <https://gitlab.iessanclemente.net/damo/a18franciscogc.git>

   [repositorio despregue de Odoo]: <https://gitlab.iessanclemente.net/a18franciscogc/odoo.git>

   [repositorio drepregue nginx]: <https://gitlab.iessanclemente.net/a18franciscogc/nginx.git>