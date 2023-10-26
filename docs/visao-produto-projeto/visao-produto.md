## Histórico de revisão

|    Data    | Versão |              Descrição              |  Autor(es)  |
| :--------: | :----: | :---------------------------------: | :---------: |
| 26/09/2023 |  0.1   | Criação e estruturação do documento | Luan Mateus |
| 25/10/2023 |  0.2   | Correção do documento               | Matheus Henrick |

<div style="text-align: center; margin: 3px">
<img src="https://raw.githubusercontent.com/mdsreq-fga-unb/2023.2-GastroWeb/GitPages/docs/images/escamadepeixe.png" alt="Diagrama de Ishikawa" style="width: 50rem">
</div>


## Declaração Geral do Produto

<p style="text-indent: 50px;text-align: justify;">Nossa cliente, uma graduada na área de Gastronomia, enfrenta uma série de desafios ao utilizar a plataforma atual para compartilhar suas receitas e experiências culinárias. O principal obstáculo reside na formatação das receitas no Instagram, onde as restrições, incluindo limitações de caracteres, exercem um impacto significativo. Essas limitações não apenas restringem sua liberdade criativa ao compartilhar receitas, tornando a inclusão de informações cruciais, como porções, tempo de preparo e variações, uma tarefa árdua ou mesmo impossível, mas também demandam que ela divida suas instruções em múltiplos comentários em uma única postagem para esclarecer as receitas. Além disso, frequentemente ela se vê compelida a responder a perguntas semelhantes nos comentários ou a repetir informações em diferentes postagens.
</p>
<p style="text-indent: 50px;text-align: justify;">Outro desafio crucial está relacionado à restrição na inserção de imagens ou vídeos entre os passos da receita, bem como à limitação quanto à quantidade máxima de fotos que podem ser publicadas em um carrossel, e à obrigatoriedade de ter imagens ou ao tamanho restrito dos vídeos. Essas restrições impactam adversamente a experiência dos usuários, que frequentemente se veem forçados a rolar a tela repetidamente para alternar entre o texto e as imagens, ou a procurar informações nos comentários para compreender e concluir as receitas.
</p>
<p style="text-indent: 50px;text-align: justify;">Além disso, um desafio adicional diz respeito à forma como o Instagram organiza o texto durante a digitação, tornando a criação de conteúdo de alta qualidade uma tarefa mais complexa.
</p>
<p style="text-indent: 50px;text-align: justify;">A plataforma atual enfrenta desafios significativos em relação à sua capacidade de alcançar o público-alvo estabelecido por nossa cliente na área de Gastronomia. A exigência de uma conta no Instagram como condição prévia para acessar o conteúdo representa uma barreira significativa, limitando assim a divulgação de suas receitas para além desta plataforma. Isso não apenas impede a eficácia de utilizar o Instagram como a principal rede para compartilhamento de receitas, mas também torna nossa cliente dependente direta do algoritmo da plataforma, tornando imperativa a exploração de alternativas mais eficazes.
</p>
<p style="text-indent: 50px;text-align: justify;">Ademais, a ausência de um sistema fácil de favoritar receitas e a falta de recursos para gerar receitas imprimíveis representam desafios adicionais. Isso compromete a capacidade de nossa cliente de alcançar seu público-alvo desejado e torna mais difícil o acesso para aqueles que preferem salvar ou imprimir as receitas de forma conveniente.
</p>
<p style="text-indent: 50px;text-align: justify;">Outro problema crítico é a ausência de uma funcionalidade eficaz de busca por receitas na plataforma. A pesquisa por meio de tags frequentemente não produz resultados precisos, devido à natureza diversificada do Instagram, que abrange diversos tipos de conteúdo, não se limitando apenas a receitas culinárias. Isso resulta na frustração dos usuários que buscam receitas específicas, uma vez que as informações muitas vezes são apresentadas com limitações de formatação e organização.
</p>

