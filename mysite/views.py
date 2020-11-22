from django.shortcuts import render

def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)
