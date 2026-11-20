# Tarefa atual — Primeiro contrato do AI Ticket Classifier

**Status:** proposta para revisão. A implementação depende de autorização.

## Contexto e aceite

Exercitar o caminho completo de `POST /classify` com um simulador local de resposta fixa. Isso permite entender os modelos de entrada e saída e testar a API sem credenciais, rede ou cobrança de inferência. Usar mensagens sintéticas nesta etapa.

- Uma requisição com `message` textual e com conteúdo retorna `200` e um JSON com `category`, `priority` e `reason`, todos textuais. Entradas válidas recebem a mesma resposta simulada.
- `message` ausente, de outro tipo, vazia ou composta apenas de espaços recebe `422`. Usar o erro padrão de validação do FastAPI.
- A rota aparece na documentação OpenAPI gerada com os modelos de entrada e saída.
- Os testes com pytest e `TestClient` verificam o corpo completo de sucesso e os casos de entrada inválida. Conferir a rota em `/docs` localmente e apresentar as verificações e o diff para revisão.

## Regras, contratos e impacto

- Referência educacional em [docs/contexto-aprendizado-ai-engineer.md](docs/contexto-aprendizado-ai-engineer.md).
- O formato dos campos vem do exemplo do projeto. Para a simulação, a proposta é usar `infrastructure` e `high` como valores de exemplo, com `reason` igual a `Resposta simulada para validar o contrato.`. A taxonomia e os critérios de negócio dependem de confirmação para a classificação real.
- O projeto fica em `ai-ticket-classifier/`, com `app.py` e `requirements.txt`. O ponto de partida é o exercício `GET /`. A proposta é acrescentar a rota `POST /classify` com os modelos Pydantic e criar `tests/test_classify.py` com pytest e HTTPX.
- Confirmar o formato e a resposta fixa antes de executar. A partir de `ai-ticket-classifier/`, iniciar a aplicação com `..\.venv\Scripts\python.exe -m uvicorn app:app`. Após preparar as dependências de teste, usar `..\.venv\Scripts\python.exe -m pytest`.

## Microentregas

- [ ] Implementar o contrato HTTP da simulação em uma única microentrega. Criar os modelos e a rota, testar os resultados esperados e mostrar como a entrada atravessa o FastAPI até o JSON de saída. Confirmar o aceite após a revisão do diff.

## Deixado para depois

- [ ] Definir o comportamento da classificação real.
  - Descrição — Identificar público e contexto de uso, categorias, níveis de prioridade, critérios, linguagem dos chamados e tratamento de casos ambíguos ou com informação insuficiente.
  - Status — O exemplo disponível ilustra o formato. Falta validar os critérios com exemplos contrastantes e registrar as regras aprovadas.
- [ ] Escolher a estratégia de inferência real.
  - Descrição — Comparar API hospedada e modelo local por qualidade, facilidade de uso, privacidade, custo, latência e hardware. Definir dados permitidos e tratamento de falhas.
  - Status — Para a primeira microentrega, a proposta usa apenas um simulador. A escolha do provedor e eventual autorização para gastos ficam para a integração.
