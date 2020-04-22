#!/usr/bin/env python3

from aws_cdk import core

from hello_cdk.hello_cdk_stack import HelloCdkStack


app = core.App()
HelloCdkStack(app, "hello-cdk", env={'region': 'us-west-2'})

app.synth()
