# CDK_Demo
AWS CDK DEMO

![N|Solid](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2021/01/15/cdk-logo6-1260x476.png)


The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages.

## Lambda-S3-Trigger
When files/objects are uploaded in S3 bucket it triggers a lambda function and files metadata(filename,bucketname) is written to dynamodb table.

<p align="center">
  <img src="https://github.com/shubhampawar/CDK_Demo/blob/main/cdk-demo.png" />
</p>



## AWS CDK Toolkit setup

Install the AWS CDK Toolkit. The toolkit is a command-line utility which allows you to work with CDK apps.
The AWS CDK uses Node.js (>= 10.13.0, except for versions 13.0.0 - 13.6.0). A version in active long-term support (14.x at this writing) is recommended.

Open a terminal session and run the following command:

    $ npm install -g aws-cdk

You can check the toolkit version:
    
    $ cdk --version

    



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
## Configure AWS credentials locally

```
aws configure
```

```
AWS Access Key ID [****************6A4Y]:Required
AWS Secret Access Key [****************1xmv]:Required
Default region name [None]: optional (default is us-east-1)
Default output format [None]:optional (default is text)
```

## Build and Deploy

The `cdk.template.json` file tells the CDK Toolkit how to execute your app.

With specific profile,
```
$ cdk deploy --profile test
```

Using the default profile

```
$ cdk deploy
```
