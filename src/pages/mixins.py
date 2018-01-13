from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    def form_valid(self, form):
        # if the user is not logged they cannot make changes. Here we can add a another validation to check 
        # if the user has enough score to add a new Candidate

        if self.request.user.is_authenticated():
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
             form.instance.userId = self.request.user
             return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList("User must be Logged in to continue")
            return self.form_invalid(form)


# there is a problem with this mixin need to figure out what 
class UserOwnerMixin(object): 
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)

        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList("This user is not allowed to update must loggin ")
            return self.form_invalid(form)