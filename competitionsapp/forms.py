from django.forms import ModelForm,HiddenInput
from competitionsapp.models import Answer

class AnswerForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Answer
        fields= ['value','exercise']
        widgets = {
            'exercise': HiddenInput
        }

