# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, results, homePost


urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('results/<str:gender>/<int:age>/<int:hypertension>/<int:heart_disease>/<str:ever_married>/<str:work_type>/<str:Residence_type>/<str:avg_glucose_level>/<str:bmi>/<str:smoking_status>/', results, name='results'),
]
