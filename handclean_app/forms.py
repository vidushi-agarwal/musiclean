from django import forms
from .models import LyricModel,ReviewModel

#edit crispy tags
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML,Layout, Fieldset, Submit, ButtonHolder
from crispy_forms.bootstrap import *

# This is a model form- this is created using model
class LyricModelForm(forms.ModelForm):
    class Meta:
        model = LyricModel
        fields = {'song_title', 'artist'}
    def __init__(self, *args, **kwargs):
        super(LyricModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Wash your hands',HTML("""
            <p>Please type your song's title and singer name, and click Create Poster. <strong>Above, in the navbar we have selected most popular songs searched.</strong> Check them for quick access.</p>
        """),'song_title', 'artist'
            ),
            ButtonHolder(
                Submit('submit', 'Create Poster', css_class='btn btn-primary btn-block')
            )
        )

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = {'jingle', 'myreview', 'picture'}
        ordering = ('-date_posted')
    def __init__(self, *args, **kwargs):
        super(ReviewModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Your review is important.',HTML("""
            <p>Please write your 'go to jingle', you created using Musiclean,a small review and your musiclean best poster.</p>"""),'jingle','myreview', 'picture'
            ),
            ButtonHolder(
                Submit('submit', 'Happy to help', css_class='btn btn-primary btn-block')
            )
        )

