from django.shortcuts import render
from django.views.generic import TemplateView , DetailView, CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from lectures.models import Lecture, Inquiry
from lectures.forms import InquiryForm
# Create your views here.

context_settings = {
    'title':'IM-skolen',
    'headline':'Velkommen til IM-skolen!',
    'headline_over':'Velkommen til',
    'introduksjon':'Her finner du alt du trenger for å lære om IT og multimedia',
    'author':'Kuben Yrkesarena',
}

def home(request):
    active_tab = 'home'
    lectures = Lecture.objects.all()

    context = context_settings.copy()
    
    context['lectures'] = lectures
    context['view'] = {}
    context['view'].update({'active_tab' : active_tab})

    return render(request, 'lectures/home.html', context)

class LectureDetailView(DetailView):
    model = Lecture


class InquiryCreateView(CreateView):
    active_tab = 'feedback'
    success_url = reverse_lazy('feedback_success')
    #model = Inquiry
    template_name = 'lectures/inquiry_form.html'
    form_class = InquiryForm
    def get_context_data(self,**kwargs):
        context = super(InquiryCreateView, self).get_context_data(**kwargs)
        context.update(context_settings)
        return context

class InquirySuccessView (TemplateView):
    active_tab = 'feedback'
    template_name = 'lectures/inquiry_success.html'

    def get_context_data(self,**kwargs):
        context = super(InquirySuccessView, self).get_context_data(**kwargs)
        #context.update({
        #    'navn':'Arvid',
        #    })
        return context