# CDK_Demo
AWS CDK DEMO

![N|Solid](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2021/01/15/cdk-logo6-1260x476.png)


The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages.

## Lambda-S3-Trigger
When files are uploaded in S3 bucket it triggers a lambda function and file metadata(filename,bucketname) is written in dynamodb.

<p align="center">
  <img src="https://github.com/shubhampawar/CDK_Demo/blob/main/cdk-demo.png" />
</p>

## Build and Deploy

The `cdk.template.json` file tells the CDK Toolkit how to execute your app.


### Python setup

This project is set up like a standard Python project. The initialization process also creates a virtualenv within this
project, stored under the `.env` directory. To create the virtualenv it assumes that there is a `python3` (or `python`
for Windows) executable in your path with access to the `venv` package. If for any reason the automatic creation of the
virtualenv fails, you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

### CDK Deploy

With specific profile,
```
$ cdk deploy --profile test
```

Using the default profile

```
$ cdk deploy
```
