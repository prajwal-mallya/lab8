from django.urls import path
from .views import (
    courselist,
    generateCSV,
    generatePDF
)

urlpatterns = [

    path(
        'courses/',
        courselist,
        name='course_list'
    ),

    path(
        'courses/generateCSV/',
        generateCSV,
        name='generate_csv'
    ),

    path(
        'courses/generatePDF/',
        generatePDF,
        name='generate_pdf'
    ),

]