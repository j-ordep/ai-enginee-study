# Roadmap de AI Engineering

A meta é conseguir integrar, avaliar e operar sistemas que usam modelos, além de entender como um modelo aprende e por que erra. A experiência com APIs, SQL e backend já fornece uma base para contratos, integração e testes. Estude Python conforme essas habilidades ganharem forma no projeto.

O [AI Ticket Classifier](ai-ticket-classifier.md) é o primeiro laboratório. Use os marcos abaixo para avaliar o que consegue explicar e aplicar. Avance por evidência, no ritmo em que o projeto levantar as dúvidas.

| Etapa | O que estudar | O que conseguir fazer |
| --- | --- | --- |
| Começo — Python e APIs | Ambiente virtual, módulos, type hints, validação com Pydantic, FastAPI e testes. | Subir uma API local, acompanhar uma requisição e comprovar o contrato com um teste. |
| Começo — Modelos e inferência | IA, ML e deep learning, treinamento, inferência, tokens, contexto, prompt, amostragem, saída estruturada e falhas de integração. | Percorrer o caminho do chamado até a resposta e explicar o que o modelo faz quando recebe um texto novo. |
| Meio — Dados e avaliação | Rotulagem, conjunto de referência, distribuição de classes, matriz de confusão, precisão, recall, F1, amostragem e incerteza. | Calcular uma métrica à mão com poucos casos, comparar resultados por classe e explicar quais erros importam na triagem. |
| Meio — Treinamento clássico | Aprendizado supervisionado, representação de texto, TF-IDF, regressão logística, treino, validação, teste e generalização. | Treinar um classificador simples, repetir o experimento e avaliar em exemplos que ficaram fora do treinamento e dos ajustes. |
| Fim do ciclo — Engenharia e operação | Escolha de abordagem, publicação, monitoramento, latência, custo, privacidade, degradação da qualidade e reavaliação. | Defender uma escolha com evidência e explicar como investigar falhas depois de publicar. |

## Matemática conforme a pergunta

- **Estatística e probabilidade.** Ao medir, comece com proporções, média, variância e distribuições. Avance para probabilidade condicional, Bayes, amostragem, viés e intervalos de confiança. Investigue como 95% de acurácia pode esconder todos os chamados urgentes.
- **Álgebra linear.** Ao transformar texto em números, estude vetores, matrizes, normas e produto escalar. Similaridade de cosseno ganha sentido quando for preciso comparar representações de dois textos.
- **Cálculo e otimização.** Ao treinar, estude função de perda, derivada, gradiente e taxa de aprendizado. Use um exemplo pequeno para explicar por que um ajuste nos parâmetros muda a previsão.

## Aprofundamentos depois do primeiro ciclo

Redes neurais, backpropagation e Transformers ajudam a aprofundar o funcionamento interno dos modelos. Explore embeddings e busca semântica quando similaridade fizer parte do problema. Estude RAG quando houver necessidade de consultar fontes, tool calling quando a aplicação precisar executar uma ação e fine-tuning quando houver evidência de que adaptar o modelo vale o custo.

## Referências

- Direção geral e visão do papel profissional. [AI Engineer Roadmap](https://roadmap.sh/ai-engineer) · [Artigo inicial da Simplilearn](https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/how-to-become-an-ai-engineer)
- Para o começo do projeto. [Ambientes virtuais no Python](https://docs.python.org/3.13/library/venv.html) · [FastAPI e testes](https://fastapi.tiangolo.com/tutorial/testing/) · [Pydantic](https://docs.pydantic.dev/latest/concepts/fields/)
- Para ligar teoria à prática. [Introdução a ML](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml) · [Artigo original do Transformer](https://arxiv.org/abs/1706.03762) · [Avaliação de modelos no scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html)

Use o [guia de estudo](como-estudar.md) para transformar o próximo tema em um exercício.
