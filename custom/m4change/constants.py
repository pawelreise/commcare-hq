
M4CHANGE_DOMAINS = ('m4change', 'test-pathfinder')

M4CHANGE_LIVE_FOLLOW_UP_FORM_XMLNS = 'http://openrosa.org/formdesigner/56189892f7d8b3087d98b7599e0574f8e2031da6'
M4CHANGE_LIVE_BOOKING_FORM_XMLNS = 'http://openrosa.org/formdesigner/B4FD1933-C925-4FD3-A17A-9FB4A8727BA7'
M4CHANGE_LIVE_IMMUNIZATION_FORM_XMLNS = 'http://openrosa.org/formdesigner/58FB3D54-354B-4216-A4D1-47B5160965CE'

M4CHANGE2_FOLLOW_UP_FORM_XMLNS = 'http://openrosa.org/formdesigner/56189892f7d8b3087d98b7599e0574f8e2031da6'
M4CHANGE2_BOOKING_FORM_XMLNS = 'http://openrosa.org/formdesigner/b9d9f943e63d5de8a6ea3a40a314bc5dafd2ef50'
M4CHANGE2_BOOKED_DELIVERY_FORM_XMLNS = 'http://openrosa.org/formdesigner/e951a60e291a2867a95d206441d876fbf204949d'
M4CHANGE2_UNBOOKED_DELIVERY_FORM_XMLNS = 'http://openrosa.org/formdesigner/3b48e25bab6e7bd0967336b81b1e008c9ab5e6f9'

M4CHANGE2R_FOLLOW_UP_FORM_XMLNS = 'http://openrosa.org/formdesigner/a336db2836b54b2c301a79ef531d30d00618577c'
M4CHANGE2R_BOOKED_DELIVERY_FORM_XMLNS = 'http://openrosa.org/formdesigner/dffcbe5c125f3b0c6859265b0f08abec9f4d23f0'

MERGE_LIVE_FOLLOW_UP_FORM_XMLNS = 'http://openrosa.org/formdesigner/56189892f7d8b3087d98b7599e0574f8e2031da6'
MERGE_LIVE_BOOKING_FORM_XMLNS = 'http://openrosa.org/formdesigner/b9d9f943e63d5de8a6ea3a40a314bc5dafd2ef50'
MERGE_LIVE_IMMUNIZATION_FORM_XMLNS = 'http://openrosa.org/formdesigner/58FB3D54-354B-4216-A4D1-47B5160965CE'

PNC_CHILD_IMMUNIZATION_FORM_XMLNS = 'http://openrosa.org/formdesigner/4dc380eadd46dfa9915f374934af30b5596edc92'
REG_HOME_DELIVERED_INFANT_FORM_XMLNS = 'http://openrosa.org/formdesigner/7fea595525157a9edd81b731d6b10f0b65a44ae2'

BOOKING_FORMS = [
    M4CHANGE_LIVE_BOOKING_FORM_XMLNS,
    M4CHANGE2_BOOKING_FORM_XMLNS,
    MERGE_LIVE_BOOKING_FORM_XMLNS
]

FOLLOW_UP_FORMS = [
    M4CHANGE_LIVE_FOLLOW_UP_FORM_XMLNS,
    M4CHANGE2_FOLLOW_UP_FORM_XMLNS,
    M4CHANGE2R_FOLLOW_UP_FORM_XMLNS,
    MERGE_LIVE_FOLLOW_UP_FORM_XMLNS
]

IMMUNIZATION_FORMS = [
    PNC_CHILD_IMMUNIZATION_FORM_XMLNS,
    M4CHANGE_LIVE_IMMUNIZATION_FORM_XMLNS,
    MERGE_LIVE_IMMUNIZATION_FORM_XMLNS
]

BOOKED_DELIVERY_FORMS = [
    M4CHANGE2_BOOKED_DELIVERY_FORM_XMLNS,
    M4CHANGE2R_BOOKED_DELIVERY_FORM_XMLNS
]

UNBOOKED_DELIVERY_FORMS = [
    M4CHANGE2_UNBOOKED_DELIVERY_FORM_XMLNS,
]

BOOKED_AND_UNBOOKED_DELIVERY_FORMS = BOOKED_DELIVERY_FORMS + UNBOOKED_DELIVERY_FORMS
BOOKING_AND_FOLLOW_UP_FORMS = BOOKING_FORMS + FOLLOW_UP_FORMS
PNC_CHILD_IMMUNIZATION_AND_REG_HOME_DELIVERED_FORMS = PNC_CHILD_IMMUNIZATION_FORM_XMLNS +\
                                                      REG_HOME_DELIVERED_INFANT_FORM_XMLNS
