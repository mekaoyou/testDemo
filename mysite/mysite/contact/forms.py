''' this is contact form '''
from django import forms

class ClassName(forms.Form):
    """docstring for ClassName"""
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
		