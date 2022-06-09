from constructs import Construct
from .services import aws_lambda as _lambda
from .services import aws_s3 as _s3
from .services import aws_iam as _iam
from .services import aws_dynamodb as _dynamodb
from aws_cdk import (
    Stack,
    aws_s3_notifications,
    aws_s3 as s3
)


class CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # lambda_Role
        lambda_role = _iam.create_lambda_role(self)

        # create lambda function
        lambda_function = _lambda.create_lambda_function(
            self, role=lambda_role)

        # create s3 bucket
        s3_bucket = _s3.create_s3_bucket(self)

        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(lambda_function)

        # assign notification for the s3 event type
        s3_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED_PUT, notification)

        # create DynamoDb Table
        table = _dynamodb.create_table(self)

        # add managed policy to lambda execution role
        lambda_role.attach_inline_policy(
            (_iam.create_lambda_managed_policy(self)))
