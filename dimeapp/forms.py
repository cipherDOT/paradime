

# ---------------------------------------------------imports------------------------------------------------------------ #

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer

# --------------------------------------------------Question Form---------------------------------------------------------- #


class QuestionForm(forms.ModelForm):
    # it HAS an user field, but as a hidden field
    user = forms.HiddenInput()

    heading = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Type your question here', 'autocomplete': 'off'}))

    body = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Type your content here', 'autocomplete': 'off'}))

    class Meta:
        model = Question
        # we input the user in the views file, and don't
        # include the user field in the form
        fields = ['heading', 'body']

# ---------------------------------------------------Answer Form---------------------------------------------------------- #

class AnswerForm(forms.ModelForm):
    # it HAS an user field, but as a hidden field
    user = forms.HiddenInput()
    question = forms.HiddenInput()

    body = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Type your content here', 'autocomplete': 'off'}))

    class Meta:
        model = Answer
        # we input the user in the views file, and don't
        # include the user field in the form
        fields = ['body']

# ----------------------------------------------------User form-------------------------------------------------------------- #

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ------------------------------------------------------------------------------------------------------------------------- #
