import re

from crispy_forms.layout import Submit
from django import forms
from .models import NewsLetterUser, NewsLetter
from crispy_forms.helper import FormHelper


class NewsLetterUserSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_show_labels = False
    helper.add_input(Submit('save', 'Submit', css_class='btn-default'))

    class Meta:
        model = NewsLetterUser
        fields = ['email']


        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email


class NewsLetterCreationForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_show_labels = True
    helper.add_input(Submit('save', 'Submit', css_class='btn-default'))

    class Meta:
        model = NewsLetter
        fields = ['subject', 'content', 'email', 'status']

        def clean_price(self):
            subject = self.cleaned_data['subject']
            subject = re.sub('[.]', '', subject)
            subject = re.sub('[,]', '.', subject)
            return subject

        # def clean_email(self):
        #     email = self.cleaned_data.get('email')
        #
        #     return email
        #
        # def clean_subject(self):
        #     subject = self.cleaned_data.get('subject')
        #
        #     return subject
        #
        # def clean_content(self):
        #     content = self.cleaned_data.get('content')
        #
        #     return content
        #
        # def clean_status(self):
        #     status = self.cleaned_data.get('status')
        #
        #     return status













