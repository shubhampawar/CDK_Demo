from aws_cdk import (
    aws_s3 as _s3,
)
from constructs import Construct


def create_s3_bucket(stack):

    return _s3.Bucket(
        stack,
        'demo-s3-bucket-cdk',
        bucket_name='demo-s3-bucket-cdk'
    )
