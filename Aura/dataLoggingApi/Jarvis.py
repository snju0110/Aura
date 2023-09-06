
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from dataLoggingApi.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum
from datetime import datetime, date
from datetime import timedelta
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from views import page_logout_msg


def page_logout_msg():
    return JsonResponse({'Message: ': 'Kindly login first'}, safe=False)


def Jarvis_Headsup(request):
    current_user = request.user
    user = current_user.username

    if user:

        talk_data = 'Ask here !'
        phrase_word = ''

        if request.method == 'POST':
            phrase_word = request.POST["phrase"]
            print("---------------------------------------------------------------phrase_word :", phrase_word)
            talk_data = wikipedia.summary("phrase_word", sentences=2)
            print(talk_data)
            print("|" + str(phrase_word) + "|")
        today = date.today()
        parsed_today = today.strftime("%Y-%m-%d")
        startdate = str(date.today()).split('-')
        MonthStartDate = str(startdate[0]) + '-' + str(startdate[1]) + '-01'
        selected_date = {'from_date': MonthStartDate, 'to_date': parsed_today}

        monthly_type_data = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user).values(
            'type').annotate(
            total_amount=Sum('amount'))
        print(monthly_type_data)

        category_data = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user).values(
            'primaryCat').annotate(
            total_amount=Sum('amount'))
        print(category_data)
        datewisespent = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user,
                                                    type='Sent').exclude(primaryCat="Skip").values(
            'date').annotate(
            total_amount=Sum('amount'))
        data = {}
        m_ate = []
        m_spen = []
        for i in datewisespent:
            q_date = i['date']
            f_date = q_date.strftime("%Y-%m-%d")
            # data[f_date] = i['total_amount']
            m_ate.append(f_date)
            m_spen.append(i['total_amount'])

        context = {
            'dem_monthly': monthly_type_data,
            'dem_category': category_data,
            'talk_data': talk_data,
            'm_ate': m_ate,
            'm_spen': m_spen,

        }

        if phrase_word == 'open document manager':
            return redirect('/docma/')
        else:
            return render(request, "jarvis_wings_test.html", context)
            # return render(request, "jarvis_wings_test.html")
    else:
        # return JsonResponse({'Message': 'Kindly login first'}, safe=False)
        return page_logout_msg()
