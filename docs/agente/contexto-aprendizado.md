# Contexto da mentoria para agentes de IA

Ao retomar a mentoria, confira o [README](../../README.md), a [arquitetura e os marcos do projeto](../estudo/ai-ticket-classifier.md), o [roadmap de aprendizado](../estudo/roadmap-ai-engineering.md) e o [task.md](../../task.md). Confirme o que já existe no código antes de avançar.

## Perfil e objetivo profissional

Desenvolvedor de software com foco em backend. Quer fazer a transição para Applied AI Engineer e aproveitar uma oportunidade na empresa para construir sistemas e APIs que usam IA em problemas reais. O laboratório também servirá como portfólio para demonstrar a capacidade de integrar, avaliar e operar modelos, além de treinar um classificador simples e comparar abordagens.

## Conhecimentos declarados

| Área | Experiência informada |
| --- | --- |
| Backend | Go, TypeScript e JavaScript, Fastify, NestJS, APIs REST, organização e arquitetura de aplicações. |
| Dados | SQL, PostgreSQL, bancos relacionais e modelagem de dados. |
| Complementar | Conhecimentos de Java e Spring e experiência em frontend. |
| Infraestrutura | Conhecimento conceitual de Docker, CI/CD e DevOps, com pouca prática de implementação. |
| Python | Escolhido como linguagem principal. A familiaridade será aferida na prática, aproveitando a experiência prévia em programação. |

## Como conduzir a mentoria

- Comece pela visão de ponta a ponta. Situe cada exercício no começo, meio e fim do projeto antes de entrar no código. Explique a finalidade de cada parte, o efeito de uma mudança e como verificar o resultado.
- Use a experiência com backend para calibrar as explicações. Faça analogias com Go, TypeScript ou SQL quando couber. Introduza Python e matemática sob demanda, com perguntas ou exercícios curtos. Use o [método de estudo](../estudo/como-estudar.md) para dosar exemplos, pistas, previsão, feedback e revisão em sessões posteriores.
- Quando o exercício tiver valor didático, oriente o desenvolvedor a escrever ou modificar um trecho pequeno. Peça uma previsão ou explicação com um caso novo antes de registrar compreensão.
- O desenvolvedor decide escopo, regras e trade-offs. Use o `task.md` para planejar uma microentrega de cada vez, aguarde autorização para implementar e apresente o diff e as verificações para revisão. Siga o [guia de desenvolvimento com agentes](https://github.com/j-ordep/agentic-development-guide/blob/main/PARA-AGENTES.md).

## Progresso de aprendizado

| Estado | Evidência na descoberta inicial |
| --- | --- |
| Apresentado | IA, ML e deep learning, treinamento e inferência, geração de tokens em LLMs, validade do esquema e qualidade da classificação. No primeiro exercício, ambiente virtual, FastAPI, Uvicorn e registro de rota com um decorador. |
| Compreendido | A compreensão dos conceitos de IA ainda precisa ser verificada com uma explicação ou previsão do desenvolvedor. |
| Aplicado | O desenvolvedor montou o ambiente virtual e relatou ter rodado a primeira aplicação FastAPI com `GET /`. |
| A reforçar | Explicar onde ocorre validação e onde ocorrerá inferência. Distinguir um teste que comprova o contrato de uma avaliação que mede o acerto das classificações. |

O início da leitura do artigo da Simplilearn foi informado pelo desenvolvedor. O entendimento de seus tópicos ainda precisa ser verificado na prática. As decisões de produto e de integração em aberto estão no [task.md](../../task.md).

O próximo exercício está no [guia de estudo](../estudo/como-estudar.md#um-exercício-para-agora). Atualize este registro quando houver compreensão demonstrada, experimento executado, decisão durável ou mudança de objetivo.
