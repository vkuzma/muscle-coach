# -*- coding: utf-8 -*-
import forms
import calendar

from datetime import date
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from models import Exercise
from forms import AddTrainingForm

MONTH_NAME = ('Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'Septemper', 'Oktober', 'November', 'December')

def config(request):
    return render(request, 'config.html')
    
def add_training(request):
    if request.method == 'POST':
        form = forms.AddTrainingSchemaForm(request.POST)
    else:
        form = forms.AddTrainingSchemaForm()
    return render(request, 'add_training.html', {'form': form, 'exercise_list': Exercise.objects.all()})

@login_required(login_url='/accounts/login/')
def detail(request, year, month, day):
    context = {
        'year': year,
        'month': month,
        'day': day}
    return render(request, 'detail.html', context)
  
@login_required(login_url='/accounts/login/')  
def add(request, year, month, day):
    if request.method == 'POST':
        form = AddTrainingForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = AddTrainingForm()
    return render(request, 'add.html', {'form': form})

@login_required(login_url='/accounts/login/')
def overview_month(request, year, month):
    today = date.today()
    days_in_month = calendar.mdays[int(month)]
    begin_at_moth = date(int(year), int(month), 1)
    row_count = 0
    days_grid = []
    days = []
    for i in range(days_in_month):
        days.append(date(today.year, int(month), i+1))
        row_count += 1
        if row_count > 6:
            days_grid.append(days)
            days = []
            row_count = 0
            
    if len(days):
        while len(days) is not 7:
            days.append('empty')
        days_grid.append(days)
        
    next_year = int(year)
    if int(month) == 12:
        next_year = int(year)+1
    
    last_year = int(year)
    if int(month) == 1:
        last_year = int(year)-1
    
    last_month = valueInRange(int(month)-1, 1, 12)
    next_month = valueInRange(int(month)+1, 1, 12)
        
    context = {
        'today': today, 
        'days_grid': days_grid, 
        'month_name': MONTH_NAME[int(month)-1], 
        'next_month': next_month, 
        'last_month': last_month, 
        'next_year': next_year,
        'last_year': last_year,}
    return render(request, 'overview.html', context)
    
def valueInRange(value, min, max):
    if value > max:
        return min
    elif value < min:
        return max
    return value
    
@login_required(login_url='/accounts/login/')
def overview(request):
    today = date.today()
    return HttpResponseRedirect('%d/%d'% (today.year, today.month,))
    
