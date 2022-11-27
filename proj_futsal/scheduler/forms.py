from django import forms
from .models import Player


class RegisterPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['event', 'name', 'player_status', 'attendance_status', 'comment',] 

class EditPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['event', 'name', 'player_status', 'attendance_status', 'comment',]  
    