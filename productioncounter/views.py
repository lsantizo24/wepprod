from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render
from . import contador  
from .models import ProductionData
from django.db.models import F



monitor = None


def start_monitor(root_dir, start_time, end_time):
    global monitor
    monitor = contador.CSVMonitor(root_dir, start_time, end_time)
    monitor.start()




def production_counter(request):
    root_dir = '/home/lsantizo/dataResult/'  
    start_time = "7:00"  
    end_time = "23:50"  

    global monitor
    if monitor is None or not monitor.is_alive():
        start_monitor(root_dir, start_time, end_time)

    data, new_count, non_passed_count, station_name,order_number, lot_number = monitor.get_data()  # Call get_data to retrieve data

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data_html = data.to_html(index=False) if not data.empty else '<p>No data available for the current timeframe.</p>'
        response_data = {'data': data_html, 'new_pieces': new_count, 'non_passed_count': non_passed_count}
        return JsonResponse(response_data)
    else:
        context = {
            'data': data.to_html(index=False),  
            'new_pieces': new_count,
            'non_passed_count': non_passed_count,
            'station_name': station_name,
            'order_number': order_number,
            'lot_number': lot_number,
            
        }
        return render(request, 'production/production_count.html', context)

def collect_production_data(root_dir, start_time, end_time):
    global monitor
    if monitor is None or not monitor.is_alive():
        start_monitor(root_dir, start_time, end_time)

    data, new_count, non_passed_count, station_name, order_number, lot_number = monitor.get_data()
    return data, new_count, non_passed_count, station_name, order_number, lot_number


  

def update_production_data(data):
    
    for item in data:
        station_name = item.get('station_name') 
        order_number = item.get('order_number') 
        lot_number = item.get('lot_number')
        production_count = item.get('production_count')  
        hour = item.get('hour')  

      
        existing_record, created = ProductionData.objects.get_or_create(
            line=station_name,
            order=order_number,
            lot_number=lot_number,
            hour=hour,  
        )

        
        if created:
            existing_record.total_production_hour = production_count
            existing_record.total_production = 0  
            existing_record.fail_count = 0  
        else:
            existing_record.total_production_hour = F('total_production_hour') + production_count  
            existing_record.total_production = F('total_production') + production_count  

        existing_record.save()

