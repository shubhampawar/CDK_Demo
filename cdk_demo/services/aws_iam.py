from aws_cdk import (
    aws_iam as _iam
)


def create_lambda_role(stack):
    lambda_role = _iam.Role(scope=stack, id="demo_lambda_role",
                            assumed_by=_iam.ServicePrincipal(
                                "lambda.amazonaws.com"),
                            role_name="demo_lambda_role")
    return lambda_role


def lambda_policy_statements():
    statement = _iam.PolicyStatement(resources=["*"],
                                     actions=["dynamodb:PutItem",
                                              "logs:CreateLogGroup",
                                              "logs:CreateLogStream",
                                              "logs:PutLogEvents"]
                                     )
    return statement


def create_lambda_managed_policy(stack):
    print(lambda_policy_statements())
    # return _iam.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess')
    policy = _iam.Policy(stack,
                         id="demo_lambda_policy",
                         policy_name="demo_lambda_policy",
                         statements=[lambda_policy_statements()])
    return policy