| Para            | Uma graduada na área de Gastronomia                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Quem            | Busca uma solução que faça aumentar o número de visualizações das suas publicações.                                    |
| O GastroWeb     | É uma plataforma de compartilhamento culinário online.                                                                 |
| Que             | Gerencia o compartilhamento e o acesso às receitas.                                                                    |
| Ao contrário de | Outras plataformas, como o Instagram, que, embora amplamente utilizadas, apresentam restrições que dificultam a criação de conteúdo, tais como limite de caracteres, quantidade de imagens, etc.                                                                   |
| Nosso produto   | Entrega solução para o compartilhamento de receitas, que permite aos criadores de conteúdo publicar suas receitas sem restrições de tamanho ou quantidade de texto e imagens. Além disso, os usuários poderão buscar e salvar as receitas de seu interesse através da plataforma. |

## Objetivos do Produto

<p style="text-indent: 50px;text-align: justify;">Nosso objetivo principal é estabelecer uma estrutura de criação de receitas que simplifique a intercalação de textos, imagens e vídeos, garantindo uma padronização consistente. Nosso objetivo é otimizar o processo de publicação para nossa cliente e melhorar a compreensão dos leitores, garantindo que cada receita atenda a esses requisitos estabelecidos. Além de democratizar o acesso de qualquer pessoa, permitindo compartilhar e exportar facilmente as receitas do site. Para alcançar esse objetivo, estamos comprometidos com as seguintes melhorias:
</p>


- **Otimizar a Criação de Conteúdo**: Para cada nova receita, vamos aumentar o limite atual de 10 fotos e videos com duração de 60 segundos, que serão adicionados ao corpo do texto e não mais em formato de carrossel. Além disso, queremos que nossa cliente possa incluir informações cruciais, como porções, tempo de preparo e variações, de modo que ela não precise dividir as instruções em múltiplos comentários.

- **Permitir o Compartilhamento de Receitas**: Nosso produto se propõe a permitir que nossa cliente compartilhe suas receitas da maneira que ela achar mais conveniente, seja por meio de legendas nas imagens ou no formato de receita tradicional, sem as restrições de formatação do Instagram.

- **Democratizar o Acesso ao Conteúdo**: Queremos que tanto nossa cliente, quanto os demais usuários que acessarão a plataforma tenham mais liberdade para acessar o conteúdo, sem precisar de uma conta no Instagram. Assim, poderemos alcançar tanto os usuários que usam o Instagram quanto os que não usam.

- **Administração do Armazenamento das Receitas**: Um dos objetivos é melhorar a organização e a manutenibilidade das receitas. Ou seja, as receitas precisam ser editáveis, e devem poder ser categorizadas para auxiliar na administração delas no site.

## Tecnologias Utilizadas

- **Backend**: Utilizaremos Python e o framework Django com Django Rest Framework para criar um backend seguro e eficiente.
- **Frontend**: Usaremos JavaScript com Vue.js para uma interface de usuário dinâmica e amigável.
- **Banco de Dados**: Armazenaremos dados com segurança e escalabilidade no PostgreSQL.
- **Hospedagem de Vídeos**: Vídeos serão hospedados no YouTube pela confiabilidade e alcance.
- **Hospedagem de Imagens**: Integraremos serviços como Imgur ou ImgBB para armazenar e exibir imagens.
- **Controle de Versão**: Git para controle de versão.
- **Análise de Dados**: Adotaremos o Matomo para oferecer uma visão valiosa do desempenho da plataforma à nossa cliente, permitindo uma análise aprofundada.
- **Integração com Redes Sociais**: Implementaremos APIs de redes sociais para facilitar a interação dos usuários.
- **DevOps**: Usaremos Docker para garantir ambientes de desenvolvimento consistentes, Shell Script para automação de tarefas e um Makefile para facilitar o gerenciamento de comandos e processos de desenvolvimento e implantação

**Nota Importante**: As tecnologias mencionadas são escolhas iniciais, sujeitas a revisões durante o desenvolvimento do projeto, para se adequarem às necessidades emergentes.
