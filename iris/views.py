from django.shortcuts import render
from .forms import IrisForm
from .ml_model.ml_classifier import predict, string_category

# Create your views here.


def index(request):
    if request.method == 'POST':
        sepal_length = request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepal_width')
        petal_length = request.POST.get('petal_length')
        petal_width = request.POST.get('petal_width')
        prediction = predict([[sepal_length, sepal_width, petal_length, petal_width]],
                             model_path='iris/ml_model/model.joblib')
        category = string_category(prediction)
        parameters_form = IrisForm()
        result = 'Looks like is\'s ' + category
        return render(request, 'index.html', {'form': parameters_form, 'result': result})
    else:
        parameters_form = IrisForm()
        return render(request, 'index.html', {'form': parameters_form, 'result': '...'})