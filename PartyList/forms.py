from django import forms


from .models import PartyList

class PartyListDetailCreateForm(forms.ModelForm):
	class Meta:
		model = PartyList
		fields = [
			'partylist_name',
		]