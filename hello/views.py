from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

import csv

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors


# COURSE LIST VIEW
def courselist(request):

    courses = Course.objects.all()

    return render(
        request,
        'courselist.html',
        {'course_list1': courses}
    )


# CSV GENERATION VIEW
def generateCSV(request):

    courses = Course.objects.all()

    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = (
        'attachment; filename="course_data.csv"'
    )

    writer = csv.writer(response)

    # Header Row
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


# PDF GENERATION VIEW
def generatePDF(request):

    courses = Course.objects.all()

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="course_data.pdf"'
    )

    # Create PDF
    pdf = SimpleDocTemplate(
        response,
        pagesize=A4
    )

    # Table Data
    table_data = [[
        'Course Code',
        'Course Name',
        'Credits'
    ]]

    # Add Course Data
    for c in courses:

        table_data.append([
            c.coursecode,
            c.coursename,
            c.credits
        ])

    # Create Table
    table = Table(table_data)

    # Table Styling
    style = TableStyle([

        # Header Background
        (
            'BACKGROUND',
            (0, 0),
            (-1, 0),
            colors.lightblue
        ),

        # Header Text Color
        (
            'TEXTCOLOR',
            (0, 0),
            (-1, 0),
            colors.black
        ),

        # Header Font
        (
            'FONTNAME',
            (0, 0),
            (-1, 0),
            'Helvetica-Bold'
        ),

        # Header Font Size
        (
            'FONTSIZE',
            (0, 0),
            (-1, 0),
            12
        ),

        # Padding
        (
            'BOTTOMPADDING',
            (0, 0),
            (-1, 0),
            10
        ),

        # Background for Data Rows
        (
            'BACKGROUND',
            (0, 1),
            (-1, -1),
            colors.beige
        ),

        # Grid Borders
        (
            'GRID',
            (0, 0),
            (-1, -1),
            1,
            colors.black
        ),

        # Alignment
        (
            'ALIGN',
            (0, 0),
            (-1, -1),
            'CENTER'
        ),

    ])

    table.setStyle(style)

    # Build PDF
    pdf.build([table])

    return response