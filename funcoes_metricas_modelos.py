from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


def dividir_modelo(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)
    return X_train, X_test, Y_train, Y_test
     
def avaliar_modelo(nome_modelo, y_teste, previsao):
    acuracia = accuracy_score(y_teste, previsao)
    precisao = precision_score(y_teste, previsao)
    recall = recall_score(y_teste, previsao)
    f1 = f1_score(y_teste, previsao)
    auc = roc_auc_score(y_teste, previsao)
    matrix_conf = confusion_matrix(y_teste, previsao, labels = [1, 0])
    especificidade = round(matrix_conf[0,0]/(matrix_conf[0,0] + matrix_conf[0, 1]),3)
    sensibilidade = round(matrix_conf[1,1]/(matrix_conf[1,1]+matrix_conf[1,0]),3)
    return f'Modelo {nome_modelo}:\nAcuracia:{acuracia:.2%}\nPrecisão:{precisao:.2%}\nRecall:{recall:.2%}\nF1_Score:{f1:.2%}\nAUC:{auc:.2%}\nEspecificidade:{especificidade:.2%}\nSensibilidade{sensibilidade:.2%}'
