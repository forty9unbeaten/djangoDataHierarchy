from django.shortcuts import render
from django.views.generic.base import View
from filesAndFolders.models import FileFolder

# Create your views here.


class Hompage(View):

    def get(self, request):
        instances = FileFolder.objects.all()
        return render(
            request,
            'index.html',
            {
                'nodes': instances
            }
        )
