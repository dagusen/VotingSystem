from django import forms


from .models import Course

class CourseCreateForm(forms.Form):
	course_name		= forms.CharField()
	description		= forms.CharField()
	

	def clean_name(self):
		course_name = self.cleaned_data.get("course_name")
		if course_name == "Hello":
			raise forms.ValidationError("Not a valid course name")
		return course_name

class CourseDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			'course_name',
			'description',
			'department',
		]