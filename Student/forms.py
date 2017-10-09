from django import forms


from .models import Student

class StudentCreateForm(forms.Form):
	FirstName		= forms.CharField()
	LastName		= forms.CharField(required=False)
	MiddleName		= forms.CharField(required=False)
	Gender			= forms.CharField(required=False)
	age				= forms.IntegerField(required=False)
	birthday		= forms.DateTimeField()

	def clean_name(self):
		FirstName = self.cleaned_data.get("FirstName")
		if FirstName == "Hello":
			raise forms.ValidationError("Not a valid name")
		return FirstName

class StudentDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'FirstName',
			'LastName',
			'MiddleName',
			'Gender',
			'age',
			'birthday',
			'course',
		]