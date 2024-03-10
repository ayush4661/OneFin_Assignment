class CountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request, *args, **kwargs):
        request.count_middleware = self
        self.count += 1
        response = self.get_response(request)
        return response

    def get_request_count(self):
        return self.count
    
    def reset_request_count(self):
        self.count = 0
