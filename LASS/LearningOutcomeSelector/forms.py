#Learning query form

from django import forms

class LearningQueryForm(forms.Form):
    learningquery_text=forms.CharField(label='Type in your learning outcome', max_length=100)
