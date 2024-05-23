from rest_framework.authentication import SessionAuthentication


class CsrfExemptAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        print("Here we go!")
        return