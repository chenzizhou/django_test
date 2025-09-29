from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    # django2.0以上版本使用以下方式定义
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("MiddlewareA: Before view")
        response = self.get_response(request)
        print("MiddlewareA: After view")
        return response

    # django2.0以下版本使用以下方式定义
    def process_request(self, request):
        # 在请求到达视图之前执行的代码
        print("Request received at", request.path)

    def process_response(self, request, response):
        # 在视图生成响应之后执行的代码
        print("Response sent with status", response.status_code)
        return response


class MyMiddlwareExp1(MiddlewareMixin):
    def process_exception(self, request, exception):
        print("Exception occurred:", exception)
