from django.shortcuts import render
from .models import Subject
from django.contrib.auth.decorators import login_required


def subjects(request):
    subjects_list = Subject.objects.all()
    # CSS-Klassen vorbereiten
    prepared_subjects = []
    for s in subjects_list:
        css_class = s.name.lower().replace(" ", "-")
        if css_class not in ['math','english','biologie']:
            css_class = 'default-subject'
        prepared_subjects.append({
            "name": s.name,
            "css_class": css_class
        })

    return render(request, "studyflow/subjects.html", {"subjects": prepared_subjects})
