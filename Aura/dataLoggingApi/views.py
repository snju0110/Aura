# sanjay > aura > pythonanywhere > github
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
import wikipedia


def page_logout_msg():
    return JsonResponse({'Message: ': 'Kindly login first'}, safe=False)


# @api_view(['GET', 'POST', 'PUT'])
# def food_daily_data(requests):
#     if requests.method == 'GET':
#         queryset = foodDailyData.objects.all()
#         serializer = foodDailyDataSerializer(queryset, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     if requests.method == 'POST':
#         serializer = foodDailyDataSerializer(data=requests.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#

@api_view(['GET', 'POST', 'PUT'])
def DemDailyData(requests):
    if requests.method == 'GET':
        queryset = demDailyData.objects.all()
        serializer = demDailyDataSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    if requests.method == 'POST':
        serializer = demDailyDataSerializer(data=requests.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if requests.method == 'PUT':
        serializer = demDailyDataSerializer(data=requests.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT'])
def edit_records(request, id):
    if request.method == 'GET':
        p_cat_setting = settingDemCategory.objects.values_list('primary_category', flat=True)

        print("Records pushed for ID: {id}".format(id=id))
        queryset = demDailyData.objects.get(id=id)
        queryset.date.strftime("%Y-%m-%d")
        context = {
            'formData': queryset,
            'p_cat_setting': p_cat_setting
        }
        print(context)
        return render(request, "dem_record_edit_form.html", context)
    if request.method == 'POST':
        print("request for edit record for ID: {id}".format(id=id))
        user = request.POST["user"]
        amount = request.POST["amount"]
        sf = request.POST["sf"]
        st = request.POST["st"]
        t_date = request.POST["date"]
        tm = request.POST["tm"]
        Ttype = request.POST["Ttype"]
        cat = request.POST["cat"]
        pcat = request.POST["gc"]
        trip = request.POST["trip"]

        data = demDailyData.objects.filter(id=id).update(
            user=user, date=t_date, amount=amount, sentFrom=sf, sentTo=st, message=tm, type=Ttype, primaryCat=cat,
            groupCat=pcat, trip=trip)

        print("New edited data: ", id, user, sf, st, date, tm, Ttype, cat, amount, pcat)
        return MonthTable(request)


def Logout(request):
    auth.logout(request)
    print("logged out")
    return redirect("/")


def Login(request):
    if request.method == 'POST':
        name = request.POST['UserName']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            print("Logged in as ", user)
            return redirect('Head_display')
        else:
            print("login failed")
            messages.info(request, "Check User name or password")
            return render(request, "login_page.html")
    else:
        pass

    return render(request, "login_page.html")


@api_view(['POST'])
def app_login(request):
    if request.method == 'POST':
        appuserdata = request.data
        try:
            user = auth.authenticate(username=appuserdata['username'], password=appuserdata['password'])

            if user is not None:
                return JsonResponse({'Login': True}, safe=False)
            else:
                return JsonResponse({'Login': False}, safe=False)
        except:
            return JsonResponse({'Login': False}, safe=False)


def DemMainPage(request):
    current_user = request.user
    user = current_user.username

    if user:

        try:
            current_user = request.user
            print(current_user.id)
            MonthStartDate = request.GET["fdate"]

            today = request.GET["tdate"]

            formatted_today = datetime.strptime(today, "%Y-%m-%d")
            yesterday = formatted_today - timedelta(days=1)
            print(yesterday)
            print("---- input got from front end")
            selected_date = {'from_date': MonthStartDate, 'to_date': today}
            print("selected dates : ", selected_date)
        except:
            today = date.today()
            parsed_today = today.strftime("%Y-%m-%d")
            startdate = str(date.today()).split('-')
            MonthStartDate = str(startdate[0]) + '-' + str(startdate[1]) + '-01'
            yesterday = today - timedelta(days=1)
            selected_date = {'from_date': MonthStartDate, 'to_date': parsed_today}
            print("selected dates : ", selected_date)

        current_user = request.user
        user = current_user.username

        monthlydata = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user).exclude(
            primaryCat="Skip").values('type').annotate(
            total_amount=Sum('amount'))

        print(monthlydata)
        datewisespent = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user,
                                                    type='Sent').exclude(
            primaryCat="Skip").values(
            'date').annotate(
            total_amount=Sum('amount'))
        datewiserecv = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user,
                                                   type='Received').values(
            'date').annotate(
            total_amount=Sum('amount'))

        ydata = demDailyData.objects.filter(date=yesterday, user=user).values('type').annotate(
            total_amount=Sum('amount'))
        category_data = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user).values(
            'primaryCat').annotate(total_amount=Sum('amount'))

        last5 = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user).order_by('-date')[:5]

        cat, catVal = [], []
        days, day_spent = [], []
        dayr, day_recv = [], []

        for i in category_data:
            if i['primaryCat'] not in ('Received_NC', 'Others', 'Skip'):
                cat.append(i['primaryCat'])
                catVal.append(i['total_amount'])

        for i in datewisespent:
            q_date = i['date']
            f_date = q_date.strftime("%Y-%m-%d")
            days.append(f_date)
            day_spent.append(i['total_amount'])
        for i in datewiserecv:
            q_date = i['date']
            f_date = q_date.strftime("%Y-%m-%d")
            dayr.append(f_date)
            day_recv.append(i['total_amount'])
        print(day_spent)
        context = {
            'monthlydata': monthlydata,
            'set1': last5,
            'cat': cat,
            'catVal': catVal,
            'days': days,
            'day_spent': day_spent,
            'dayr': dayr,
            'day_recv': day_recv,
            'category_data': category_data,
            'ydata': ydata,
            'selected_date': selected_date

        }

        return render(request, "dem_main_page.html", context)
    else:
        return page_logout_msg()


def MonthTable(request):
    current_user = request.user
    user = current_user.username
    if user:
        try:
            MonthStartDate = request.GET["fdate"]
            today = request.GET["tdate"]
            column_filter = request.GET["column_filter"]
            selected_date = {'from_date': MonthStartDate, 'to_date': today, "column_filter": column_filter}
            print("selected dates : ", selected_date)
        except:
            today = date.today()
            parsed_today = today.strftime("%Y-%m-%d")
            startdate = str(date.today()).split('-')
            MonthStartDate = str(startdate[0]) + '-' + str(startdate[1]) + '-01'
            selected_date = {'from_date': MonthStartDate, 'to_date': parsed_today, "column_filter": 'All_records'}
            print("Auto sleleced for month", selected_date)

        p_cat_setting = settingDemCategory.objects.values_list('primary_category', flat=True)

        if selected_date['column_filter'] == 'All_records':
            set = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user, ).order_by('-date')
        else:
            set = demDailyData.objects.filter(date__range=[MonthStartDate, today], user=user,
                                              primaryCat=selected_date['column_filter']).order_by('-date')

        context = {
            'set': set,
            'selected_date': selected_date,
            'p_cat_setting': p_cat_setting
        }
        return render(request, "dem_monthly_record_table.html", context)
    else:
        return page_logout_msg()


@api_view(['GET', 'POST', 'PUT'])
def test_case_a(request):
    # if request.method == 'POST':
    #     print(request.data)
    # if request.method == 'GET':
    #     ata = {'All Data': 'Delete'}
    #     foodDailyData.objects.all().delete()
    # return JsonResponse(ata, safe=False)
    return JsonResponse({'Message': 'Kindly login first'}, safe=False)
