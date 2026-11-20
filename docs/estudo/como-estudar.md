# Como estudar neste laboratório

Em cada sessão, comece localizando o assunto no fluxo do projeto. Em seguida, trabalhe uma pergunta que você consiga responder com uma previsão, um teste ou uma comparação de resultados.

## Método

| Técnica | Como usar aqui |
| --- | --- |
| Exemplo resolvido com redução gradual de ajuda | Na primeira passagem, acompanhe um exemplo curto e explique por que cada passo existe. No próximo caso, complete uma parte e peça pistas conforme precisar. A meta é conseguir resolver uma variação usando a mesma ideia. |
| Prever, rodar, investigar, modificar e criar | Antes de testar, anote o que espera que aconteça. Rode e investigue o resultado. Depois, modifique uma condição e use a ideia em um caso novo. É uma adaptação do PRIMM para quem já desenvolve software. |
| Recuperação ativa e revisão espaçada | Ao fechar a sessão, reconstrua de memória o fluxo ou a decisão e confira com o código. Retome o conceito em uma sessão posterior quando ele aparecer em outro problema. |
| Feedback curto | Compare o que esperava com o que aconteceu. A mentoria deve explicar a diferença, indicar onde conferir e propor uma nova tentativa pequena. |

### Um exercício para agora

1. Desenhe o caminho de um chamado entre o cliente e a resposta, usando a [arquitetura do classificador](ai-ticket-classifier.md) como referência.
2. Imagine o corpo `{"message": "   "}`. Diga em qual etapa ele deve parar e como você demonstraria isso num teste.
3. Imagine agora que o sistema respondeu com prioridade `high` no formato certo. Explique que evidência você precisaria para dizer que a prioridade está correta.

O marco desta sessão é conseguir explicar a diferença entre validar o contrato e avaliar a classificação, usando um exemplo novo. Você pode registrar uma explicação curta, um teste que escreveu ou as duas coisas.

## De onde vêm as técnicas

- Atkinson, Renkl e Merrill estudaram a transição de exemplos resolvidos para problemas independentes. Usaram perguntas de autoexplicação junto com a retirada gradual de passos. A aplicação aos nossos exercícios é uma adaptação. [Artigo original de Atkinson et al.](https://doi.org/10.1037/0022-0663.95.4.774)
- Sentance, Waite e Kallia avaliaram o PRIMM em aulas de programação com estudantes do ensino secundário. Usamos a sequência para investigar exemplos em Python, levando em conta que a sua experiência em backend é diferente da população do estudo. [Estudo original do PRIMM](https://eprints.gla.ac.uk/229013/)
- Roediger e Karpicke observaram melhor retenção tardia com testes de recuperação do que com releitura em seus experimentos. Cepeda e colegas observaram que o efeito do espaçamento depende do intervalo até a avaliação. Aqui, isso inspira revisões curtas em sessões diferentes. [Experimentos de recuperação ativa](https://pubmed.ncbi.nlm.nih.gov/16507066/) · [Experimento sobre espaçamento](https://journals.sagepub.com/doi/full/10.1111/j.1467-9280.2008.02209.x)
