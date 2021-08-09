# Загрузка библиотек

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


# Загрузка датасета из URL-адреса

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read(url, names=names)

# Загрузка датасета из локального файла

path = "csv/iris.csv"
dir = os.path.dirname(__file__)
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset1 = read(os.path.join(dir, path), delimiter=",", names=names)

# # shape
# print(dataset.shape)
# 
# # Срез данных head
# print(dataset.head(20))
#
# # Стастические сводка методом describe
# print(dataset.describe())
#
# # Распределение по атрибуту class
# print(dataset.groupby('class').size())

# Диаграмма размаха
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

#Матрица диаграмм рассеяния
#scatter_matrix(dataset)
# pyplot.show()

# Гистограмма распределения атрибутов датасета
#dataset.hist()
# pyplot.show()

# Разделение датасета на обучающую и контрольную выборки
array = dataset.values

# Выбор первых 4-х столбцов
X = array[:,0:4]

# Выбор 5-го столбца
y = array[:,4]

# Разделение X и y на обучающую и контрольную выборки
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

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

#print('-------------------->')

for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	#print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Сравниванием алгоритмы
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

#print(dataset)
# print(dataset2)

# Создаем прогноз на контрольной выборке
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)


# Оцениваем прогноз
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
