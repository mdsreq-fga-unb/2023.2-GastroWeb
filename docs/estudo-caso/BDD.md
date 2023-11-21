## Histórico de revisão

|    Data    | Versão |              Descrição              |  Autor(es)  |
| :--------: | :----: | :---------------------------------: | :---------: |
| 20/11/2023 |  0.1   | Criação e estruturação do documento | Luan Mateus |

# Behavior Driven Development (BDD)

<p style="text-indent: 50px;text-align: justify;">Como atividade da unidade 3 da disciplina, foi solicitado que a equipe criasse o BDD da facção Gunthers a partir do estudo de caso "HealthNet".
Com isso, a equipe fez a atividade de engenharia de requisitos verificação e validação das Histórias de Usuário e os seus devidos Critérios de Aceitação.
</p>

## Verificação

- Para verificação das histórias de usuário, optamos por utilizar a técnica do INVEST, visto que todas as histórias possuem os devidos critérios de aceitação, portanto, é possível julgar a forma com que cada uma está escrita.
- O INVEST segue a seguinte lógica:
    - **I → Independente;**
    - **N → Negociável;**
    - **V → Valoroso;**
    - **E → Estimável;**
    - **S → História curta;**
    - **T → Testável;**

| User Story (Eu, como usuário, quero poder/devo ser capaz ..., para (valor de negócio) ) | I | N | N | E | S | T |
| --- | --- | --- | --- | --- | --- | --- |
| Eu, como recepcionista, desejo consultar informações pessoais dos pacientes para saber se o paciente já está registrado | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como recepcionista, desejo realizar cadastro dos pacientes para registrar novos pacientes | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como recepcionista, desejo atualizar informações dos pacientes para manter a consistência dos dados dos pacientes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como Médico Clínico Geral, desejo consultar o histórico do paciente para acessar as informações do histórico completo | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como Médico Clínico Geral, desejo buscar exames já realizados para identificar os problemas já enfrentados pelo paciente | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como Médico Clínico Geral, desejo buscar prescrições já realizadas para avaliar a eficácia dos medicamentos prescritos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como Médico Clínico Geral, desejo inserir notas das consultas para consultar informações importantes sobre as consultas anteriores | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como Médico Clínico Geral, desejo inserir prescrições medicamentosas para prescrever medicamentos para os pacientes, via sistema. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como farmacêutica, desejo verificar a prescrição médica do paciente para identificar os medicamentos prescritos. | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como farmacêutica, desejo registrar a dispensa do medicamento para identificar os medicamentos que foram dispensados para o paciente | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como farmacêutica, desejo verificar as interações medicamentosas para identificar possíveis interações entre fármacos. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como farmacêutica, desejo consultar informações das interações medicamentosas para averiguar o motivo das interações medicamentosas. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como coordenador de agendamento, desejo gerenciar agendamento de consultas para gerenciar as consultas. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como coordenador de agendamento, desejo detectar se há conflito no agendamento para detecção de possíveis conflitos de agendamento. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como coordenador de agendamento, desejo atualizar informações do agendamento para fazer ajustes facilmente. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como coordenador de agendamento, desejo notificar as consultas agendadas | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como Paciente, desejo consultar o resultado dos exames para consultar o resultado do exame de forma prática | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como paciente, desejo realizar agendamento online para ter praticidade ao marcar consultas. | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como paciente, desejo realizar cancelamento de consulta para evitar burocracia em cancelamentos. | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Eu, como paciente, desejo receber lembretes de medicações, para ser notificado quando um medicamento deve ser tomado | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Eu, como paciente, desejo receber lembretes de consultas futuras, para ser notificado quando perto de consultas futuras | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |

OBSERVAÇÕES:

💡 **As US 1.2, 2.1, 3.1, 3.2, 4.2, 5.1, 5.2, 6.1, 6.2, 6.4, 7.1, 7.3 e 8.2 possuem o mesmo impasse:**

