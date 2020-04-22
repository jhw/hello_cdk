from aws_cdk import (core,
                     aws_lambda as _lambda,
                     aws_apigateway as _apigw)

class HelloCdkStack(core.Stack):

    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        handler=_lambda.Function(self, 'Hello Lambda',
                                 handler='lambda-handler.handler',
                                 runtime=_lambda.Runtime.PYTHON_3_7,
                                 code=_lambda.Code.asset('lambda'))
        api=_apigw.LambdaRestApi(self, "Hello API Gateway",
                                 handler=handler)
        api.root.add_method("GET")
        api.root.add_method("POST")

if __name__=="__main__":
    pass

        
