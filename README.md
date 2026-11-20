# AI Engineering na prática

Este é um laboratório de Applied AI Engineering para quem já desenvolve APIs. O primeiro projeto é o **AI Ticket Classifier**, uma API em Python que vai ler a descrição de um chamado técnico e sugerir categoria, prioridade e uma justificativa curta para a triagem.

## Onde estamos

O FastAPI responde a `GET /` e a `POST /classify`. A rota de classificação valida a entrada e devolve uma resposta fixa de simulação. O próximo marco é definir os critérios de triagem antes de integrar um LLM pré-treinado. Depois, vamos medir o resultado com chamados rotulados e comparar com um classificador treinado com exemplos.

O caminho de estudo acompanha o projeto. Começa com Python, contratos e testes, passa por LLMs, dados e avaliação e chega a ML clássico e à preparação de um serviço para operação.

## Para estudar

| Documento | O que você vai encontrar |
| --- | --- |
| [Arquitetura e roadmap do AI Ticket Classifier](docs/estudo/ai-ticket-classifier.md) | O fluxo de uma requisição, o papel do modelo, o que entra no escopo e os marcos até a comparação de modelos. |
| [Roadmap de AI Engineering](docs/estudo/roadmap-ai-engineering.md) | O que estudar e como demonstrar cada habilidade, a partir da experiência em backend. |
| [Como estudar](docs/estudo/como-estudar.md) | O ritmo de mentoria, os exercícios e as fontes usadas para montar o método. |

## Rodar a API localmente

Em um PowerShell na raiz do repositório, rode os comandos abaixo. Se já tiver a `.venv` do projeto com as dependências instaladas, execute só o `cd` e a última linha.

```powershell
cd ai-ticket-classifier
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app:app --reload
```

Abra [a documentação interativa](http://127.0.0.1:8000/docs) para experimentar `POST /classify`.

## Para agentes de IA

Use o [contexto da mentoria](docs/agente/contexto-aprendizado.md) para retomar uma sessão e consulte o [plano da microentrega atual](task.md) antes de trabalhar no projeto.
