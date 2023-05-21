from django.shortcuts import render

# Create your views here.
import os

current_path = os.path.join(os.getcwd(), 'Documents')


def upload_doc(request):
    pass


def save_doc_data(request, doc_type, doc):
    doc_type = 'Aadhar_card'
    print("path:", os.listdir(current_path))
    if doc_type in os.listdir(current_path):
        pass

    return render(request, 'jarvis_ui.html')
    pass
    # get data from front end

    # do calculation

    # uoload doc

    # return
