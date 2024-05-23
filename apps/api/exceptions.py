from rest_framework.exceptions import APIException


class DBLockedException(APIException):
    status_code = 400
    default_detail = 'Database locked, cannot create service ticket or indirect hours in past dates!'
    default_code = 'DB_LOCKED'

    def get_full_details(self):
        print('get_full_details()')
        return self.default_detail

    def get_codes(self):
        print('get_codes()')
        return self.status_code
