from django.shortcuts import render
from django.http import HttpResponseNotAllowed

def generate_table(request):
    if request.method == 'POST':
        row_count = int(request.POST.get('row_count'))
        return render(request, 'shopping_list.html', {'result': row_count})
    return HttpResponseNotAllowed(['POST'])  # Explicitly show allowed methods