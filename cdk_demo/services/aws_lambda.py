from aws_cdk import (
    aws_lambda as _lambda
)

def create_lambda_function(stack,role):
        # create lambda function
        function = _lambda.Function(stack, "demo_lambda",
                                    function_name="demo_lambda",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda_handler.handler",role=role,
                                    code=_lambda.Code.from_asset(".\cdk_demo\lambda_handler"))

        return function

