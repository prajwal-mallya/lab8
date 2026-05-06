from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

import csv

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table

# Display Course List
def courselist(request):
    courses = Course.objects.all()

    return render(
        request,
        'courselist.html',
        {'course_list1': courses}
    )


# CSV Download
def generateCSV(request):

    courses = Course.objects.all()

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = (
        'attachment; filename="course_data.csv"'
    )

    writer = csv.writer(response)

    # Header
    writer.writerow([
        'Course Code',
        'Course Name',
        'Credits'
    ])

    # Data Rows
    for c in courses:
        writer.writerow([
            c.coursecode,
            c.coursename,
            c.credits
        ])

    return response


# PDF Download
def generatePDF(request):

    courses = Course.objects.all()

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="course_data.pdf"'
    )

    pdf = SimpleDocTemplate(
        response,
        pagesize=A4
    )

    table_data = [[
        'Course Code',
        'Course Name',
        'Credits'
    ]]

    for c in courses:
        table_data.append([
            c.coursecode,
            c.coursename,
            c.credits
        ])

    table = Table(table_data)

    pdf.build([table])

    return response