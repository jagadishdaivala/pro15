from django.shortcuts import render

# Create your views here.
def insta(request,id):
    if id==1:
        return render(request,'h1.html')
    elif id==2:
        return render(request,'h2.html')
    return render(request,'home.html')