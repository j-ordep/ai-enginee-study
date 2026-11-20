# Contexto de aprendizado em AI Engineering

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

## Como aprender

- Partir de um problema concreto, estudar o fundamento que ele exige, experimentar, verificar o resultado e aprofundar as lacunas reveladas pela prática.
- Explicar o mecanismo e os trade-offs com exemplos do projeto e, quando ajudarem, comparações com Go, TypeScript ou SQL. Introduzir tipagem, módulos, ambientes, dependências, exceções e testes conforme forem usados. Estudar `async` quando houver I/O que justifique a escolha.
- Manter autonomia sobre decisões e código. Usar microentregas aprovadas, testes que comprovem o aceite e revisão do diff antes de avançar. Preferir exercícios curtos, como prever o resultado de um teste ou interpretar um erro de classificação. [Guia de desenvolvimento com agentes](https://github.com/j-ordep/agentic-development-guide/blob/main/PARA-AGENTES.md)

## Lacunas e prioridades

- **Matemática e estatística** — Começar com proporções, média, variância e leitura de distribuições ao medir resultados. Usar probabilidade condicional, Bayes, amostragem, viés e intervalos de confiança quando houver perguntas sobre incerteza. Introduzir vetores, matrizes, normas e produto escalar com representações de texto e similaridade. Ligar derivadas, perda, gradientes e taxa de aprendizado ao treinamento.
- **ML, deep learning e linguagem** — Consolidar treinamento, inferência, classificação supervisionada, generalização e overfitting. Avançar para representação de texto, redes neurais, backpropagation, Transformers e pré-treinamento conforme surgirem os experimentos.
- **Engenharia e operação** — Praticar contratos, integração de modelos, avaliação reprodutível, privacidade, custo, latência e tratamento de falhas. Investigar deploy, observabilidade, Docker, CI/CD, MLOps e LLMOps quando houver um serviço para operar.

## Projeto prático e percurso

O **AI Ticket Classifier** usa a triagem de chamados técnicos para estudar como uma API em Python recebe texto e devolve categoria, prioridade e justificativa breve. A classificação inicial usará um LLM pré-treinado depois que o contrato puder ser exercitado com uma simulação. As regras de triagem serão registradas na referência técnica do projeto após validação.

O código e as dependências declaradas ficam em [ai-ticket-classifier/](../ai-ticket-classifier/). O ambiente Python local (`.venv`) fica na raiz do workspace.

| Horizonte | Prática e aprendizado |
| --- | --- |
| Essencial agora | Descoberta e contrato mínimo. Validar entrada e saída com FastAPI e Pydantic e testar a rota com pytest. Distinguir IA, ML, deep learning, inferência, validade do esquema e acerto da classificação. |
| Em seguida | Integrar um LLM pré-treinado. Explorar tokens, contexto, amostragem, saídas estruturadas, falhas, latência e custo. Definir critérios de triagem e rotular cerca de 30 a 50 chamados para uma avaliação exploratória. |
| Depois | Medir categoria e prioridade separadamente com métricas por classe e matrizes de confusão. Comparar mudanças de instrução ou modelo com dados comparáveis, cuidando para evitar ajustes repetidos sobre a avaliação final. Treinar um modelo clássico com scikit-learn, estudar TF-IDF, regressão logística, separação dos dados e validação, e verificar se é preciso ampliar o conjunto de treinamento. Comparar qualidade, latência, custo e manutenção e praticar a operação do serviço. |
| Aprofundamentos opcionais | Usar embeddings e busca semântica, RAG, tool calling, agentes ou fine-tuning quando uma necessidade ou hipótese justificar um experimento. Aprofundar redes neurais e Transformers em paralelo quando isso ajudar a explicar os resultados. |

## Progresso de aprendizado

| Estado | Evidência na descoberta inicial |
| --- | --- |
| Apresentado | IA, ML e deep learning, treinamento e inferência, geração de tokens em LLMs, validade do esquema e qualidade da classificação. No primeiro exercício, ambiente virtual, FastAPI, Uvicorn e registro de rota com um decorador. |
| Compreendido | A compreensão dos conceitos de IA ainda precisa ser verificada com uma explicação ou previsão do desenvolvedor. |
| Aplicado | O desenvolvedor montou o ambiente virtual e relatou ter rodado a primeira aplicação FastAPI com `GET /`. |
| A reforçar | Explicar onde ocorre validação e onde ocorrerá inferência. Distinguir um teste que comprova o contrato de uma avaliação que mede o acerto das classificações. |

**Em aberto:** público e contexto da triagem, categorias, critérios de prioridade, casos ambíguos e dados permitidos para avaliação. A escolha do provedor depende de qualidade, custo, privacidade, latência e viabilidade local. O início da leitura do artigo foi informado pelo desenvolvedor. O entendimento de seus tópicos será verificado na prática.

## Próximos assuntos recomendados

1. Percorrer uma requisição da rota até a resposta e prever o que acontece com `message` ausente ou em branco.
2. Escrever ou revisar um modelo Pydantic e um teste de erro, relacionando type hints com validação em execução.
3. Definir critérios com exemplos de chamados e identificar informações que mudam a prioridade, como ambiente afetado e alcance da indisponibilidade.

Atualizar este registro quando houver compreensão demonstrada, experimento executado, decisão durável ou mudança de objetivo.

## Referências

- Direção de estudo e leitura inicial sobre fundamentos. [AI Engineer Roadmap](https://roadmap.sh/ai-engineer) · [How to Become an AI Engineer](https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/how-to-become-an-ai-engineer)
- Técnicas da primeira microentrega. [Python e `venv`](https://docs.python.org/3.13/library/venv.html) · [Entrada no FastAPI](https://fastapi.tiangolo.com/tutorial/body/) · [Saída no FastAPI](https://fastapi.tiangolo.com/tutorial/response-model/) · [Campos no Pydantic](https://docs.pydantic.dev/latest/concepts/fields/) · [Testes no FastAPI](https://fastapi.tiangolo.com/tutorial/testing/) · [pytest](https://docs.pytest.org/en/stable/)
- Conceitos para a integração posterior. [Introdução a ML](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml) · [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · [Exemplo de documentação de saídas estruturadas](https://developers.openai.com/api/docs/guides/structured-outputs)
