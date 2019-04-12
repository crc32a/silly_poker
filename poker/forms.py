from django import forms

class idForm(forms.Form):
    def __init__(self,*args,**kw):
        forms.Form.__init__(self,*args,**kw)
        form_name = forms.CharField(max_length=32,
                                    required=True,
                                    widget=forms.HiddenInput,
                                    initial=self.__class__.__name__
                                   )
        self.fields["form_name"] = form_name


class UserForm(idForm):
    name = forms.CharField(label="user name", max_length=32)
    project = forms.CharField(label="project name", max_length=32)
