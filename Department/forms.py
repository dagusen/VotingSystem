from django import forms


from .models import Department

class DepartmentCreateForm(forms.Form):
	department_name		= forms.CharField()
	department_code		= forms.CharField()
	college_dean 		= forms.CharField()
	

	def clean_name(self):
		department_name = self.cleaned_data.get("department_name")
		if department_name == "Hello":
			raise forms.ValidationError("Not a valid department name")
		return department_name

class DepartmentDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = [
			'department_name',
			'department_code',
			'college_dean',
		]