- Dentro dos requisitos, a ideia desta funcionalidade faz sentido. No entanto, na forma como está escrita, o valor de negócio parece equivalente à ação ou atividade realizada. Em nossa análise, achamos que é importante encontrar outra maneira de agregar valor ao negócio.

- Com isso, fizemos as seguintes correções:
    - 1.2: Eu, como recepcionista, desejo realizar o cadastro de pacientes para facilitar o acesso à informações do mesmo.
    - 2.1: Eu, como Médico Clínico Geral, desejo consultar o histórico do paciente para obter informações relevantes para a consulta atual.
    - 3.1: Eu, como Médico Clínico Geral, desejo inserir notas das consultas para armazenar informações importantes para consultas posteriores
    - 3.2: Eu, como Médico Clínico Geral, desejo inserir prescrições medicamentosas para autorizar o paciente a retirar os medicamentos na farmácia.
    - 4.2: Eu, como farmacêutica, desejo registrar a dispensa do medicamento para que eu identifique, facilmente, quais medicamentos foram fornecidos para cada paciente.
    - 5.1: Eu, como farmacêutica, desejo verificar as interações medicamentosas para reduzir riscos do paciente ao combinar diferentes medicamentos.
    - 5.2: Eu, como farmacêutica, desejo consultar informações das interações medicamentosas para fornecer orientações precisas aos pacientes e profissionais de saúde envolvidos
    - 6.1: Eu, como coordenador de agendamento, desejo gerenciar agendamento de consultas para facilitar o agendamento de uma consulta médica.
    - 6.2: Eu, como coordenador de agendamento, desejo detectar se há conflito no agendamento para evitar que mais de uma consulta seja agendada no mesmo horário.
    - 6.4: Eu, como coordenador de agendamento, desejo notificar os pacientes sobre suas consultas agendadas para possibilitar que se organizem adequadamente para comparecer a elas.
    - 7.1: Eu, como paciente, desejo consultar o resultado dos exames para acompanhar o meu estado de saúde e tomar medidas apropriadas.
    - 7.3: Eu, como paciente, desejo realizar o cancelamento de consulta para identificação de não comparecimento da minha parte na consulta.
    - 8.2: Eu, como paciente, desejo receber lembretes de consultas futuras para me organizar adequadamente para comparecer a elas.

---

## Validação

- Verificar os seguintes aspectos de cada requisito:
    1. Necessário: o requisito é essencial para o sistema?
    2. Apropriado: possui detalhes apropriados à necessidade?
    3. Não Ambíguo: o requisito é fácil, simples e sem ambiguidade?
    4. Completo: o requisito deve descrever o que é necessário para que ele seja desenvolvido;
    5. Singular: O requisito deve descrever uma única necessidade;
    6. Viável: o requisito deve ser possível de ser realizado dentro das restrições do sistema (custo, cronograma);
    7. Verificável: o requisito deve ser metrificado, de forma que seja possível comprovar se ele foi desenvolvido ou não ao fim do processo;
    8. Correto: o requisito deve ser uma representação precisa da necessidade;
    9. Conforme: o requisito deve estar dentro do modelo e estilo padrão de requisitos de escrita, quando aplicável;

