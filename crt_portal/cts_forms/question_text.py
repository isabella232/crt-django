from django.utils.translation import gettext_lazy as _

# contact
CONTACT_QUESTIONS = {
    'contact_title': _('Contact information'),
    'contact_name_title': _('Your name'),
    'contact_first_name': _('First name'),
    'contact_last_name': _('Last name'),
    'contact_info_tite': _('Contact information'),
    'contact_email': _('Email address'),
    'contact_phone': _('Phone number'),
}
SERVICEMEMBER_QUESTION = _('Are you now or have ever been an active duty service member?')
# primary concern
PRIMARY_REASON_QUESTION = _('What is your primary reason for contacting the Civil Rights Division?')
# hatecrime
HATECRIME_TITLE = _('Hate crimes and human trafficking')
HATECRIME_QUESTION = _('Please select if any apply to your concern')

# Location
LOCATION_QUESTIONS = {
    'location_title': _('Where did this happen?'),
    'location_name': _('Location name'),
    'location_address_line_1': _('Street address 1'),
    'location_address_line_2': _('Street address 2'),
    'location_city_town': _('City/town'),
    'location_state': _('State'),
}
ELECTION_QUESTION = _('What kind of election or voting activity was this related to?')
WORKPLACE_QUESTIONS = {
    'public_or_private_employer': _('Was this a public or private employer?'),
    'employer_size': _('How large is this employer?'),
}
PUBLIC_QUESTION = _('Please choose the location that best describes your situation')
POLICE_QUESTIONS = {
    'inside_correctional_facility': _('Where did this take place?'),
    'correctional_facility_type': _('What type of prison or correctional facility?')
}
EDUCATION_QUESTION = _('Did this happen at a public or a private school, educational program or activity?')

# Personal characteristics
PROTECTED_CLASS_QUESTION = _('Do you believe any of these personal characteristics influenced why you were treated this way?')

# Date
DATE_QUESTIONS ={
    'date_title': _('When did this happen?'),
    'last_incident_month': _('Month'),
    'last_incident_day': _('Day'),
    'last_incident_year': _('Year'),
}

# Personal description
SUMMARY_QUESTION = _('Tell us what happened')
