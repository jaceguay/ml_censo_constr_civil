# %%
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# %%
# dados
data = read_csv('dados_selecionados_join.csv')

# Definir tamanho das amostras:
teste_size = 0.3

# Garantir que os resultados podem ser reproduzidos no estado randômico:
seed = 7

# Criando os conjuntos de dados de treino e de teste
# array = data.iloc[:, 1:].values
array = data.values
x = array[:, 0:45]
y = array[:, 45]
x_treino, x_teste, y_treino, y_teste = model_selection.train_test_split(
    x, y, test_size=teste_size, random_state=seed)

# %%[markdown]
# ## Regressão logística

# %%
modelorl = LogisticRegression()
modelorl.fit(x_treino, y_treino)
# matriz de confusão:
predrl = modelorl.predict(x_teste)
matrl = confusion_matrix(y_teste, predrl)
print("Matriz de confusão: \n"+str(matrl))
# %%
acuraciarl = modelorl.score(x_teste, y_teste)
print("\nAcurácia: "+str(acuraciarl*100)+"%")

# %%
modelorl.predict(data.iloc[:, 0:45])

# %%[markdown]
# ## KNN:

# %%
# Criação do modelo
modeloknn = KNeighborsClassifier()
modeloknn.fit(x_treino, y_treino)

# matriz de confusão:
predknn = modeloknn.predict(x_teste)
matknn = confusion_matrix(y_teste, predknn)
print("Matriz de confusão: \n"+str(matknn))

# %%
# acurácia:
acuraciaknn = modeloknn.score(x_teste, y_teste)
print("\nAcurácia: "+str(acuraciaknn*100)+"%")

# %%
modeloknn.predict(data.iloc[:, 0:45])

# %%[markdown]
# ## SVM

# %%
# Criação do modelo
modelosvm = SVC()
modelosvm.fit(x_treino, y_treino)

# matriz de confusão:
predsvm = modelosvm.predict(x_teste)
matsvm = confusion_matrix(y_teste, predsvm)
print("Matriz de confusão: \n"+str(matsvm))

# %%
# acurácia:
acuraciasvm = modelosvm.score(x_teste, y_teste)
print("\nAcurácia: "+str(acuraciasvm*100)+"%")

# %%
modelosvm.predict(data.iloc[:, 0:45])

# %%[markdown]
# ## Naive Bayes

# %%
# Criação do modelo
modelonb = GaussianNB()
modelonb.fit(x_treino, y_treino)

# matriz de confusão:
prednb = modelonb.predict(x_teste)
matnb = confusion_matrix(y_teste, prednb)
print("Matriz de confusão: \n"+str(matnb))

# %%
# acurácia:
acuracianb = modelonb.score(x_teste, y_teste)
print("\nAcurácia: "+str(acuracianb*100)+"%")

# %%
modelonb.predict(data.iloc[:, 0:45])

# %%[markdown]
# ## Árvore de decisão

# %%
# Criação do modelo
modeloarvd = DecisionTreeClassifier()
modeloarvd.fit(x_treino, y_treino)

# matriz de confusão:
predarvd = modeloarvd.predict(x_teste)
matarvd = confusion_matrix(y_teste, predarvd)
print("Matriz de confusão: \n"+str(matarvd))

# %%
# acurácia:
acuraciaarvd = modeloarvd.score(x_teste, y_teste)
print("\nAcurácia: "+str(acuraciaarvd*100)+"%")

# %%
modeloarvd.predict(data.iloc[:, 0:45])

# %%[markdown]
# ## Random Forest

# %%
# Criação do modelo
num_arvores = 50
max_features = 8
modelorf = RandomForestClassifier(
    n_estimators=num_arvores, max_features=max_features)
modelorf.fit(x_treino, y_treino)

# matriz de confusão:
predrf = modelorf.predict(x_teste)
matrf = confusion_matrix(y_teste, predrf)
print("Matriz de confusão: \n"+str(matrf))

# %%
# acurácia:
acuraciarf = modelorf.score(x_teste, y_teste)
print("\nAcurácia: "+str(acuraciarf*100)+"%")

# %%
modelorf.predict(data.iloc[:, 0:45])
