import os

from matplotlib import pyplot
from pandas import read_csv as read
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import os

from Basics.GenerateDatasets import GenerateDatasets

temp_dir = 'csv/1.csv'
gdc = GenerateDatasets()
gdc.generate(500, temp_dir, size=3)

dir = os.path.dirname(__file__)
names = ['t1', 't2', 't3', 't4',
         't5', 't6', 't7', 't8',
         't9', 't10', 't11', 't12',
         't13', 't14', 't15', 't16', 't17', 't18', 'result']
dataset = read(os.path.join(dir, temp_dir), delimiter=",", names=names)

print(dataset.head(20))

# dataset.plot(kind='box', subplots=True, layout=(8, 8), sharex=False, sharey=False)
#
# scatter_matrix(dataset)
# pyplot.show()

# Разделение датасета на обучающую и контрольную выборки
array = dataset.values

# Выбор первых 16-х столбцов
X = array[:, 0:16]

# Выбор 17-го столбца
y = array[:, 16]

# Разделение X и y на обучающую и контрольную выборки
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.80, random_state=1)

# Загружаем алгоритмы модели
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# оцениваем модель на каждой итерации
results = []
names = []

# print('-------------------->')

for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
# print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Сравниванием алгоритмы
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

# print(dataset)
# print(dataset2)

# Создаем прогноз на контрольной выборке
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Оцениваем прогноз
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
