from django.urls import path
from my_app.views import (home, greeting, contact, licenses, contributing, features, usage, installation, form_submitted,
						  contact_input)

urlpatterns = [
	path('home/', home, name='home'),
	path('', home, name='home'),
	path('greeting/', greeting, name='greeting'),
	path('contact/', contact, name='contact'),
	path('licenses/', licenses, name='licenses'),
	path('contributing/', contributing, name='contributing'),
	path('features/', features, name='features'),
	path('usage/', usage, name='usage'),
	path('installation/', installation, name='installation'),
	path('form-submitted/', form_submitted, name='form-submitted'),
	path('contact_input/', contact_input, name='contact_input')
]