| Código User Story | User Story | Necessário | Apropriado | Não Ambíguo | Completo | Singular | Viável | Verificável | Correto | Conforme |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| US 1.1 | Eu, como recepcionista, desejo consultar informações pessoais dos pacientes para saber se o paciente já está registrado | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 1.2 | Eu, como recepcionista, desejo realizar cadastro dos pacientes para registrar novos pacientes | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 1.3 | Eu, como recepcionista, desejo atualizar informações dos pacientes para manter a consistência dos dados dos pacientes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 2.1 | Eu, como Médico Clínico Geral, desejo consultar o histórico do paciente para acessar as informações do histórico completo | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 2.3 | Eu, como Médico Clínico Geral, desejo buscar exames já realizados para identificar os problemas já enfrentados pelo paciente | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 2.4 | Eu, como Médico Clínico Geral, desejo buscar prescrições já realizadas para avaliar a eficácia dos medicamentos prescritos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 3.1 | Eu, como Médico Clínico Geral, desejo inserir notas das consultas para consultar informações importantes sobre as consultas anteriores | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 3.2 | Eu, como Médico Clínico Geral, desejo inserir prescrições medicamentosas para prescrever medicamentos para os pacientes, via sistema. | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 4.1 | Eu, como farmacêutica, desejo verificar a prescrição médica do paciente para identificar os medicamentos prescritos. | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 4.2 | Eu, como farmacêutica, desejo registrar a dispensa do medicamento para identificar os medicamentos que foram dispensados para o paciente | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 5.1 | Eu, como farmacêutica, desejo verificar as interações medicamentosas para identificar possíveis interações entre fármacos. | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 5.2 | Eu, como farmacêutica, desejo consultar informações das interações medicamentosas para averiguar o motivo das interações medicamentosas. | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 6.1 | Eu, como coordenador de agendamento, desejo gerenciar agendamento de consultas para gerenciar as consultas. | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 6.2 | Eu, como coordenador de agendamento, desejo detectar se há conflito no agendamento para detecção de possíveis conflitos de agendamento. | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 6.3 | Eu, como coordenador de agendamento, desejo atualizar informações do agendamento para fazer ajustes facilmente. | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 6.4 | Eu, como coordenador de agendamento, desejo notificar as consultas agendadas | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 7.1 | Eu, como Paciente, desejo consultar o resultado dos exames para consultar o resultado do exame de forma prática | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 7.2 | Eu, como paciente, desejo realizar agendamento online para ter praticidade ao marcar consultas. | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 7.3 | Eu, como paciente, desejo realizar cancelamento de consulta para evitar burocracia em cancelamentos. | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| US 8.1 | Eu, como paciente, desejo receber lembretes de medicações, para ser notificado quando um medicamento deve ser tomado | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US 8.2 | Eu, como paciente, desejo receber lembretes de consultas futuras, para ser notificado quando perto de consultas futuras | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |

OBSERVAÇÕES:

- As **US** **1.2, 2.1, 3.2, 4.1, 4.2, 6.1, 6.2, 7.1, 7.3 e 8.2** possuem a justificativa:
    - Itens 2, 8 e 9 por conta da forma como está escrita, o valor de negócio parece equivalente à ação ou atividade realizada.
- As **US 5.1 e 5.2** possuem a justificativa:
    - Itens 2, 3, 8 e 9 por conta da forma como está escrita, o valor de negócio parece equivalente à ação ou atividade realizada. Além disso, US 5.1 e 5.2 parecem tem ambiguidade, visto que uma fala sobre verificar e a outra consultar.
- A **US 6.4** possui a justificativa:
    - Itens 2, 4, 8 e 9 por conta da forma como está escrita, o valor de negócio parece equivalente à ação ou atividade realizada.

---

## BDD

Dessa maneira, o BDD está apresentado da seguinte forma:

**História de Usuário**

- Critérios de Aceitação

***Cenário: Título***

- Dado que **{contexto inicial}**

- Quando **{evento ou ação}**

- Então, **{resultado esperado}.**



**US 1.1: Eu, como recepcionista, desejo consultar informações pessoais dos pacientes para saber se o paciente já está registrado**

- Capacidade de Visualização de nome, data de nascimento, CPF, gênero, endereço e contatos.
- Visualizar as informações em documento, com os itens listados.

***Cenário: Consultar Paciente.***

**Dado** que o paciente já frequentou a clínica.

**Quando** o paciente for se apresentar para a consulta

**Então**, o histórico médico e as suas informações, tais como nome, data de nascimento, CPF, gênero, endereço e contatos devem constar no sistema.

---

**US 1.2: Eu, como recepcionista, desejo realizar o cadastro de pacientes para facilitar o acesso à informações do mesmo.**

