from django import forms


from .models import Student

class StudentCreateForm(forms.Form):
	First_name		= forms.CharField()
	Last_name		= forms.CharField(required=False)
	Middle_name		= forms.CharField(required=False)
	Gender			= forms.CharField(required=False)
	age				= forms.IntegerField(required=False)

	def clean_name(self):
		First_name = self.cleaned_data.get("First_name")
		if First_name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return First_name

class StudentDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'First_name',
			'Last_name',
			'Middle_name',
			'Gender',
			'age',
			'course',
			'year',
		]