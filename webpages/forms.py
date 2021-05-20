from django.forms import TextInput, EmailInput, Textarea, NumberInput
from django import forms
from .models import Contact, CareerForm
from django.utils.translation import gettext_lazy as _
from .models import CareerForm
from crispy_forms.bootstrap import InlineField


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'subject': TextInput(attrs={'placeholder': 'Subject'}),
            'message': Textarea(attrs={'placeholder': 'Message'}),
        }
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]


class CaForm(forms.ModelForm):
    class Meta:
        model = CareerForm
        fields = (
            'first_Name',
            'last_Name',
            'email',
            'phone_number',
            'address',
            'state',
            'city',
            'pin_code',
            'position',
            'about',
            'qualify',
            'employment_Type'
        )

        STATE_CHOICES = [
            ('', 'Select a state'),
            # First one is the value of select option and second is the displayed value in option
            ('Assam', 'Assam'),
            ('Arunachal', 'Arunachal'),
            ('Nagaland', 'Nagaland'),
            ('Manipur', 'Manipur'),
            ('Mizoram', 'Mizoram'),
            ('Meghalaya', 'Meghalaya'),
            ('Tripura', 'Tripura'),
        ]

        EMPLOYMENT_CHOICES = [
            ('', 'Select employment type'),
            ('Part Time', 'Part Time'),
            ('Full Time', 'Full Time')
        ]
        widgets = {
            'first_Name': TextInput(attrs={'placeholder': 'First Name'}),
            'last_Name': TextInput(attrs={'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': NumberInput(attrs={'placeholder': 'Eg :9xxxxxxxxx 10 digits'}),
            'address': Textarea(attrs={'placeholder': 'Eg: Vill , pin ,state'}),
            'state': forms.Select(choices=STATE_CHOICES, attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'placeholder': 'City'}),
            'pin_code': NumberInput(attrs={'placeholder': 'Pin'}),
            'position': TextInput(attrs={'placeholder': ''}),
            'about': Textarea(attrs={'placeholder': 'Eg: Your work,How will you tackle problems if given... etc'}),
            'qualify': Textarea(attrs={'placeholder': ''}),
            'employment_Type': forms.Select(choices=EMPLOYMENT_CHOICES, attrs={'class': 'form-control'}),
        }

        labels = {
            'about': _('Tell me little bit about yourself'),
            'qualify': _('Why should we hire you for this position?')
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'phone_number': {
                'max_length': _("This writer's name is too long."),
            },
        }