- Capacidade de inserir nome, data de nascimento, CPF, gênero, endereço e contato.
- Os campos nome, CPF, data de nascimento, gênero e contato não devem ser deixados em branco.
- O sistema deve fornecer uma mensagem de cadastro concluído, caso tenha sucesso no cadastro
- Usuário já cadastros não devem ser registrados novamente, usando o campo CPF como parâmetro.

***Cenário: Cadastrar Paciente.***

**Dado** que o paciente nunca frequentou a clínica.

**Quando** o paciente for se apresentar para a consulta

**Então**, deve ser possível criar um cadastro com as informações nome, CPF, data de nascimento, gênero e contato, obrigatoriamente.

---

**US 1.3: Eu, como recepcionista, desejo atualizar informações dos pacientes para manter a consistência dos dados dos pacientes**

- Capacidade de modificar os campos Nome, data de nascimento, CPF, gênero, endereço e contato.
- O sistema deve fornecer uma mensagem de atualização concluída, caso tenha sucesso na atualização.

***Cenário: Atualizar Paciente.***

**Dado** que o paciente já frequentou a clínica e alterou seu número de contato.

**Quando** a clínica precisar ligar para ele

**Então**, deve ser possível editar seu cadastro para que se possa manter o contato.

---

**US 2.1: Eu, como Médico Clínico Geral, desejo consultar o histórico do paciente para obter informações relevantes para a consulta atual.**

- O médico deve ser capaz de acessar o histórico médico completo de um paciente, incluindo diagnósticos anteriores e tratamentos.
- As informações devem ser exibidas listadas em um documento PDF.

***Cenário: Consultar Histórico do Paciente.***

**Dado** que o paciente esteja sendo consultado.

**Quando** o médico precisar de acesso ao histórico do paciente

**Então**, deve ser possível visualizar e listar em um documento PDF o histórico do paciente tanto quanto diagnósticos e tratamentos anteriores.

---

**US 2.3: Eu, como Médico Clínico Geral, desejo buscar exames já realizados para identificar os problemas já enfrentados pelo paciente**

- O médico deve ser capaz de consultar todos os exames já prescritos para o paciente em algumas das unidades.
- O médico deve ser capaz de consultar os resultados de todos os exames encontrados.

***Cenário: Buscar exames.***

**Dado** que o paciente é reincidente na consulta médica.

**Quando** o paciente já estiver realizado exames no hospital.

**Então**, o histórico de exames e prescrições de exames devem constar no sistema.

---

**US 2.4: Eu, como Médico Clínico Geral, desejo buscar prescrições já realizadas para avaliar a eficácia dos medicamentos prescritos**

- O médico deve ser capaz de consultar todos os medicamentos já prescritos anteriormente.
- A habilidade de visualizar as informações detalhadas das prescrições anteriores, incluindo datas, medicamentos prescritos, doses, duração do tratamento e diagnósticos associados.

***Cenário 1: Buscar prescrições.*** 

**Dado** que o paciente é reincidente na consulta médica. 

**Quando** o paciente já tiver recebido prescrições médicas. 

**Então**, deve ser possível consultar o laudo com todas as prescrições anteriores, doses, duração do tratamento e diagnóstico.

---

**US 3.1: Eu, como Médico Clínico Geral, desejo inserir notas das consultas para armazenar informações importantes para consultas posteriores**

A capacidade de pesquisar e recuperar notas anteriores com base em critérios como nome do paciente, data da consulta ou palavras-chave.

As notas devem incluir informações de data, hora, identificação do paciente e descrição.

***Cenário 1: Adicionar notas***

Dado que a consulta médica está ocorrendo. 

Quando o médico solicitar uma anotação sobre a consulta. 

Então, a nota deve ser feita contendo a data da consulta, nome do paciente e a descrição que o médico desejar no sistema.

---

**US 3.2: Eu, como Médico Clínico Geral, desejo inserir prescrições medicamentosas para autorizar o paciente a retirar os medicamentos na farmácia.**

- O médico deve ser capaz de inserir a dose do medicamento, a frequência de uso e duração do tratamento.
- A prescrição deve conter dados como Nome e CPF do paciente para possível identificação.

