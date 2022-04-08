# pages/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import pandas as pd
from pycaret.classification import *

valid_choices_home = {
    'genders': ['Male', 'Female'],
    'hypertension': ['Yes', 'No'],
    'heart_disease': ['Yes', 'No'],
    'ever_married': ['Yes', 'No'],
    'work_type': ['children', 'Government Job', 'Never Worked', 'Private', 'Self-employed'],
    'Residence_type': ['Rural', 'Urban'],
    'smoking_status': ['formerly smoked', 'never smoked', 'smokes', 'Unknown'],
}

error_home = {
    'errorMessage': '*** The data submitted is invalid. Please try again.',
    'genders': ['Male', 'Female'],
    'hypertension': ['Yes', 'No'],
    'heart_disease': ['Yes', 'No'],
    'ever_married': ['Yes', 'No'],
    'work_type': ['children', 'Government Job', 'Never Worked', 'Private', 'Self-employed'],
    'Residence_type': ['Rural', 'Urban'],
    'smoking_status': ['formerly smoked', 'never smoked', 'smokes', 'Unknown'],
}


def convertJobStr(value):
    if value == "Government Job":
        return "Govt_job"
    elif value == "Never Worked":
        return "Never_worked"
    else:
        return value


def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', valid_choices_home)


def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')


def homePost(request):
    # Use request object to extract choice.

    try:
        # Extract value from request object by control name.
        features = {
            'gender': request.POST['gender'],
            'age': int(request.POST['age']),
            'hypertension': 1 if request.POST['hypertension'] == 'Yes' else 0,
            'heart_disease': 1 if request.POST['heart_disease'] == 'Yes' else 0,
            'ever_married': request.POST['ever_married'],
            'work_type': convertJobStr(request.POST['work_type']),
            'Residence_type': request.POST['Residence_type'],
            'avg_glucose_level': float(request.POST['avg_glucose_level']),
            'bmi': float(request.POST['bmi']),
            'smoking_status': request.POST['smoking_status']
        }

        print(features)
    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', error_home)
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs=features,))


def results(request, gender, age, hypertension, heart_disease, ever_married,
            work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
    print("*** Inside results()")
    # load saved model
    model = load_model('stacked_final_stroke_predict')
    df = pd.DataFrame({
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married,
        'work_type': work_type,
        'Residence_type': Residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }, index=[0])
    print(df)
    print(predict_model(model, data=df))

    return render(request, 'results.html', {'choice': 1, 'gmat': 1})
