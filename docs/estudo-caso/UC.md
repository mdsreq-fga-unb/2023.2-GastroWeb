## Histórico de revisão

|    Data    | Versão |              Descrição              |  Autor(es)  |
| :--------: | :----: | :---------------------------------: | :---------: |
| 06/12/2023 |  0.1   | Criação e estruturação do documento | Lucas Andrade |

## Casos de Uso - VoyageX

<p style="text-align: justify">

Com base no estudo de caso do "VoyageX", desenvolvemos um diagrama de caso de uso, capturando as interações fundamentais entre usuários (viajentes e provedores de serviço) e o sistema. As relações de extensão e inclusão foram utilizadas para aprimorar a compreensão e a consistência, a fim de proporcionar uma base para o desenvolvimento do aplicativo "VoyageX" (caso fosse ser desenvolvido).

</p>
Abaixo está o nosso diagrama de casos de uso:

<div style="text-align: center; margin: 3px">
Diagrama 1 - Caso de Uso "VoyageX"
<img src="https://github.com/mdsreq-fga-unb/2023.2-GastroWeb/blob/GitPages/docs/images/UC_VOYAGEX.png?raw=true" alt="UC" style="width: 50rem">
Fonte: Facção Tanás, 2023.
</div>

## Especificação dos casos de uso

### 1. Pesquisar Informações Detalhadas

**Descrição:**

<div style="text-align: justify">
Este caso de uso permite ao usuário pesquisar informações detalhadas sobre acomodações e atividades, incluindo detalhes específicos, disponibilidade e opções de reserva.
</div>

**Fluxo Básico:**

1. O usuário acessa a função de pesquisa de informações detalhadas.

2. O usuário seleciona entre "Buscar Acomodações" e "Buscar Atividades".

3. O usuário define critérios de busca: preço, localização e tipo.

4. O aplicativo apresenta uma lista de resultados que correspondem aos critérios definidos. (FA1)

5. O usuário pode visualizar detalhes: descrição, fotos e avaliações. (FA2)

6. O usuário pode selecionar "Ver Detalhes e Disponibilidade de Reserva."

**Fluxos Alternativos:**

A1. Resultado de busca não encontrado (entra no passo 4. do fluxo básico)

1. O aplicativo notifica o usuário e sugere ajustes nos parâmetros de pesquisa

A2. Não visualizar detalhes (entra no passo 5. do fluxo básico)

1. Se o usuário decidir não visualizar detalhes e disponibilidade de reserva, o caso de uso é encerrado.

**Requisitos Especiais:**

1. O sistema deve retornar os resultados de acordo com os filtros selecionados pelo usuário.

2. As avaliações de outras atividades do usuário podem influenciar a ordem ou destaque dos resultados.

**Pré-condições:**

- O usuário está autenticado no aplicativo.

**Pontos de Extensão:**

- Após encontrar uma acomodação ou atividade desejada, o usuário pode iniciar os casos de uso "Buscar Acomodações" ou "Buscar Atividades."

### 2. Buscar Acomodações

**Descrição:**

<div style="text-align: justify">

Este caso de uso estende o caso de uso "Pesquisar Informações Detalhadas" e permite ao usuário buscar especificamente por acomodações com base em critérios como preço, localização, tipo e avaliações.

</div>

**Fluxo Básico:**

1. O usuário seleciona a opção "Buscar Acomodações" durante o caso de uso "Pesquisar Informações Detalhadas."

2. O usuário define critérios de busca para acomodações.

3. O aplicativo apresenta uma lista de acomodações que correspondem aos critérios definidos. (FA1)

**Fluxos Alternativos:**

A1. Busca sem resultados (entra no passo 3. do fluxo básico)

1. O aplicativo notifica o usuário e sugere ajustes nos parâmetros de pesquisa.

**Requisitos Especiais:**

- O sistema deve integrar avaliações de outras atividades do usuário para influenciar a ordem ou destaque das acomodações na lista de resultados.

**Pré-condições:**

- O usuário precisa ter executado o caso "Pesquisar informações detalhadas".

**Pontos de Extensão:**

- Após encontrar uma acomodação desejada, o usuário pode iniciar o caso de uso "Ver Detalhes e Disponibilidade de Reserva."

### 3. Buscar Atividades

**Descrição:**

<div style="text-align: justify">

Este caso de uso estende o caso de uso "Pesquisar Informações Detalhadas" e permite ao usuário buscar especificamente por atividades com base em critérios como tipo, preço e avaliações.

</div>

**Fluxo Básico:**

1. O usuário seleciona a opção "Buscar Atividades" durante o caso de uso "Pesquisar Informações Detalhadas."

2. O usuário define critérios de busca para atividades.

3. O aplicativo apresenta uma lista de atividades que correspondem aos critérios definidos. (FA1)

**Fluxos Alternativos:**

A1. Busca sem resultados (entra no passo 3. do fluxo básico)

1. O aplicativo notifica o usuário e sugere ajustes nos parâmetros de pesquisa.

**Requisitos Especiais:**

- O sistema deve integrar avaliações de outras atividades do usuário para influenciar a ordem ou destaque das atividades na lista de resultados.

**Pré-condições:**

- O usuário precisa ter executado o caso "Pesquisar informações detalhadas".

**Pontos de Extensão:**

- Após encontrar uma atividade desejada, o usuário pode iniciar o caso de uso "Ver Detalhes e Disponibilidade de Reserva."