***Cenário 1: Médico insere prescrição médica com informações.*
Dado** que o médico está consultando o paciente
**Quando** o médico preencher as informações de dose do medicamento, a frequência de uso e a duração do tratamento **E** o médico preencher as informações de Nome e CPF do paciente
**Então** a prescrição deve ser salva no sistema.

***Cenário 2: Médico insere prescrição médica sem informações*
Dado** que o médico está consultando o paciente
**Quando** o médico não preencher as informações de dose de medicamento, frequência de uso e a duração do tratamento **E** o médico não preencher as informações de Nome e CPF do paciente
**Então** uma mensagem de erro é exibida informando que os dados do paciente são obrigatórios.

---

**US 4.1: Eu, como farmacêutica, desejo verificar a prescrição médica do paciente para identificar os medicamentos prescritos.**

- A Farmacêutica deve ser capaz de pesquisar prescrições feitas pelo Médico pelo Nome e CPF do paciente no sistema.

***Cenário 1: Farmacêutica verifica prescrição médica*
Dado** que a farmacêutica está atendendo um paciente
**E** existem prescrições médicas registradas no sistema
**Quando** a farmacêutica realizar uma pesquisa das prescrições do paciente usando Nome e CPF
**Então** o sistema exibe todas as prescrições para o paciente.

---

**US 4.2: Eu, como farmacêutica, desejo registrar a dispensa do medicamento para que eu identifique, facilmente, quais medicamentos foram fornecidos para cada paciente.**

- A Farmacêutica deve ser capaz de inserir o Nome do medicamento e a data em que foi dispensado.

***Cenário 1: Farmacêutica dispensa medicamento*
Dado** que a farmacêutica está entregando o medicamento ao paciente
**Quando** a farmacêutica inserir o nome do medicamento e a data que foi entregue
**Então** a quantidade de medicamentos é atualizada
**E** a identificação do medicamento vai para o histórico do paciente.

---

**US 5.1: Eu, como farmacêutica, desejo verificar as interações medicamentosas para reduzir riscos do paciente ao combinar diferentes medicamentos.**

- O sistema deve, no ato da dispensa de medicamentos, alertar se houver interação entre um ou mais medicamentos Dispensados.

***Cenário 1: Farmacêutica recebe alerta de interação medicamentosa na dispensa)***

**Dado** que os medicamentos que serão dispensados têm interação medicamentosa conhecida.

**Quando** o farmacêutico for adicioná-los ao registro da dispensa.

**Então**, o sistema exibe um alerta de interação medicamentosa contendo detalhes sobre a interação, os medicamentos envolvidos e o tipo de interação

---

**US 5.2: Eu, como farmacêutica, desejo consultar informações das interações medicamentosas para fornecer orientações precisas aos pacientes e profissionais de saúde envolvidos.**

- O sistema deve conter todas as interações medicamentos existentes entre os medicamentos do sistema.
- O sistema deve fornecer uma descrição da interação Medicamentosa.

***Cenário 1: Farmacêutica consulta todas as interações medicamentosas***

**Dado** que o sistema contém as principais interações medicamentosas registradas.

**Quando** o farmacêutico faz uma consulta de um medicamento

**Então**, o sistema exibe todas as interações medicamentosas e suas respectivas descrições com aquele medicamento.

---

**US 6.1: Eu, como coordenador de agendamento, desejo gerenciar agendamento de consultas para facilitar o agendamento de uma consulta médica.**

- O sistema deve possuir campos para inserir o nome do paciente, selecionar a data e o horário da consulta, especificar o tipo de consulta e fornecer informações de contato.
- Os campos de nome do paciente, data e o horário consulta, tipo de consulta e informações de contato não devem ser deixados em branco.
- O sistema deve fornecer uma mensagem de agendamento concluído, caso tenha sucesso no agendamento.

***Cenário 1: Coordenador de agendamento agenda uma consulta com sucesso***

**Dado** que o coordenador deseja realizar um agendamento

