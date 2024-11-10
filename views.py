from django.shortcuts import render
from .models import Sales, Inventory, Expenses
from django.shortcuts import render
from .models import Sales  
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render
from .models import SalesData
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from .models import SalesData
import mplcursors


def dashboard_view(request):
    sales_data = SalesData.objects.all()
    months = [record.month for record in sales_data]
    sales = [record.sales for record in sales_data]

    return render(request, 'dashboard/index.html', {
        'months': months,
        'sales': sales,
        'sales_data': sales_data
    })

def update_sales(request):
    if request.method == "POST":
        record_id = request.POST.get("id")
        new_value = request.POST.get("sales_value")
        
       
        sales_record = Sales.objects.get(id=record_id)
        sales_record.sales = new_value
        sales_record.save()
        
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "failed"})

from django.shortcuts import render
from .models import Sales  

from django.http import JsonResponse

def sales_data_api(request):
    sales_data = SalesData.objects.all()
    months = [record.month for record in sales_data]
    sales = [record.sales for record in sales_data]
    return JsonResponse({'months': months, 'sales': sales})

def sales_histogram(request):

    import matplotlib.pyplot as plt
    import matplotlib.ticker as mtick

# Your plotting code here

    plt.gca().get_yaxis().set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))
    
    sales_data = list(SalesData.objects.all().values('month', 'sales'))

    
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    
    sorted_sales_data = sorted(sales_data, key=lambda x: month_order.index(x['month']))

    
    months = [item['month'] for item in sorted_sales_data]
    sales = [item['sales'] for item in sorted_sales_data]

    
    fig, ax = plt.subplots(figsize=(10, 6))


    ax.bar(months, sales, color='gold', edgecolor='none')
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('₹', fontsize=16,)
    


    plt.xticks(rotation=45)


    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    plt.gca().get_yaxis().set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))


    plt.tight_layout()


    plt.show()

    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    
    return HttpResponse(buffer, content_type='image/png')
