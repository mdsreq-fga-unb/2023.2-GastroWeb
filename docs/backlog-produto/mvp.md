## MVP

| Id | Descrição |
| --- | --- |
| US03 | Eu, como administrador, desejo deletar as receitas gastronômicas para ter mais controle sobre o conteúdo do site. |
| US04 | Eu, como usuário, desejo visualizar as receitas gastronômicas para consultá-las sempre que quiser. |
| US02 | Eu, como administrador, desejo editar as receitas gastronômicas para ter mais flexibilidade sobre as receitas. |
| US01 | Eu, como administrador, desejo criar receitas gastronômicas para poder enriquecer o conteúdo do site aumentando a variedade de receitas culinárias. |
| US33 | Eu, como administrador, desejo fazer login com minha conta para acessar as funcionalidades de gerenciamento de receitas. |
| US25 | Eu, como um usuário, quero exportar receitas em formato PDF para que eu consiga visualizar a receita offline e em outros dispositivos. | 
| US24 | Eu, como usuário, desejo compartilhar uma receita com outras pessoas para trocar experiências culinárias com amigos e familiares de forma rápida e conveniente. |
| US07 | Eu, como usuário, desejo buscar receitas por nome para encontrar rapidamente receitas específicas e facilitar o acesso a pratos de meu interesse. |
| US05 | Eu, como administrador, desejo inserir categorias nas receitas para organizar o conteúdo de forma estruturada. |
| US06 | Eu, como administrador, desejo inserir tags nas receitas para facilitar o agrupamento dos ingredientes que o prato possui. |
| US08 | Eu, como usuário, desejo filtrar receitas por categorias para encontrar os pratos de meu interesse mais eficientemente. |
| US09 | Eu, como usuário, desejo filtrar receitas por tags para encontrar os pratos com ingredientes de meu interesse mais eficientemente. |


## Critérios de Aceitação

**US03 -** Eu, como administrador, desejo deletar as receitas gastronômicas para ter mais controle sobre o conteúdo do site.

1. O sistema deve verificar por meio do login se o usuário é administrador, a fim de garantir que apenas administradores possam acessar essa funcionalidade.

2. Ao clicar para deletar uma receita, o sistema deve solicitar uma confirmação antes de realizar a exclusão.

**US04** - Eu, como usuário, desejo visualizar as receitas gastronômicas para consultá-las sempre que quiser.

1. Deve haver uma seção claramente identificada na interface do usuário para visualizar as receitas gastronômicas.

2. Ao clicar em uma receita na lista, o sistema deve exibir detalhes da receita, incluindo ingredientes, instruções de preparo e tags.

**US02** - Eu, como administrador, desejo editar as receitas gastronômicas para ter mais flexibilidade sobre as receitas.

1. Todos os campos de uma receita podem ser editados.

2. Oferecer a opção de visualizar as alterações antes de salvá-las permanentemente

**US01** - Eu, como administrador, desejo criar receitas gastronômicas para poder enriquecer o conteúdo do site aumentando a variedade de receitas culinárias.

1. Os campos de título, ingredientes e instruções são obrigatórios.

2. O sistema deve impedir a criação de uma receita que não tenha todos os campos obrigatórios preenchidos

3. O usuário deve ser informado de quais campos de informação são obrigatórios e quais são opcionais

4. Permitir o upload de imagens e vídeos presentes no dispositivo (computador ou smartphone) para ilustrar a receita.

5. Permitir a associação da receita a categorias específicas e adicionar tags relevantes para facilitar a busca e a organização.

6. Oferecer uma pré-visualização para que os administradores possam revisar a aparência final da receita antes de publicá-la.

**US33 -** Eu, como administrador, desejo fazer login com minha conta para acessar as funcionalidades de gerenciamento de receitas (criar, editar e deletar receitas).

1. As funcionalidades de criar, editar e deletar receitas devem estar restritas à interface do administrador.

2. O sistema deve validar as credenciais inseridas e permitir o acesso apenas a administradores.
   
3. As credenciais devem ser criadas previamente, pela equipe de desenvolvimento, e passadas para o administrador.

**US05 -** Eu, como administrador, desejo inserir categorias nas receitas para organizar o conteúdo de forma estruturada.

1. As categorias dos pratos devem ser: Entrada, prato principal, sobremesa, lanche, café da manhã, Bolos e tortas, Eventos Festivos.

2. Cada prato pode ter nenhuma, uma ou muitas categorias diferentes.

**US06 -** Eu, como administrador, desejo inserir tags nas receitas para facilitar o agrupamento dos ingredientes que o prato possui.

1. As tags possíveis dos pratos são: Leite, Oleaginosas, Carne de Porco, Farinha de Trigo, Carne de Frango, Carne Bovina, Peixe, Queijos, Cogumelos

2. Cada receita pode ter nenhum, uma ou muitas tags diferentes.

3. Automatizar as tags com todos os ingredientes que forem descritos na receita.

**US07 -**  Eu, como usuário, desejo buscar receitas por nome para encontrar rapidamente receitas específicas e facilitar o acesso a pratos de meu interesse.

1. As receitas devem ser buscadas pelas palavras que contém no título da receita.

2. A receita não necessariamente deve conter todas as palavras da busca em seu título

3. A pesquisa por uma receita não precisa ser feita na ordem exata das palavras do título da receita

4. Caso o campo de busca esteja vazio, então o sistema deve avisar ao usuário que o campo de busca está vazio

5. Caso a busca não encontre nenhuma receita, o usuário deve receber a seguinte mensagem: 'A receita que está procurando não foi encontrada.”


**US08 -**  Eu, como usuário, desejo filtrar receitas por categorias para encontrar os pratos de meu interesse mais eficientemente.

1. A pesquisa é feita apenas com as categorias pré-existentes. É uma busca direcionada.

2. O usuário pode filtrar por uma ou mais categorias simultaneamente

3. Não deve ser possível pesquisar receitas com uma categoria não existente.

4. Todas as receitas que conterem alguma das categorias escolhidas serão mostradas ao usuário


**US09 -** Eu, como usuário, desejo filtrar receitas por tags para encontrar os pratos com ingredientes de meu interesse mais eficientemente.

1. A pesquisa é feita apenas com as tags pré-existentes. É uma busca direcionada.

2. O usuário pode filtrar por uma ou mais tags simultaneamente

3. Não deve ser possível pesquisar receitas com uma tag não existente.

4. Todas as receitas que conterem alguma das tags escolhidas serão mostradas ao usuário


**US24 -** Eu, como usuário, desejo compartilhar uma receita com outras pessoas para trocar experiências culinárias com amigos e familiares de forma rápida e conveniente.

1. O usuário deve poder copiar o link da receita com apenas 1 clique em um botão.


**US25 -** Eu, como usuário, quero exportar receitas em formato PDF para que eu consiga visualizar a receita offline e em outros dispositivos.

1. Deve-se abrir um pdf através de um botão intuitivo de visualização de pdf.
2. Deve ter a opção de baixar o pdf na mesma página.
