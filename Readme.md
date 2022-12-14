## Лабораторная по компьютерному зрению №1
Эрозия. Задан примитив размера 3 на 3. На вход поступает изображение,
программа отрисовывает окно, в которое выводится либо исходное
изображение после бинаризации, либо после эрозии (переключение по
нажатию клавиши). Базовый алгоритм - эрозия.

OpenCV-Библиотека алгоритмов компьютерного зрения, обработки изображений и численных алгоритмов общего назначения с открытым кодом. Реализована на C/C++, также разрабатывается для Python, Java, Ruby, Matlab, Lua и других языков. Может свободно использоваться в академических и коммерческих целях - распространяется в условиях лицензии BSD.

Морфологические операции над изображениями позволяют удалить
артефакты или выделить границы объектов на изображении
Основными операциями являются дилатация и эрозия
В обеих операциях необходимо заранее выбрать структурный элемент
При эрозии структурный элемент перемещается по изображению и в
итоговом изображении 1 записывается только в тот пиксель, где все
пиксели исходного изображения и структурного элемента совпали
\
Подключение библиотек
```
import cv2
import numpy as np
```

Объявление пременной, примитива 3 на 3
```
p=False
primitiv = np.array([[255, 255, 0],
                     [255, 255, 0],
                     [0, 0, 0]],  np.uint8)
m0 = np.zeros((3, 3))
```
Подключение к камере и задание формы экрана
```
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 300)
```

Преобразование изображения к серому фону и бинаризация изображение
Бинаризация -операция преобразования многоградационного
изображения в изображение, содержащего только два
значения пикселя: 0 и 1.
```
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY=0?
```


Если нажата пробел необходимо произвести 
операцию эрозию.
```
if  p==True:
    img = cv2.erode(img, primitiv,iterations = 1)
```

Выполнять цикл, склеивание картинки, пока не нажата кнопка 'q'
```
while True:
    succes, img = cap.read() 
    cv2.imshow("Image", img)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
```
Приимер выполнения программы\
Бинеризация
![Бинеризация](1.1.png)

Эрозия
![Бинеризация](1.1 ercode.png)
Эрозия уменьшает область изображения, приводя к истончению пикселей, расширяя и усиливая светлые места на изображении.
Суть данного преобразования состоит в том, что нежелательные вкрапления и шумы размываются, а большие и, соответственно, значимые участки изображения изменениям не подвергаются.
Это операция определения локального минимума по некоторой окрестности, которая задается структурообразующим элементом.

## Реализация алгоритма

Для упрощения задачи и наглядного выполнения будем использлвать картинку

```
import cv2
import numpy as np
import time
```

Функция сравнения двух массиовов
```
def func_equal(a, b):
    y1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    y2 = np.zeros((3, 3))
    k=0
    for i in range(0,3):
        for j in range(3):
            if a[i][j] == b[i][j]:
                  k += 1
    if k == 9:
        y=255
    else:
        y=0
    return y
```

Обявление переменных
```
primitiv = np.array([[255, 255, 255],
                     [255, 255, 255],
                     [255, 255, 255]])
m0 = np.zeros((3, 3))
p=0
```

Загрузка изображения image_1.jpg, преобразование в бинарный вид
```
img = cv2.imread('image_1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY=0?
```


   Фиксация времени начала алгортма эрозии
```
start_time = time.time()
```
Обнуление   n0
```
n0 = np.zeros((360, 640))
```
Проходим по горизанали затем по вртекали изображения
```
 while i < 350:#img.shape[0] -10:
    while j < 630:# img.shape[1] - 10:
```

Если исходное изображение совпало, то возвращаем значение
1, в противном случае 0
```
 n0[i+1][j+1]=func_equal(img[i:i + 3, j:j + 3],primitiv[0:3, 0:3])
```
Время работы алгоритма эрозии 
```
print("Execution time of the program is- ", time.time() - start_time)
```
Приимер выполнения программы\
Бинеризация
![Бинеризация](1.3.png)
Реализованный алгоритм эрозии
![Бинеризация](1.3 ercode.png)

## Третий ваиант реализации с ипользованием библиотеки Numba

Python – не самый быстрый язык, но недостаток скорости не помешал ему стать важной силой в аналитике, машинном обучении и других дисциплинах, требующих обработки сложных чисел. Его простой синтаксис и общая простота использования делают Python изящным интерфейсом для библиотек, которые выполняют всю тяжелую работу с числами.

Numba, созданная людьми, стоящими за дистрибутивом Anaconda Python, использует подход, отличный от большинства математических и статистических библиотек Python. Обычно такие библиотеки, такие как NumPy, для научных вычислений, заключают высокоскоростные математические модули, написанные на C, C ++ или Fortran, в удобную оболочку Python. Numba преобразует ваш код Python в высокоскоростной машинный язык с помощью своевременного компилятора или JIT.
```
import numba
@numba.jit()
```
Время выполнения программ

| Реализация             | t1, с |  t2, с  | t3, с  |
|------------------------|:-----:|:-------:|:------:|
| OpenCV                 | 0.001 |  0.02   | 0.0005 
| Алгоритм эрозия        | 2.26  |  38.87  |  7.55  
|Алгоритм эрозия с Numba | 1.64  |  4.41   |  2.12  

Агализ исходных изображений

| Параметры  | image1  |  image2  | image3 |
|------------|:-------:|:--------:|:------:|
| Разрешение | 640-426 | 1083-908 | 480-360 
| Размер, Кб |   56    |   122    |  33  

Отличие изображений в пикселях 
```
result = np.array(img1-img2)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))
```
|  | image1-image2  | image1-image3 | image2-image3 |
|------------|:--------------:|:-------------:|:-------------:|
| OpenCV   |      0.0       |      0.0      |     0.0   
| Алгоритм эрозия |     0.012      |     0.009     |  0.0027      
| image3     |     0.009      |     0.009     |     0.0      



В ходе данной работы, произведено ознакомление с библиртеками OpenCV. 
Изуены следующие функции:
* работа с камероой 
* работа с видеопотоком 
* бинаризация
* эрозия 

Так же реализован алгоритм эрозии. Следует отметить, использввание библиотеки Numba ускоряет процесс. 
Больше примеров работы программ представлено в репозитории папке outputs. \
Список использованной литературы
Общая документация по OpenCV: https://docs.opencv.org/ \
Eroding and Dilating: https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html \
Анализ и обработка изображений с использованием операций математической морфологии, python и библиотеки OpenCV: https://habr.com/ru/post/565378/