from aws_cdk import (
    aws_dynamodb as _dynamodb
)


def create_table(stack):
    demo_table = _dynamodb.Table(stack, "Demo-Table", 
                                 table_name="Demo-Table",
                                 partition_key=_dynamodb.Attribute(
                                 name="id",
                                 type=_dynamodb.AttributeType.STRING))
    return demo_table
