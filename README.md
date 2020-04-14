[![logo]][repoProxecto]

# Proxecto fin de ciclo: **xestiónSAT**

## Descrición

Este módulo para a plataforma de software ERP [Odoo] pretende extender as funcionalidades deste para adaptarse a unha empresa que dispoña dun **Servizo de Atención Técnica** (**SAT**) e facilitar o rexistro das súas intervencións sobre un ou varios **Equipos** relacionados cos seus **Clientes** e a consulta do histórico das mesmas.

## Instalación / Posta en marcha

Para a posta en marcha deste módulo precisase instalar a plataforma de software [Odoo], recomendo a versión base da [OCA] (Odoo Community Association) dispoñible no seguinte enlace: [OCB]

Podese instalar todo o necesario por un dos seguintes métodos:

**1. Instalación automatizada:** Para facilitar a súa instalación ofrezo un [repositorio para o despregue de Odoo][repoOdoo] cun script para a automatización da descarga, instalación e parametrización do servizo de [Odoo] baseado na version [OCB]. O script é para o despregue nun entorno **`GNU/Linux`**, en concreto **`Debian 10`** e o punto de montaxe do directorio deste repositorio para a cal está configurado o script é `/var/odoo/`.

Para descar o repositorio debería empregarse o programa de terminal `git` coa seguinte instrucción:

``` bash
git clone --recurse-submodules https://gitlab.iessanclemente.net/a18franciscogc/odoo /var/odoo/
```

Así descargarase o reposistorio principal e os submodulos asociados incluíndo o [OCB] no lugar apropiado. Unha vez finalizada a descarga é recomendable modificar o contido do script **`/var/odoo/cfg-odoo/odoo_install_d10.sh`** para unha parametrización máis adecuada ó escenario concreto da instalación.

**2. Instalación manual:** Se non se quixese facer uso deste repositorio GIT para a posta a punto dos requisitos necesarios para por en marcha **xestiónSAT** recomendo que sigan as instrucións da fonte oficial para a [instalación de Odoo], despois do cal será necesario descargar o contido do [deste repositorio][repoProxecto] nun directorio de addons accesible dende a instancia de [Odoo] configurada.

**Opcional:** Se se quixese empregar [Odoo] como un servizo en liña ou nunha intranet local da empresa podese facer uso do seguinte [repositorio de drepregue nginx][repoNginx] para facilitar a súa configuración. Do mesmo xeito que co [repositorio para o despregue de Odoo][repoOdoo] é interesante a parametrización personalizada dos ficheiros descargados para unha mellor adaptación á causística partitular do despreguamento.

Despois de poñer en marcha [Odoo] por calquera dos xeitos anteriormente descritos hai que ir á sección de aplicacións e buscar o módulo de nome **xestiónSAT** na lista e instalalo dende ahí para (é necesario quitar calquera filtro preconfigurado por [Odoo]).

## Emprego

Con este software poderase ampliar o funcionamento do ERP [Odoo] para incluír as seguintes funcionalidades para o manexo do SAT dunha empresa:

* Dar de alta unha nova Incidencia
* Rexistrar unha Actuación sobre unha Incidencia dada
* Crear novas Accións para poder asignar a unha Actuación
* Crear Actuacións sen ser unha Acción rexistrada
* Dar de alta un Equipo novo
* Rexistrar/Editar/Borrar un Compoñente dun Equipo
* Cambiar o estado operacional dun Equipo rexitrado (está funcionando, reparandose, de baixa...)
* **Incluír os traballos realizados no ciclo de facturación da empresa**

## Sobre o autor

**Contacto:** a18franciscogc@iessanclemente.net

O meu nome é **Fco. Javier González Campos** e son técnico superior en **ASI** (Administración de Sistemas Informáticos) e **DAM** (Desenvolvemento de Aplicacións Multiplataforma) `(espero que en breve)`, tamén son membro de **Inestable** (a Asociación de Usuarios de GNU/Linux de Ordes) aínda que actualmente estamos sen actividade pública.

Algunhas das tecnoloxías que domino son:

* Sistemas Operativos GNU/Linux e Windows (estacións de traballo e servidores)
* Administración de redes
* Linguaxes de programacións: `Java, Python, VB.NET, C#, C/C++ e Pascal`
* Sistemas Xestores de BD: `MySQL, MS SQL Server, MongoDB, PostgreSQL e Oracle`

Despois de algo máis de 15 anos de experiencia na administrción e mantemento de equipos informáticos non atopei ningún software que se adaptase ó 100% ás necesidades que tiña para a documentación e o seguimento das actividades profesionais realizadas. Por ese motivo decidín iniciar este proxecto e así tentar cubrir esas demandas intentando xeneralizar o proxecto todo o posible para abarcar o mair número de sectores e calquera outro con requisitos parecidos.

## Licenza

Este software licensase baixo as condicións descritos no ficheiro [LICENSE.md] que se incormpora na raíz desde repoisitorio. Dito ficheiro describe unha licenza [GNU-AGPL] da [FSF] (Free Software Foundation).

## Limitación de responsabilidades

Os autores de **xestiónSAT** non se fan responsables, baixo ningunha circunstacia, de posibles danos nin indemnizacións, moral ou patrimonial; directos ou indirectos; polo uso deste software ou pola perdida, parcial ou total, da información introducida polo mencionado software. O anterior inclúe os gastos asociados á fallas de comunicación e/ou de funcionamento de equipos informáticos vinculados co depregamento preciso para o seu emprego.

## Notificar un erro

Se atopaches un erro por favor acude á sección [Notificando unha incidencia][NovaIncidencia] do ficheiro [CONTRIBUTING] e notificao, agradezoche toda a axuda que poidas ofrecer.

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

Antes de nada quero agradecerche se estás interesado en contribuír a este pequeno proxecto, no seguinte documento [CONTRIBUTING] están as redactadas os xeitos nos que poderías axudar, gracias.

## Links

| ENLACE                                        | DESTINO
|:-                                             |:-
| [FSF]                                         | Free Software Foundation
| [GNU-AGPL]                                    | Licenza GNU-AGPL
| [Odoo]                                        | Software ERP Odoo
| [Instalación de Odoo]                         | Documentación oficial de instalación de Odoo
| [OCA]                                         | Odoo Community Association
| [OCB]                                         | Repositorio do software de Odoo Community Base
| [Repositorio Proxecto][repoProxecto]          | Repositorio deste proxecto
| [Repositorio de despregue de Odoo][repoOdoo]  | Repositorio con script e ficheiros de configuración para a automatización do despregue da [OCB]
| [Repositorio de drepregue nginx][repoNginx]   | Repositorio con script e ficheiros de configuración para o despregue dunha intranet con [nginx]

[//]: # (Listado dos links empregados)

   <!-- Licencia -->

   [LICENSE.md]: <LICENSE.md>

   <!-- Guía de contribución -->

   [CONTRIBUTING]: <CONTRIBUTING.md>
   [NovaIncidencia]: <CONTRIBUTING.md#notificando-unha-incidencia>

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

   [repoProxecto]: <https://gitlab.iessanclemente.net/damo/a18franciscogc.git>

   [repoOdoo]: <https://gitlab.iessanclemente.net/a18franciscogc/odoo.git>

   [repoNginx]: <https://gitlab.iessanclemente.net/a18franciscogc/nginx.git>