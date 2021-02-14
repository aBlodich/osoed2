import math
import mpmath
import numpy as np

def firstTask():
    y = 0 
    print("ОСОЭД лаб2 з1") 
    x = int(input("Введите x (целое число):")) 
    if x < 0: 
        y = math.log(-x) 
    elif x > 4: 
        y = math.atan(math.sqrt(x)) 
    else: y = math.cos(x*x)-x+math.sqrt(x+1) 
    print(y) 

def secondTask():
    print("\nОСОЭД лаб2 з2") 
    x = float(input("Введите x: "))
    while True:
        try:
            mode = int(input("Введите режим работы.\n1 - точность, 0 - кол-во слагаемых:"))
            firstFact = 1 ## первый факториал
            secondFact = 2 ## второй факториал факториал
            fitstFactStep = 1 ##переменная для расчета первого факториала с каждым новым шагом
            secFactStep = 3 ##переменная для расчета второго факториала g
            l = 4 ## 2 в степени 2
            numerator = float(x*x) ##числитель
            denominator = float(l*secondFact) ## знаменатель
            y = numerator/denominator ## искомая функция Бесселя
            if mode == 0: 
                n = int(input("Введите количество слагаемых: ")) 
                for i in range(n): 
                    numerator *= -x*x 
                    l *= 4 
                    secondFact *= secFactStep 
                    denominator = l*firstFact*secondFact 
                    y = y+numerator/denominator 
                    fitstFactStep += 1 
                    firstFact *= fitstFactStep  
                    secFactStep +=1
            else:
                e = float(input("Введите точность: "))
                while math.fabs(numerator/denominator) > e:
                    numerator *= -x*x 
                    l *= 4 
                    secondFact *= secFactStep 
                    denominator = l*firstFact*secondFact 
                    y = y+numerator/denominator 
                    fitstFactStep += 1 
                    firstFact *= fitstFactStep  
                    secFactStep +=1
        except:
            print("Вы ввели не число")
        else:
            print("Получившаяся функция Бесселя: %.5f" %y) 
            print("функция Бесселя, рассчитанная библиотекой mpmath: %.5f" %mpmath.besselj(2,x))
            break
        
def thirdTask(str):
    print("\nОСОЭД лаб2 з3")
    words = str.split()
    resultStr=""
    for word in words:
        if word.find("ab") != -1:
            resultStr += word+" "
    return resultStr

def fourthTask():
    print("\nОСОЭД лаб2 з4")
    n = int(input("Введите n: "))
    a = []
    b = []
    for i in range(n):
        a.append(int(input("Введите %.d элемент: " %(i+1))))
    print("Полученный массив A:", a)
    for i in range(1,n,2):
        b.append(a[i])
    for i in range(0,n,2):
        b.append(a[i])
    print("Полученный массив B: ", b)

def fifthTask():
    print("\nОСОЭД лаб2 з5")
    m = int(input("Введите m: "))
    n = int(input("Введите n: "))
    x = np.zeros((m,n),dtype=np.int32)
    if m < n:
        k = 0
        for i in range(m):
            x[i,i] = 2
            if i == 0:
                x[i,i+1] = 1
            else:
                x[i,i-1] = 1
                x[i,i+1] = 1
        
    else:
        k = 0
        for i in range(n):
            x[i,i] = 2
            if i == 0:
                x[i,i+1] = 1
            elif i == n-1:
                x[i,i-1] = 1
            else:
                x[i,i-1] = 1
                x[i,i+1] = 1
        for i in range(n,m):
            if i == n:
                x[i,0] = 1
            elif i > n and i < m:
                x[i,k] = 2
                k += 1
                if i == n+1:
                    x[i,k] = 1
                elif k == n:
                    x[i,k-2] = 1
                else:
                    x[i,k] = 1
                    x[i,k-2] = 1
    print(x)

def sixthTask():
    print("\nОСОЭД лаб2 з6")
    with open('input.txt','r') as f:
        s = f.read()
    x = np.zeros(20,dtype=np.int32)
    s = s.split()
    for i in range(20):
        x[i] = int(s[i]) 
    print("Выборка из файла:\n{0}".format(x))
    x.sort()
    print("Сортируем выборку:\n{0}".format(x))
    average = x.mean()
    print("Выборочное среднее:",average)
    mode = findMode(x)
    print("Мода:",mode)
    mediane = (x[9]+x[10])/2
    print("Медиана:",mediane)
    s = findDisperce(x,average,2)
    print("Дисперсия: %.5f" %s)
    so = math.sqrt(s)
    print("Стандартное отклонение: %.5f" %so)
    asimmetry = findDisperce(x,average,3)/(so*so*so)
    print("Асимметрия: %.5f" %asimmetry)
    exscess = findDisperce(x,average,4)/(so*so*so*so)
    print("Эксцесс: %.5f" %exscess)
    with open('output.txt','w') as f:
        print("Мода:",mode,file=f)
        print("Медиана:",mediane,file=f)
        print("Дисперсия: %.5f" %s,file=f)
        print("Стандартное отклонение: %.5f" %so,file=f)
        print("Асимметрия: %.5f" %asimmetry,file=f)
        print("Эксцесс: %.5f" %exscess,file=f)       
    
def findMode(x):
    a = 0
    b = 0
    c = 0
    mode = 0
    for n in range(19):
        if x[n]==x[n+1]:
            a+=1
        else: 
            a+=1
            c=a
            a=0
            if b < c:
                b=c
                mode=x[n]
    return mode

def findDisperce(x,average,n):
    s=0
    for i in x:
        s+=(i - average)**n
    s=s/19
    return s

def main():
    firstTask()
    secondTask()
    print(thirdTask("srweab frfab frfwrf ewfe tryabedge"))
    fourthTask()
    fifthTask()
    sixthTask()
    
if __name__=="__main__":
    main()



