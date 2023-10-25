## Histórico de revisão

|    Data    | Versão |                     Descrição                      |                                Autor(es)                                 |
| :--------: | :----: | :------------------------------------------------: | :----------------------------------------------------------------------: |
| 26/09/2023 |  0.1   |        Criação e estruturação do documento         | Felipe Direito, </br> Luan Mateus |
| 24/10/2023 |  0.2   |        Atualização de Metodologia         | Luan Mateus |

## GUPTA

<p style="text-indent: 50px;text-align: justify;"> O Gupta (2008)¹ propõe que a definição da abordagem de desenvolvimento de software ideal deve ser baseada em uma série de critérios fundamentais. Esses critérios incluem as necessidades e requisitos específicos do projeto, o ambiente e a cultura organizacional em que o projeto será executado, o tamanho e a complexidade do projeto, os riscos envolvidos, o orçamento disponível e o prazo para a conclusão do projeto.
</p>

### Características dos Requisitos

| Requisitos | Cascata | Prototipação | Iterativo e Incremental | Evolutivo | Spiral | RAD |
| --- | --- | --- | --- | --- | --- | --- |
| Os requisitos são facilmente compreensíveis e definidos? (NÃO) | Sim | Não | Não | Não | Não | Sim |
| Mudamos os requisitos com bastante frequência? (SIM) | Sim | Não | Sim | Sim | Não | Sim |
| Podemos mudar os requisitos no início do ciclo? (SIM) | Sim | Não | Sim | Sim | Não | Sim |
| Os requisitos indicam um sistema complexo a ser construído? (NÃO) | Sim | Não | Não | Não | Não | Sim |

### Status da Equipe de Desenvolvimento

| Requisitos | Cascata | Prototipação | Iterativo e Incremental | Evolutivo | Spiral | RAD |
| --- | --- | --- | --- | --- | --- | --- |
| Menos experiência em projetos similares(NÃO) | Não | Sim | Não | Não | Sim | Não |
| Menos conhecimento de domínio (novidade na tecnologia) (NÃO) | Não | Sim | Não | Não | Não | Sim |
| Menos experiência nas ferramentas a serem utilizadas (NÃO) | Não | Sim | Sim | Sim | Não | Sim |
| Disponibilidade de treinamento, se necessário(SIM) | Não | Não | Sim | Sim | Não | Sim |

### Envolvimento do Usuário

| Requisitos | Cascata | Prototipação | Iterativo e Incremental | Evolutivo | Spiral | RAD |
| --- | --- | --- | --- | --- | --- | --- |
| Envolvimento do usuário em todas as fases (SIM) | Sim | Não | Sim | Sim | Sim | Não |
| Participação limitada do usuário(NÃO) | Sim | Não | Sim | Sim | Sim | Não |
| O usuário não tem experiência prévia de participação em projeto semelhante(SIM) | Não | Sim | Sim | Sim | Sim | Não |
| Os usuários são especialistas no domínio do problema (NÃO) | Sim | Não | Não | Sim | Sim | Não |

### Tipo de Projeto e Risco Associado

| Requisitos | Cascata | Prototipação | Iterativo e Incremental | Evolutivo | Spiral | RAD |
| --- | --- | --- | --- | --- | --- | --- |
| O projeto é aprimoramento do sistema existente (SIM) | Sim | Sim | Não | Não | Sim | Não |
| O financiamento é estável para o projeto(SIM) | Sim | Sim | Não | Não | Não | Sim |
| Altos requisitos de confiabilidade(SIM) | Não | Não | Sim | Sim | Sim | Não |
| Cronograma do projeto apertado(SIM) | Não | Sim | Sim | Sim | Sim | Sim |
| Uso de componentes reutilizáveis(NÃO) | Sim | Não | Sim | Sim | Não | Não |
| Os recursos (tempo, dinheiro, pessoas etc.) são escassos?(SIM) | Não | Sim | Não | Não | Sim | Não |

### Conclusão

- Cascata: 8
- Prototipação: 10
- **Iterativo e Incremental: 12**
- Evolutivo: 11
- Spiral: 11
- RAD: 9

<p style="text-indent: 50px;text-align: justify;"> Ao analisar cada uma das perguntas no contexto atual do projeto, obtivemos o resultado da metodologia Iterativo e Incremental. Essa é uma metodologia ágil e permite o desenvolvimento iterativo do software, com entregas incrementais ao longo do tempo. Ela se baseia na colaboração intensa entre a equipe de desenvolvimento e os stakeholders do projeto.</p>

