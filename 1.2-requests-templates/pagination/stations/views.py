from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        stations = []
        for row in reader:
            stations.append({'Name': row['Name'],
                             'Street': row['Street'],
                             'District': row['District']})
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(stations, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