**Quando** o coordenador preenche os campos obrigatórios: Nome do Paciente, Data da Consulta, Horário da Consulta, Tipo de Consulta, Informações de Contato e clica no botão de agendar consulta.

**Então** o sistema exibe uma mensagem de agendamento concluído com sucesso

---

**US 6.2: Eu, como coordenador de agendamento, desejo detectar se há conflito no agendamento para evitar que mais de uma consulta seja agendada no mesmo horário.**

- Se houver qualquer conflito de agendamento para o profissional ou sala associada à consulta selecionada, o sistema deve apresentar um alerta destacando os detalhes do conflito.
- O sistema deve fornecer opções para resolver conflitos, como a sugestão de horários alternativos ou a reatribuição de profissionais e recursos.

***Cenário 1: Coordenador de agendamento detecta conflito e o resolve***

**Dado** que o coordenador deseja realizar um agendamento e existem consultas previamente agendadas para o mesmo profissional ou sala.

**Quando** o coordenador tenta agendar uma nova consulta no mesmo horário

**Então**, o sistema exibe um alerta destacando os detalhes do conflito e fornece opções para resolver o conflito, como por exemplo: sugestões de horários alternativos. Após a resolução do conflito, o sistema exibe uma mensagem indicando que o agendamento foi concluído com sucesso.

---

**US 6.3: Eu, como coordenador de agendamento, desejo atualizar informações do agendamento para fazer ajustes facilmente.**

- A interface deve permitir a fácil identificação do agendamento a ser atualizado, exibindo informações relevantes, como nome do paciente, data e horário da consulta.

***Cenário: Visualização do agendamento.***

**Dado** que o coordenador de agendamento acessou a página de agendamento de consultas.

**Quando** o coordenador de agendamento digitar o nome do paciente, a data ou o horário da consulta.

**Então**, o sistema deverá mostrar o nome do paciente, a data e o horário da consulta pesquisada.

- O coordenador deve poder editar informações específicas do agendamento, como o nome do paciente, data e horário da consulta, tipo de consulta e informações de contato.

***Cenário: Editar dados do agendamento.***

**Dado** que o coordenador de agendamento acessou a página de agendamento de consultas e selecionou um agendamento.

**Quando** o coordenador de agendamento alterar o nome do paciente, a data da consulta, o horário da consulta, o tipo de consulta ou as informações de contato.

**Então**, o sistema deverá mostrar as informações atualizadas.

- O sistema deve realizar validação automática dos dados atualizados, garantindo a integridade das informações e evitando entradas inválidas.

***Cenário: Prevenção de erros.***

**Dado** que o coordenador de agendamento acessou a página de agendamento de consultas e selecionou um agendamento.

**Quando** o coordenador de agendamento alterar o nome do paciente, a data da consulta, o horário da consulta, o tipo de consulta ou as informações de contato.

**Então**, o sistema deverá fornecer formatação válida para cada tipo de informação do agendamento.

---

**US 6.4: Eu, como coordenador de agendamento, desejo notificar os pacientes sobre suas consultas agendadas para possibilitar que se organizem adequadamente para comparecer a elas.**

- O sistema deve oferecer opções para notificação, como emails, mensagens de texto (SMS) ou qualquer outro canal preferido pelos pacientes.

***Cenário 1: Notificação de agendamento via e-mail***

**Dado** que o paciente possui um e-mail válido cadastrado no sistema.

**Quando** o coordenador de agendamento clicar em notificar paciente.

**Então**, o sistema deverá enviar uma mensagem para o e-mail informado, contendo a data, horário e local da consulta.

***Cenário 2: Notificação de agendamento via SMS***

**Dado** que o paciente possui um número de telefone válido cadastrado no sistema.

**Quando** o coordenador de agendamento clicar em notificar paciente.

**Então**, o sistema deverá enviar uma mensagem para o número informado, contendo a data, horário e local da consulta.

***Cenário 3: Notificação de agendamento via WhatsApp***

**Dado** que o paciente possui um número de telefone válido cadastrado no sistema e que possui uma conta no WhatsApp.

