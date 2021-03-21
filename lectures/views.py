from django.shortcuts import render
from django.views.generic import TemplateView 
from django.http import HttpResponse
from lectures.models import Lecture
# Create your views here.

def home(request):
    lectures = Lecture.objects.all()

    context = {
        'title':'IKT-skolen v2',
        'headline':'Velkommen til IKT-skolen!',
        'introduksjon':'Velg en modul og sett i gang!',
        'author':'Kuben Yrkesarena',
    }
    
    context['lectures'] = lectures

    return render(request, 'lectures/home.html', context)



class SimpleView (TemplateView):

    template_name = 'Simple.html'

    def get_context_data(self,**kwargs):
        context = super(SimpleView, self).get_context_data(**kwargs)
        context.update({
            'navn':'Arvid',
            })
        return contex