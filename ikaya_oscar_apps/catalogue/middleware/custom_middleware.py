class VariableSetMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        request.session['currency_code'] = 'INR'
        request.session['currency_factor'] ='1.00'