**Quando** o coordenador de agendamento clicar em notificar paciente.

**Então**, o sistema deverá enviar uma mensagem para o número informado, contendo a data, horário e local da consulta.

- Além da notificação inicial, o sistema deve enviar lembretes automáticos em intervalos pré-determinados antes da data da consulta para minimizar faltas.

***Cenário 1: Notificação automática de agendamento via e-mail***

**Dado** que o paciente possui um e-mail válido cadastrado no sistema.

**Quando** o tempo para a consulta for de 48h, 24h e 4h.

**Então**, o sistema deverá enviar uma mensagem para o e-mail informado, contendo a data, horário e local da consulta.

***Cenário 2: Notificação automática de agendamento via SMS***

**Dado** que o paciente possui um número de telefone válido cadastrado no sistema.

**Quando** o tempo para a consulta for de 48h, 24h e 4h.

**Então**, o sistema deverá enviar uma mensagem para o número informado, contendo a data, horário e local da consulta.

***Cenário 3: Notificação automática de agendamento via WhatsApp***

**Dado** que o paciente possui um número de telefone válido cadastrado no sistema e que possui uma conta no WhatsApp.

**Quando** o tempo para a consulta for de 48h, 24h e 4h.

**Então**, o sistema deverá enviar uma mensagem para o número informado, contendo a data, horário e local da consulta.

---

**US 7.1: Eu, como paciente, desejo consultar o resultado dos exames para acompanhar o meu estado de saúde e tomar medidas apropriadas.**

- Deve haver a opção de baixar os resultados dos exames em formato PDF ou outro formato padrão.

***Cenário: Download do resultado do exame.***

**Dado** que o usuário acessou o resultado do exame.

**Quando** o usuário clicar em baixar PDF.

**Então**, o arquivo do exame deve ser baixado em formato PDF.

- Os resultados devem ser exibidos com informações relevantes, como data do exame, nome do exame, valores e dados pessoais do paciente.

***Cenário 1: Visualização do resultado do exame.***

**Dado** que o paciente acessou a página consultar resultado de exames e possui um CPF cadastrado no sistema.

**Quando** o paciente informar um CPF válido e confirmar.

**Então**, o sistema deverá mostrar o resultado do exame, informando o nome do exame, a data do exame, o valor do exame, o nome do paciente, o CPF do paciente, a idade do paciente, o sexo do paciente e o nome do médico que realizou o exame.

***Cenário 2: Falha na visualização do resultado do exame.***

**Dado** que o paciente acessou a página consultar resultado de exames e não possui um CPF cadastrado no sistema.

**Quando** o paciente informar um CPF e confirmar.

**Então**, o sistema deverá mostrar um aviso de que não foi possível encontrar o resultado do exame para o CPF informado.

---

**US 7.2: Eu, como paciente, desejo realizar agendamento online para ter**

**praticidade ao marcar consultas.**

- Deve ser possível visualizar os horários disponíveis para Consulta.

***Cenário: Visualização de horários.***
**Dado** que o paciente acessou a página de agendamento online.

**Quando** o paciente clicar em visualizar horários disponíveis.

**Então**, o sistema deve mostrar uma lista contendo as datas, horários e locais disponíveis.

- O sistema deve permitir que o paciente selecione um horário disponível para agendamento.

***Cenário: Seleção de horário do agendamento.***

**Dado** que o paciente acessou a página de agendamento online.

**Quando** o paciente clicar em um horário na lista de horários disponíveis.

**Então**, o sistema deverá mostrar uma mensagem para confirmação do horário escolhido.

- O sistema deve fornecer confirmação imediata do agendamento, indicando data, hora e local da consulta.

***Cenário: Agendamento de consulta.***

**Dado** que o paciente acessou a página de agendamento online.

**Quando** o paciente clicar em um horário na lista de horários disponíveis.

**Então**, o sistema deverá mostrar uma confirmação de que a consulta foi agendada com sucesso, indicando a data, hora e local da consulta.

