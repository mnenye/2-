import time
from .models import Data
from random import randint
from .__init__ import dataSort

def testAdd100():
    start_time = time.time()
    test_success = True
    textt = 'Тест прошел успешно'
    for i in range(100):
        oo = ''
        for i in range(randint(2, 10)):
            i = randint(-100, 100)
            oo += str(i) + ' '
        Data(oldData= oo).save()
    finish_time = time.time() - start_time
    test_dictionary = {
        'textt': textt,
        'test_success': test_success,
        'finish_time': str(finish_time)
    }
    if test_dictionary['test_success']:
        print("Тест для 100 массивов: " + test_dictionary['textt'])
        print("Время выполнения: " + test_dictionary['finish_time'] + "\n")
        print("Выгрузка массивов: ")
        last_id = Data.objects.last().id
        first_id = Data.objects.first().id
        for i in range(first_id, last_id + 1):
            o_data = (list(Data.objects.filter(id=i).values_list('oldData', flat=True)))[0]
            print(str(i - first_id) + ". " + o_data)
    else:
        print("Тест для 100 массивов: " + test_dictionary['textt'])

def testAdd1000():
    start_time = time.time()
    test_success = True
    textt = 'Тест прошел успешно'
    for i in range(1000):
        oo = ''
        for i in range(randint(2, 10)):
            i = randint(-100, 100)
            oo += str(i) + ' '
        Data(old_data=oo).save()
    finish_time = time.time() - start_time
    test_dictionary = {
        'textt': textt,
        'test_success': test_success,
        'finish_time': str(finish_time)
    }
    if test_dictionary['test_success']:
        print("Тест для 1000 массивов: " + test_dictionary['textt'])
        print("Время выполнения: " + test_dictionary['finish_time'] + "\n")
        print("Выгрузка массивов: ")
        last_id = Data.objects.last().id
        first_id = Data.objects.first().id
        for i in range(first_id, last_id + 1):
            o_data = (list(Data.objects.filter(id=i).values_list('oldData', flat=True)))[0]
            print(str(i - first_id) + ". " + o_data)
    else:
        print("Тест для 1000 массивов: " + test_dictionary['textt'])

def testAdd10000():
    start_time = time.time()
    test_success = True
    textt = 'Тест прошел успешно'
    for i in range(10000):
        oo = str(randint(-100, 100)) + ' ' + str(randint(-100, 100)) + ' ' + str(randint(-100, 100)) + ' ' + str(randint(-100, 100)) + ' ' + str(randint(-100, 100)) + ' ' + str(randint(-100, 100)) + ' ' + str(randint(-100, 100))
        Data(oldData=oo).save()
    finish_time = time.time() - start_time
    test_dictionary = {
        'textt': textt,
        'test_success': test_success,
        'finish_time': str(finish_time)
    }

def testSort100():

    n = 0
    start_time = time.time()
    test_success = True
    textt = 'Тест прошел успешно'
    count = 0
    if Data.objects.last():
        last_id =  Data.objects.last().id
        first_id = Data.objects.first().id
    else:
        test_success = False
        test_dictionary = {
            'textt': 'Нечего сортировать',
            'test_success': test_success,
            'finish_time': 0
        }


    for i in range(first_id, last_id + 1):
        data = (list(Data.objects.filter(id=i).values_list('sortData', flat=True)))[0]
        if data == '':
            count+=1
    if count == 0:
        test_success = False
        test_dictionary = {
            'textt' : 'Нечего сортировать',
            'test_success': test_success,
            'finish_time': 0
        }


    if (last_id - first_id) + 1 < 100:
        rang = (last_id - first_id) + 1
    else:
        rang = 100
    for i in range(rang):
        while True:
            r_id = randint(first_id, last_id)
            data = (list(Data.objects.filter(id=r_id).values_list('sortData', flat=True)))[0]
            if data == '':
                break
        old_data_ofdata = (list(Data.objects.filter(id=r_id).values_list('oldData', flat=True)))[0]
        if data == '':
            ss = dataSort(old_data_ofdata)
            dd = Data(id= r_id)
            dd.sortData = ss
            dd.oldData = old_data_ofdata
            dd.save()
            n += 1
    if n != rang:
        n = 0
        test_success = False
        textt = 'Ошибка теста'
    finish_time = time.time() - start_time

    test_dictionary = {
        'textt': textt,
        'test_success': test_success,
        'finish_time': str(finish_time)
    }
    if test_dictionary['test_success']:
        print("Тест cортировки 100 массивов: " + test_dictionary['textt'])
        print("Время выполнения: " + test_dictionary['finish_time'] + "\n")
        print("Выгрузка массивов: ")
        last_id = Data.objects.last().id
        first_id = Data.objects.first().id
        for i in range(first_id, last_id + 1):
            o_data = (list(Data.objects.filter(id=i).values_list('oldData', flat=True)))[0]
            s_data = (list(Data.objects.filter(id=i).values_list('sortData', flat=True)))[0]
            print(str(i - first_id) + ". " + o_data + ", отсорт данные: " + s_data)
    else:
        print("Тест сортировки 100 массивов: " + test_dictionary['textt'])

def testClear():
    start_time = time.time()
    test_success = True
    textt = 'Тест прошел успешно'
    Data.objects.all().delete()
    finish_time = time.time() - start_time
    test_dictionary = {
        'textt': textt,
        'test_success': test_success,
        'finish_time': str(finish_time)
    }
    if test_dictionary['test_success']:
        print("Тест очистки массивов: " + test_dictionary['textt'])
        print("Время выполнения: " + test_dictionary['finish_time'])
    else:
        print("Тест очистки массивов: " + test_dictionary['textt'])

def f():
    testClear()
    print("---------------тесты для 100 массивов------------------")
    print("\n")
    testAdd100()
    print("\n")
    testSort100()
    print("\n")
    testClear()
    print("---------------тесты для 100 массивов------------------\n")


