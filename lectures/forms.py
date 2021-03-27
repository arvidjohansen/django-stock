from django import forms
from lectures.models import Inquiry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Row, Column
from crispy_forms.bootstrap import FormActions

class InquiryForm(forms.ModelForm):
    #extra_field = forms.CharField()
    class Meta():
        model = Inquiry
        fields = ['name', 'email','description']
        widgets = {
            'description':forms.Textarea(attrs={
                'cols':40, 'rows':10
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('email'),
            ),
            Row(
                Column('description')
            ),
            FormActions(
                Submit('send','Send tilbakemelding', css_class='btn-success'),
                #Submit('cancel','Avbryt',css_class='btn-danger'),
            )
        )
        