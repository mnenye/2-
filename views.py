from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import Data
from .__init__ import dataSort, randomDataSort
from django.forms.models import model_to_dict
from .tests import f

f()

def index(request):
    data = {
        'title': 'Справка',
    }
    return render(request, 'main/index.html', data)

def random_sort(request):
    array = randomDataSort()
    sort_array = dataSort(array)
    Data(oldData = array, sortData= sort_array).save()
    random_data = Data.objects.filter(id=Data.objects.last().id)
    random_dictionary = {
        'random_data' : random_data
    }

    return render(request, 'main/random_sort.html', random_dictionary)


def solve_sort(request):
    error = ''
    data = ''
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_sort_data = (model_to_dict(form_save)['oldData'])


            if form_sort_data == '':
                error = 'Вы не ввели исходные данные'
            else:
                ss = dataSort(form_sort_data)
                if ss == '':
                    error = 'Возможно вы ввели числа через запятую или ввели не целые числа'
                else:
                    form_save.sortData = ss
                    form_save = form.save()
                    data = Data.objects.filter(id=form_save.id)
        else:
            error = '! error error !'

    form = DataForm()
    solve_dictionary = {
        'data' : data,
        'form': form,
        'error': error,
    }
    return render(request, 'main/solve_sort.html',  solve_dictionary)
def history(request):
    data = Data.objects.all()
    if request.method == 'POST':
        data.delete()
    return render(request, 'main/history.html', {'data': data})