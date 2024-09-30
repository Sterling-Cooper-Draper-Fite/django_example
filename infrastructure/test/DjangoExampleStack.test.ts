import * as cdk from "aws-cdk-lib";
import { Template } from "aws-cdk-lib/assertions";
import * as DjangoExampleStack from "../lib/DjangoExampleStack";

describe("DjangoExampleStack", () => {
  const app = new cdk.App();
  const stack = new DjangoExampleStack.DjangoExampleStack(app, "MyTestStack");
  const template = Template.fromStack(stack);

  it("has a media bucket", () => {
    template.hasResourceProperties("AWS::S3::Bucket", {});
  });

  it("has a job queue", () => {
    template.hasResourceProperties("AWS::SQS::Queue", {});
  });

  it("has a server task role", () => {
    template.hasResourceProperties("AWS::IAM::Role", {});
  });

  it("has a worker task role", () => {
    template.hasResourceProperties("AWS::IAM::Role", {});
  });
});
