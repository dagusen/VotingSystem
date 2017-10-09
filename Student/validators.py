from django.core.exceptions import ValidationError

GENDER = ['Male','Female']

def validate_gender(value):
	cat = value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError("{value} not a valid category") 