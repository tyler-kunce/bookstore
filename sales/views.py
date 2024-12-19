from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale
from .utils import get_bookname_from_id, get_chart
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None
    chart = None

    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')

        qs = Sale.objects.filter(book__name=book_title)
        if qs:
            sales_df = pd.DataFrame(qs.values())
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
            chart = get_chart(chart_type, sales_df, labels = sales_df['date_created'].values)
            sales_df = sales_df.to_html()

        """print(book_title, chart_type)

        print('Exploring querysets:')
        print('Case 1: Output of Sale.objects.all()')
        qs = Sale.objects.all()
        print(qs)

        print('Case 2: Output of Sale.objects.filter(book_name = book_title)')
        qs = Sale.objects.filter(book__name=book_title)

        print('Case 3: Output of qs.values')
        print(qs.values())

        print('Case 4: Output of qs.values_list()')
        print(qs.values_list())

        print('Case 5: Output of Sale.objects.get(id=1)')
        obj = Sale.objects.get(id=1)
        print(obj)"""

    context={
        'form': form,
        'sales_df': sales_df,
        'chart': chart,
    }

    return render(request, 'sales/records.html', context)

