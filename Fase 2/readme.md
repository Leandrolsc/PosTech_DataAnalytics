# TECH CHALLENGE - FASE 2 - Time Series

## Introdução

No contexto do Tech Challenge da Fase 2, foi solicitado o desenvolvimento de uma solução de análise de séries temporais. 

Os objetivos principais desta fase são:

1. Demonstrar o fluxo completo do modelo, desde a captura dos dados até a entrega do resultado final, com um storytelling claro e objetivo.
2. Justificar a técnica utilizada para resolver o problema.
3. Alcançar uma acurácia mínima de 70%.

## Dados Utilizados

A base de dados utilizada foi obtida na plataforma Investing, conforme indicado no problema do desafio. Para acessar os dados, foi necessário realizar cadastro na plataforma e selecionar o período desejado no link:
https://br.investing.com/indices/bovespa-historical-data.

O período selecionado foi 01/01/2000 a 17/01/2025, gerando um dataset com as seguintes características:

* Número de registros: 6.195 linhas
* Número de colunas: 7

## Descrição das Colunas
1. Data: Data do índice Ibovespa.
2. Último: Valor de fechamento do índice Ibovespa no dia.
3. Abertura: Valor de abertura do índice Ibovespa no dia.
4. Máxima: Valor máximo alcançado pelo índice no dia.
5. Mínima: Valor mínimo alcançado pelo índice no dia.
6. Vol.: Volume movimentado no dia (em valores financeiros).
7. ar%: Variação percentual entre o valor de fechamento do dia anterior e o do dia atual.

## Pré-processamento e Transformações

### 1. Concatenação de Dados:
Devido à limitação na quantidade de dados que podem ser extraídos de uma única vez na plataforma, foi necessário realizar duas extrações separadas. Os dados foram, então, concatenados em um único DataFrame.

### 2. Análise de Qualidade dos Dados:
A verificação inicial foi realizada com o comando df.info(), que indicou que todas as colunas estavam devidamente preenchidas, sem valores nulos ou ausentes.

### 3. Conversão de Índice Temporal:
A coluna Data foi convertida para o tipo datetime e definida como índice do DataFrame, facilitando análises baseadas em séries temporais e operações ao longo da linha temporal.

### 4. Análise de Outliers e Estacionariedade:
Foi feita uma inspeção visual da série temporal para identificar a presença de outliers ou padrões inconsistentes. A análise indicou que:

* Não há outliers evidentes que comprometam a integridade da série.

* A série não é estacionária, o que foi confirmado utilizando o teste de Dickey-Fuller e realizando a observação de tendência ao longo do tempo.

![Grafico Ibovespa](/imagens/Grafico_Bovespa.png)

## Modelagem

Para o problema, foram testados três modelos de previsão sendo eles o modelo de 
1. ARIMA: onde foi realizado a primeira diferença para tornar a linha temporal estacionaria; 
2. Regressão Linear;
3. Prophet. 

Foram testados esses modelos com o foco de identificar aquele que melhor capturasse a dinâmica da série temporal e atingisse os objetivos do desafio. O modelo que apresentou os melhores resultados foi o Prophet, desenvolvido pela Meta (anteriormente Facebook).

## Métrica de Avaliação

A primeira métrica utilizada para avaliar o desempenho do modelo foi o Erro Médio Absoluto Percentual (MAPE), o MAPE retorna um valor entre 0 e 1, e deve ser multiplicado por 100 para ter o percentualde acordo com a biblioteca de acordo com a biblioteca utilizad ao scikit-learn.

Além do MAPE também está sendo avalidado o Erro Médio Absoluto (MAE) onde ela mede a média da diferença absoluta entre os valores previstos pelo modelo e os valores observados porem não diferencia entre positivos e negativos. 


## Resultados

Realizando a analise do MAPE e do MAE por modelo temos:

1. Regressão Linear:

Utilizando a regressão linear tivemos o MAPE de 1.23% sendo o melhor modelo entre os três com o menor percentual de erro. E com o MAE de 667,37 sendo um erro baixo considerando as diferenças entre os dias.

![Grafico_Regression](/imagens/Grafico_Regression.png)


2. Prophet:

Utilizando o Prophet da Meta tivemos o MAPE de 8.07%, um metodo simples de ser executado assim como a Regressão Linear no entanto o percentual de erro foi maior que o da Regressão Linear. E o MAE de 8346,46 sendo uma grande variação no erro.

![Grafico_Prophet](/imagens/Grafico_Prophet.png)


3. ARIMA:

Para o ARIMA foi realizado a "Primeira Diferença" para tornar a serie estacionaria e também utilizado a biblioteca pmdarima e o modulo auto_arima para pegar os melhores parametros para executar o ARIMA, no entanto o modelo não foi coerente retornando uma linha com valor unico, e retornando um MAPE maior que 100% ou seja, um erro muito alto e inviavel para um modelo de predição. E o MAE de 1148,86 porém como o MAPE ja mostra o modelo é inviavel mesmo que o MAE não seja tão alto.

![Grafico_ARIMA](/imagens/Grafico_ARIMA.png)


## Conclusão

O Melhor modelo apresentado foi o de Regressão linear com o menor indice de erro possível, uma proxima etapa a essa seria utilizar diariamente os dados do ibovespa para ir treinando e ajustando o modelo.

### Referências:

https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html

https://medium.com/techbloghotmart/o-que-s%C3%A3o-s%C3%A9ries-temporais-e-como-aplicar-em-machine-learning-6ea5d94bec78

https://mariofilho.com/como-criar-um-modelo-simples-para-prever-series-temporais-usando-machine-learning-em-python/

https://mariofilho.com/mape-erro-absoluto-percentual-medio-em-machine-learning/

https://mariofilho.com/mae-erro-medio-absoluto-em-machine-learning/