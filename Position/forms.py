from django import forms


from .models import Position

class PositionDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Position
		fields = [
			'position_name',
		]