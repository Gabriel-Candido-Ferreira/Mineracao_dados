
---

# Clustering com Gaussian Mixture Model (GMM)

## Descrição

Neste trabalho, realizamos uma **análise de agrupamento (clustering)** utilizando o modelo de mistura gaussiana (GMM) da biblioteca `scikit-learn`.

## Como Executar

Certifique-se de possuir o `Python 3.x` e o `scikit-learn` instalados:

```bash
pip install scikit-learn matplotlib numpy
```

## Implementação

* Utilizamos o `make_blobs` para gerar um conjunto de 300 amostras distribuídas em 4 clusters.
* Aplicamos o GMM para agrupar esses pontos.
* Por fim, plotamos o resultado mostrando cada ponto colorido pelo seu respectivo agrupamento.

## Resultados

✅ **Quantidade de clusters identificados:**

* **4 clusters** (conforme especificado pelo modelo).

✅ **Sobreposição:**
Alguns clusters estão relativamente próximos, sendo que nas bordas é possível que os grupos se sobreponham.
Isso é fruto tanto da proximidade quanto do modelo probabilístico que o GMM utiliza para categorizar cada ponto.

✅ **Agrupamento visual:**
O agrupamento é **coerente** e revela grupos relativamente bem concentrados. Apenas nas bordas é que temos uma sobreposição maior.

✅ **Vantagem principal:**

* O GMM é capaz de se adaptar a clusters elípticos, sendo **mais flexível que o K-Means**, que é limitado a clusters esféricos.
* Ele também provê probabilidades de pertinência para cada ponto, aumentando a riqueza na avaliação do modelo.

✅ **Limitação principal:**

* Ele **pressupõe que os clusters seguem uma distribuição gaussiana**, o que nem sempre é verdade na prática.
* É preciso especificar o número de clusters a priori, ou usar métodos como o BIC ou AIC para essa definição.