## Metodologia

<p style="text-indent: 50px;text-align: justify;"> A abordagem que escolhemos para o nosso projeto é a abordagem ágil, com ciclo de vida iterativo incremental e utilizando o Scrum/XP para a execução do projeto. Optamos por essa configuração nos baseando no tamanho da nossa equipe, no prazo que foi estabelecido e também pela "informalidade" do projeto, uma vez que não é um projeto com altos risco e nem precisa ser tão documentado, nesse sentido, o Backlog como documentação de requisitos e a dinâmica iterativa das sprints darão um ritmo adequado para o desenvolvimento. 
</p>

<p style="text-indent: 50px;text-align: justify;"> Ao analisarmos as facetas do processo de ER, identificamos que a faceta mais adequada seria a do processo Participativo sendo ele iterativo e exploratório que se destaca pela estreita colaboração com um cliente específico ao longo de todo o ciclo de desenvolvimento. Esse método promove a exploração contínua das necessidades e expectativas do cliente, resultando em um software altamente adaptado às suas demandas específicas, devido ao surgimento de novos requisitos ao longo do projeto e com cliente definido, não voltado ao mercado.
</p>

Todas as atividades de Engenharia de Requisitos são realizadas durante a execução do Projeto:

- **Elicitação e Descoberta**: Essa atividade tem um foco logo no início do projeto para levantar os primeiros requisitos, ajudar no entendimento do problema e identificar necessidades e possíveis soluções. Entretanto, ela deve ocorrer espontâneamente ao longo de todo o ciclo de vida do produto.
- **Análise e Consenso**: Essa atividade é feita posteriormente ao levantamento inicial, com o objetivo de decidir se os requisitos estão alinhados com os objetivos do projeto, e identificar conflitos entre as parte interessadas.
- **Declaração**: Ela é executada juntamente com a atividade de Elicitação e Descoberta, a fim de comunicar os requisitos que estão sendo levantados.
- **Representação**: Para esse projeto, o tipo de representação será na sua grande maioria informal, e será desenvolvida ao decorrer das sprints.
- **Verificação e Validação**: Essa atividade também será realizada a cada ciclo (sprint), mais especificamente na planning, execução da sprint e na review.
- **Organização e Atualização**: Essa atividade está presente durante todo o andamento do projeto, sendo uma atividade primordial no início(planning) da sprint, e no final(revisão) da mesma.

Como pretendemos aplicar cada uma delas:

|    Atividade    | Método |                     Ferramenta                      |                                Entrega                                 | Cerimônia Scrum |
| :--------: | :----: | :------------------------------------------------: | :----------------------------------------------------------------------: | :--------------------: |
| Elicitação e Descoberta |  Entrevista, Brainstorming e Benchmarking (comparando com produtos similares)  |        Discord ou outra plataforma de vídeo chamadas e o Google Docs (para anotar o que está sendo declarado)         | Ideias dos possíveis requisitos em um arquivo texto e audiovisual caso a reunião seja gravada. |Ao decorrer de todo o desenvolvimento do projeto|
| Análise e Consenso |  Revisão por pares e Feedback dos Stakeholders   |        Discord e Google docs         | Lista refinada com o “esqueleto” dos requisitos contendo Título e uma breve descrição de cada um | Também está presente na elaboração do Backlog e na Planning |
| Declaração |  Histórias de Usuário   |      Google Docs e Excel  | Lista com os os requisitos funcionais e não funcionais | No desenvolvimento do Backlog e na Review (caso apareçam novos requisitos) | 
| Representação |  Mapas mentais, Wireframes e talvez alguns diagramas de casos de uso   |        Miro, Papel e draw.io         | Representações gráficas dos requisitos | Está presente nas Reviews, para que a visualização do que está sendo feito seja mais clara, tanto para o time de desenvolvimento quanto para o cliente |
| Verificação e Validação |  Análise da estrutura das US's, Revisão por pares utilizando Checklist   |        Google Sheets e Google Docs         | Lista com o que precisa ser alterado | Planning, Execução da Sprint e Review |
| Organização e Atualização |  Product Backlog e User Story Mapping   |        Google Docs e Miro         | Backlog (sempre atualizado) e o mapa de histórias | Está presente no desenvolvimento do Backlog e nas Plannings |

## Referências Bibliográficas

> ¹ GUPTA, S. Managing Iterative Software Development Projects. Auerbach Publications, 2008.</br>