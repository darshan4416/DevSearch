from django.forms import ModelForm
from django.forms.models import ModelChoiceField
from .models import Project
from django import forms

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title','featured_image','description','source_link',
        'demo_link','tags'
        ]
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):

        super(ProjectForm,self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class':'input'})
        self.fields['description'].widget.attrs.update({'class':'input'})
        self.fields['source_link'].widget.attrs.update({'class':'input'})
        self.fields['demo_link'].widget.attrs.update({'class':'input'})