---

**US 7.3: Eu, como paciente, desejo realizar o cancelamento de consulta para identificação de não comparecimento da minha parte na consulta.**

- O sistema deve solicitar uma confirmação antes de finalizar o cancelamento.
- Deve haver uma opção para fornecer uma razão opcional para o cancelamento da consulta.

***Cenário 1: Cancelamento bem-sucedido com confirmação e razão opcional***

**Dado** que sou um paciente com ao menos uma consulta agendada

**Quando** eu iniciar o processo de cancelamento de uma determinada consulta

**Então** o sistema deve exibir os detalhes da consulta acompanhados de um botão para confirmar o cancelamento e um campo para fornecer uma razão (campo preenchido de maneira opcional)

---

**US 8.1 Eu, como paciente, desejo receber lembretes de medicações, para ser notificado quando um medicamento deve ser tomado.**

- O Paciente deve ser capaz de definir o horário, a data e o nome do medicamento a ser tomado;
- A capacidade de o paciente optar por receber lembretes de medicações por meio de um aplicativo móvel, SMS, e-mail ou outra forma de comunicação preferida.

***Cenário 1: Definir lembrete de medicação com sucesso***

**Dado** que sou um paciente que tem pelo menos um remédio prescrito e desejo receber lembretes de medicações

**Quando** eu configurar um lembrete de medicação e especificar o horário, a data e o nome do medicamento.

**Então** o sistema deve confirmar o sucesso da configuração e sempre que a data e o horário definidos chegarem eu ser notificado

***Cenário 2: Configurar lembrete de medicação com campos em falta***

**Dado** que sou um paciente que tem pelo menos um remédio prescrito e desejo receber lembretes de medicações

**Quando** eu tentar configurar um lembrete de medicação sem especificar todos os detalhes necessários (horário, data, nome do medicamento)

**Então** o sistema deve exibir uma mensagem de erro indicando os campos obrigatórios e não deve aceitar a configuração do lembrete

***Cenário 3: Escolher rede comunicação para lembretes***

**Dado** que sou um paciente que desejo receber lembretes de medicações

**Quando** eu configurar a minha forma de comunicação preferida (aplicativo móvel, SMS ou e-mail)

**Então** o sistema deve confirmar o sucesso da configuração e sempre que um lembrete for enviado a rede de comunicação escolhida deve ser usada.

---

**US 8.2 Eu, como paciente, desejo receber lembretes de consultas futuras para me organizar adequadamente para comparecer a elas.**

- O paciente deve ser capaz de definir horário, data, nome do Médico e a especialidade.
- A capacidade de o paciente optar por receber lembretes de consultas por meio de um aplicativo móvel, SMS, e-mail ou outra forma de comunicação preferida.

***Cenário 1: Definir lembrete de consulta com sucesso***

**Dado** que sou um paciente que deseja receber lembretes de consultas futuras

**Quando** eu configurar um lembrete de consulta e especificar o horário, a data, o nome do médico e a especialidade

**Então** o sistema deve confirmar o sucesso da configuração e eu devo receber um lembrete 2 horas antes do horário especificado e outro no exato horário.

***Cenário 2: Configurar lembrete de consulta sem fornecer todos os detalhes***

**Dado** que sou um paciente que deseja receber lembretes de consultas futuras

**Quando** eu tentar configurar um lembrete de consulta sem especificar todos os detalhes necessários (horário, data, nome do médico, especialidade)

**Então** o sistema deve exibir uma mensagem de erro indicando os campos obrigatórios e não deve aceitar a configuração do lembrete de consulta.

***Cenário 3: Escolher formas de comunicação para lembretes de consulta***

**Dado** que sou um paciente que deseja receber lembretes de consultas futuras

**Quando** eu configurar um lembrete de consulta e escolher receber lembretes por meio de um aplicativo móvel, SMS ou e-mail

**Então** o sistema deve aceitar a forma de comunicação selecionada e eu devo receber lembretes 2 horas antes do horário especificado e outro no exato horário.