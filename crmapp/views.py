from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'landing.html')



'''def dashboard(request):
   dashboard = request.GET.get('dashboard',' ').split(',')
   return render(request, 'base.html',{'dashboard':dashboard})
def archieve(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'archieve.html', {'item_ids': item_ids})'''



def page1(request):
    item_idf = request.GET.get('item_idf',' ').split(',')
    return render(request, 'base.html',{'item_idf':item_idf})

def page2(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'archieve.html', {'item_ids': item_ids})