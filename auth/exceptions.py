from rest_framework.exceptions import APIException


class UsernameExit(APIException):
    status_code = 400
    default_detail = 'Username da ton tai.'
    default_code = '8001'
