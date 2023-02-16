from django import forms
from .models import *

class AddContentPlanForm(forms.Form):
    
    CHOICES=[('carusel','Karusel'),
             ('simple','Simple'),
             ('motion','Motion'),
             ('video','Video'),
             ('reels','Reels')]

    TELEGRAM_CHOICES=[('carusel','Karusel'),
             ('simple','Simple'),
             ('motion','Motion'),
             ('video','Video')]
    

    project = forms.ModelChoiceField(
        widget=forms.Select(),
        required=False,
        queryset=Project.objects.all())

    date = forms.DateField(
        widget = forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
        )
    
    i_post_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        required=False)
    
    i_history = forms.BooleanField(
        required=False
    )

    t_post_type = forms.ChoiceField(
        choices=TELEGRAM_CHOICES, 
        widget=forms.RadioSelect,
        required=False)
    
    f_post_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        required=False
    )
    f_history = forms.BooleanField(
        required=False
    )

    y_post_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        required=False
    )
    y_history = forms.BooleanField(
        required=False
    )

    # class Meta:
    #     model = ContentPlan
    #     fields = ['project', 'post_type', 'date', 'history']
        
class AddPostForm(forms.Form):
    
    CHOICES=[('carusel','Karusel'),
             ('simple','Simple'),
             ('motion','Motion'),
             ('video','Video'),
             ('reels','Reels')]

    TELEGRAM_CHOICES=[('carusel','Karusel'),
             ('simple','Simple'),
             ('motion','Motion'),
             ('video','Video')]
    

    project = forms.ModelChoiceField(
        widget=forms.Select(),
        # required=False,
        queryset=Project.objects.all())

    date = forms.DateField(
        widget = forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
        )
    
    i_post_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        required=False)
    
    i_history = forms.BooleanField(
        required=False
    )

    t_post_type = forms.ChoiceField(
        choices=TELEGRAM_CHOICES, 
        widget=forms.RadioSelect,
        required=False)
    
    f_post_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        required=False
    )
    f_history = forms.BooleanField(
        required=False
    )

    y_post_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        required=False
    )
    y_history = forms.BooleanField(
        required=False
    )
