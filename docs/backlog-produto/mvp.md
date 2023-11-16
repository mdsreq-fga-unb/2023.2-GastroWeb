## MVP

| Id | Descrição |
| --- | --- |
| US03 | Eu, como administrador, desejo deletar as receitas gastronômicas para ter mais controle sobre o conteúdo do site. |
| US04 | Eu, como administrador, desejo visualizar as receitas gastronômicas para consultá-las sempre que quiser. |
| US02 | Eu, como administrador, desejo editar as receitas gastronômicas para ter mais flexibilidade sobre as receitas. |
| US01 | Eu, como administrador, desejo criar receitas gastronômicas para poder enriquecer o conteúdo do site aumentando a variedade de receitas culinárias. |
| US25 | Eu, como um usuário, quero exportar receitas em formato PDF para que eu consiga visualizar a receita offline e em outros dispositivos. | 
| US24 | Eu, como usuário, desejo compartilhar uma receita com outras pessoas para trocar experiências culinárias com amigos e familiares de forma rápida e conveniente. |
| US07 | Eu, como usuário, desejo buscar receitas por nome para encontrar rapidamente receitas específicas e facilitar o acesso a pratos de meu interesse. |
| US05 | Eu, como administrador, desejo inserir categorias nas receitas para organizar o conteúdo de forma estruturada. |
| US06 | Eu, como administrador, desejo inserir tags nas receitas para facilitar o agrupamento dos ingredientes que o prato possui. |
| US08 | Eu, como usuário, desejo filtrar receitas por categorias para encontrar os pratos de meu interesse mais eficientemente. |
| US09 | Eu, como usuário, desejo filtrar receitas por tags para encontrar os pratos com ingredientes de meu interesse mais eficientemente. |


## Critérios de Aceitação

**US03 -** Eu, como administrador, desejo deletar as receitas gastronômicas para ter mais controle sobre o conteúdo do site.

1. Deve haver um mecanismo de autenticação seguro para garantir que apenas administradores autorizados possam acessar essa funcionalidade.

2. Ao clicar para deletar uma receita, o sistema deve solicitar uma confirmação antes de realizar a exclusão.

**US04** - Eu, como administrador, desejo visualizar as receitas gastronômicas para consultá-las sempre que quiser.

1. Deve haver uma seção claramente identificada na interface do administrador para visualizar as receitas gastronômicas.

2. Ao clicar em uma receita na lista, o sistema deve exibir detalhes completos da receita, incluindo ingredientes, instruções de preparo, e outras informações relevantes.

**US02** - Eu, como administrador, desejo editar as receitas gastronômicas para ter mais flexibilidade sobre as receitas.

1. Todos os campos importantes de uma receita, como ingredientes, instruções de preparo, tempo de cozimento, devem ser editáveis.

2. Oferecer a opção de visualizar as alterações antes de salvá-las permanentemente

**US01** - Eu, como administrador, desejo criar receitas gastronômicas para poder enriquecer o conteúdo do site aumentando a variedade de receitas culinárias.

1. Definir campos essenciais, por exemplo, ( título, ingredientes e instruções) sendo obrigatórios para evitar receitas incompletas.

2. Permitir o upload de imagens e vídeos para ilustrar a receita.

3. Permitir a associação da receita a categorias específicas e adicionar tags relevantes para facilitar a busca e a organização.

4. Oferecer uma pré-visualização para que os administradores possam revisar a aparência final da receita antes de publicá-la.

5. Implementar autenticação segura para que apenas o administrador crie receitas

**US05 -** Eu, como administrador, desejo inserir categorias nas receitas para organizar o conteúdo de forma estruturada.

1. As categorias dos pratos devem ser: Entrada, prato principal, sobremesa, lanche, café da manhã, Bolos e tortas, Eventos Festivos.

2. Cada prato pode ter nenhuma ou muitas categorias diferentes.

**US06 -** Eu, como administrador, desejo inserir tags nas receitas para facilitar o agrupamento dos ingredientes que o prato possui.

1. As tags possíveis dos pratos são: Leite, Oleaginosas, Carne de Porco, Farinha de Trigo, Carne de Frango, Carne Bovina, Peixe, Queijos, Cogumelos

2. Cada receita pode ter nenhum ou muitas tags diferentes.

3. *(Talvez) Automatizar as tags com todos os ingredientes que forem descritos na receita.*

**US07 -** Eu, como usuário, desejo buscar receitas por nome para encontrar rapidamente receitas específicas e facilitar o acesso a pratos de meu interesse.

1. As receitas devem ser filtradas pelas palavaras que contém no título da receita.

2. As receitas não devem ser pesquisadas com exatamente a mesma disposição das palavras da busca.

**US08 -**  Eu, como usuário, desejo filtrar receitas por categorias para encontrar os pratos de meu interesse mais eficientemente.

1. A pesquisa é feita apenas com as categorias pré-existentes. É uma busca direcionada.

2. Não deve ser possível pesquisar receitas com uma categoria não existente.

**US09 -** Eu, como usuário, desejo filtrar receitas por tags para encontrar os pratos com ingredientes de meu interesse mais eficientemente.

1. A pesquisa é feita apenas com as tags pré-existentes. É uma busca direcionada.

2. Não deve ser possível pesquisar receitas com uma tag não existente.

**US24 -** Eu, como usuário, desejo compartilhar uma receita com outras pessoas para trocar experiências culinárias com amigos e familiares de forma rápida e conveniente.

1. Deve poder copiar o link através de um botão intuitivo de compartilhamento.

2. Quem acessar o link deve dar direto na mesma página, sem necessidade de login.


**US25 -** Eu, como um usuário, quero exportar receitas em formato PDF para que eu consiga visualizar a receita offline e em outros dispositivos.

1. Deve abrir um pdf através de um botão intuitivo de visualização de pdf.

2. Deve ter a opção de baixar o pdf na mesma página.