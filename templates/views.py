from django.shortcuts import render

def generate_table(request):
    if request.method == 'POST':
        row_count = int(request.POST.get('row_count'))
        return render(request, 'shopping_list.html', {'result': row_count})
    return render(request, 'shopping_list.html')