from django import forms

from .models import Candidate

class CandidateModelForm(forms.ModelForm):
    # id_candidate = forms.CharField(help_text="Please enter the category name.")
    # name_candidate = forms.CharField(help_text="Please enter the category name.")
    # summary = forms.CharField(widget=forms.Textarea())
    # descriptions = forms.CharField(widget=forms.Textarea())

    # An inline class to provide additional information on the form.
    # summary = forms.CharField(label='Summary', widget=forms.Textarea)
    # descriptions = forms.CharField(label='Descriptions', widget=forms.Textarea)

    id_candidate = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Candidate ID", 
                            "class": "form-control"}
                    ))
    
    name_candidate = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Candidate Name", 
                            "class": "form-control"}
                    ))

    summary = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Summary", 
                            "class": "form-control"}
                    ))

    descriptions = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Descriptions", 
                            "class": "form-control"}
                    ))
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Candidate
        fields = (
            # 'userId', 
            'id_candidate',  
            'name_candidate', 
            'summary', 
            'descriptions')


# this is a type of validation added for the form 
    # def clean_name_candidate(self, *args, **kwrgs): 
    #     name_candidate = self.cleaned_data.get("name_candidate")
    #     if name_candidate == "abc":
    #         raise forms.ValidationError("Cannot be testfield ")
    #     return name_candidate




# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Page

#         # What fields do we want to include in our form?
#         # This way we don't need every field in the model present.
#         # Some fields may allow NULL values, so we may not want to include them...
#         # Here, we are hiding the foreign key.
#         # we can either exclude the category field from the form,
#         exclude = ('category',)
#         #or specify the fields to include (i.e. not include the category field)
#         #fields = ('title', 'url', 'views') 