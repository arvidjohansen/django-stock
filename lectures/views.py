from django.shortcuts import render
from django.views.generic import TemplateView , DetailView, CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from lectures.models import Lecture, Inquiry

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

class LectureDetailView(DetailView):
    model = Lecture


class InquiryCreateView(CreateView):
    success_url = reverse_lazy('feedback_success')
    model = Inquiry
    fields = ['name','email', 'description']

class InquirySuccessView (TemplateView):

    template_name = 'lectures/inquiry_success.html'

    def get_context_data(self,**kwargs):
        context = super(InquirySuccessView, self).get_context_data(**kwargs)
        #context.update({
        #    'navn':'Arvid',
        #    })
        return context