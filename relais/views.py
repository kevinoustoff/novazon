from django.shortcuts import render
from django.views import View
from .models import PointRelais
from .forms import PointRelaisForm
from django.shortcuts import redirect
from django.urls import reverse

class PointRelaisView(View):
    form_class = PointRelaisForm
    template_name = 'relais/point_relais.html'

    def get(self, request):
        form = self.form_class()
        error_message = request.GET.get('error_message', None)
        return render(request, self.template_name, {'form': form, 'error_message': error_message})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            point_relais = form.save()
            return render(request, 'relais/success.html')
        else:
            print(form.errors)
            error_message = "Le formulaire contient des erreurs."
            return redirect(reverse('point_relais') + f'?error_message={error_message}')


class AllRelaisView(View):
    def get(self, request):
        relais = PointRelais.objects.all()
        return render(request, 'relais/all_relais.html', {'relais': relais})

class MapView(View):
    def get(self, request):
        return render(request, 'relais/map.html')
