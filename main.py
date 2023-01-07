import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

import os

file_path=os.getcwd()
filedata=[]
data=[]
data2=[]
temperature=[]
nausea=[]
l_pain=[]
urine=[]
m_pains=[]
burning=[]
inflamation_u=[]
nephritis=[]

with open(file_path+ '\\diagnosis.data' , 'r') as file:
    filedata=file.read().splitlines()
    for i in filedata:
        data.append(i.split('\t'))
    for i in range(len(data)):
        data2=data2+data[i]
    for i in range(0, len(data2), 8):
        x=data2[i].replace(",", ".")
        temperature.append(float(x))

    for i in range(1, len(data2), 8):
        if(data2[i]=='no'):
            nausea.append(0)
        else:
            nausea.append(1)

    for i in range(2, len(data2), 8):
        if(data2[i]=='no'):
            l_pain.append(0)
        else:
            l_pain.append(1)

    for i in range(3, len(data2), 8):
        if(data2[i]=='no'):
            urine.append(0)
        else:
            urine.append(1)

    for i in range(4, len(data2), 8):
        if(data2[i]=='no'):
            m_pains.append(0)
        else:
            m_pains.append(1)

    for i in range(5, len(data2), 8):
        if(data2[i]=='no'):
            burning.append(0)
        else:
            burning.append(1)

    for i in range(6, len(data2), 8):
        if(data2[i]=='no'):
            inflamation_u.append(0)
        else:
            inflamation_u.append(1)

    for i in range(7, len(data2), 8):
        if(data2[i]=='no'):
            nephritis.append(0)
        else:
            nephritis.append(1)

temperature=np.array(temperature)
nausea=np.array(nausea)
l_pain=np.array(l_pain)
urine=np.array(urine)
m_pains=np.array(m_pains)
burning=np.array(burning)
inflamation_u=np.array(inflamation_u)
nephritis=np.array(nephritis)

m = np.array([temperature, nausea, l_pain, urine, m_pains, burning, inflamation_u, nephritis])

m = m.T
X_train, X_test, Y_train, Y_test = train_test_split(m[:,:6], m[:,6:], test_size=0.25)

inflam_train = Y_train[:, 0]
nephr_train = Y_train[:, 1]
inflam_test  = Y_test[:, 0]
nephr_test = Y_test[:, 1]


for i in range(-5, 9, 2):
    clf = svm.SVC(kernel='linear', C=2 ** i, gamma=1).fit(X_train, inflam_train)
    predictie = clf.predict(X_test)
    acuratete_Y = metrics.accuracy_score(y_true=inflam_test, y_pred=predictie)
    print("Acuratetea pentru inflammation of urinary bladder pentru costul", 2 ** i, "este", acuratete_Y)



for i in range(-5, 9, 2):
    clf = svm.SVC(kernel='linear', C=2 ** i, gamma=1).fit(X_train, nephr_train)
    predictie = clf.predict(X_test)
    acuratete_Z = metrics.accuracy_score(y_true=nephr_test, y_pred=predictie)
    print("Acuratetea pentru nephritis of renal pelvis origin pentru costul", 2 ** i, "este", acuratete_Z)
