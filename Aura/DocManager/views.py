from django.shortcuts import render, redirect
from django.http import JsonResponse
from .serializers import *

from .models import *
from datetime import datetime
# from PIL import Image


# Create your views here.
import os

current_path = os.path.join(os.getcwd(), 'Documents')


def upload_doc(request):
    pass


def doc_viewer(request, z):
    if request.method == 'POST' and  request.POST['holder_name'] != 'All_records':
        print(request.POST['holder_name'])
        query = docma.objects.filter(type=z, holder= request.POST['holder_name'])
        select = request.POST['holder_name']
    else:
        query = docma.objects.filter(type=z)
        select = 'All_records'
    data = []
    for i in query:
        data.append([350, 225, i.document, i.number, i.holder, i.document_back])
    holders = doc_holder.objects.all()

    context = {
        'record': query,
        'data': data,
        'holder': holders,
        'url':z ,
        'select' : select
    }

    return render(request, 'doc_viewer.html', context)


def docma_cat(request):
    # query1 = doc_type.objects.values_list('type', flat=True)
    query1 = docma.objects.values('type').distinct()
    set = []
    subset = []
    for i, j in enumerate(query1):
        print(i, j['type'])
        i = i + 1
        subset.append(j['type'])
        if i % 3 == 0:
            set.append(subset)
            subset = []
    if len(subset) > 0:
        set.append(subset)

    print(set)

    context = {
        'doc_type': set

    }

    return render(request, 'doc_cat.html', context)


def docma_test(request):
    current_user = request.user

    if request.method == 'POST':

        type = request.POST['doc_type']
        docno = request.POST['doc_no']
        docuser = request.POST['doc_user']
        edate = request.POST['edate']
        sdate = request.POST['sdate']
        value = request.POST['value']
        file_front = request.FILES['file_f']
        remarks = request.POST['remarks']
        print(type, docno, docuser, edate, sdate, value)
        data = docma(holder=docuser,
                     number=docno,
                     document=file_front,
                     end_date=edate,
                     date=sdate,
                     value=value,
                     type=type,
                     time_stamp=datetime.now(),
                     remarks=remarks,
                     updated_by=current_user.username
                     )

        if 'file_b' in request.FILES:
            data.document_back = request.FILES['file_b']
        else:
            print("file not present --------------------------")

        data.save()
        return redirect('/doccat/')

    query1 = doc_type.objects.values_list('type', flat=True)

    query2 = doc_holder.objects.values_list('Holder', flat=True)

    # print(query)
    # print("------------------------------------------------------------------------------------")

    context = {
        'doc_cat': query1,
        'doc_holder': query2,
    }

    return render(request, "docma.html", context)


def get_docdata(request):
    query = docma.objects.all()

    ata = docmaSerializer(query, many=True)

    return JsonResponse(ata.data, safe=False)
