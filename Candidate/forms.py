from django import forms


from .models import Candidate

class CandidateDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = [
			'student',
			'position',
			'party_list',
		]