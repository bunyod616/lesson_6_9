from django.shortcuts import render
from django.views import View


class HomePage(View):
    @staticmethod
    def get(request):
        return render(request, "university.html")