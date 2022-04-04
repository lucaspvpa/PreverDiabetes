# PreverDiabetes
 Ideia do projeto é fazer uma análise de dados do dataset 'diabetes.csv' , criar um modelo de machine learning e fazer o deploy do projeto para que as pessoas possam utilizar.

O dataset utilizado nessa análise foi dispiniblizado no kaggle (https://www.kaggle.com/datasets/mathchi/diabetes-data-set) 

O projeto foi dividido em 5 etapas:

1° - Foi fazer a Importação das bibliotecas utilizadas no projeto 
2° - Imortação da base de dados
3° - Foi feito uma análise dos dados
4° - Treinamento dos modelos (utilizando a biblioteca sklearn)
5° - Fazer o Deploy do projeto (utilizando a biblioteca joblib)

Primeiramente foi feito uma análise inicial de qual era o melhor modelo de classificação, para isso foi testados os modelos: RandomForest, Support Vector Machines, Stochastic Gradient Descent, Decision Trees, Naive Bayes e AdaBoostClassifier.
Na análise inicial o melhor modelo foi o RandomForest. Com isso o proximo passo foi melhorar os Hiperparâmetros do RandomForest para descobrir os melhores parametros, com isso conseguimos gerar o modelo final do projeto.

Gerado o modelo final, utilizamos a biblioteca joblib para salvar o modelo e criar um deploy do projeto, para que as pessoas pudessem utilizar esse modelo para prever se elas tem ou não diabetes.

![image](https://user-images.githubusercontent.com/49615892/161458512-5d8fe310-d03a-4136-bdd5-4ae2062df354.png)
