from django import forms

from single_match.models import Match


class MatchResultForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['result_local_team', 'result_visiting_team']


class NewMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['local_team', 'visiting_team', 'result_local_team', 'result_visiting_team',
                  'img_local_team', 'img_visiting_team']
