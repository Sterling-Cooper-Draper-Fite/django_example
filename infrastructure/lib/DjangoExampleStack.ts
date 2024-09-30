import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as sqs from "aws-cdk-lib/aws-sqs";
import * as iam from "aws-cdk-lib/aws-iam";

export class DjangoExampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    /**
     * Resources
     */

    const mediaBucket = new s3.Bucket(this, "MediaBucket", {});

    const jobQueue = new sqs.Queue(this, "JobQueue", {});

    const serverTaskRole = new iam.Role(this, "ServerTaskRole", {
      assumedBy: new iam.CompositePrincipal(
        new iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
        new iam.AccountPrincipal(cdk.Aws.ACCOUNT_ID)
      ),
    });

    const workerTaskRole = new iam.Role(this, "WorkerTaskRole", {
      assumedBy: new iam.CompositePrincipal(
        new iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
        new iam.AccountPrincipal(cdk.Aws.ACCOUNT_ID)
      ),
    });

    /**
     * Permissions
     */

    // server can r/w to the media bucket and send messages to job queue
    mediaBucket.grantReadWrite(serverTaskRole);
    jobQueue.grantSendMessages(serverTaskRole);

    // worker can receive messages from job queue and r/w to the media bucket
    jobQueue.grantConsumeMessages(workerTaskRole);
    mediaBucket.grantReadWrite(workerTaskRole);

    workerTaskRole.addToPolicy(
      new iam.PolicyStatement({
        actions: ["sqs:ListQueues"],
        resources: ["*"],
      })
    );

    /**
     * Outputs
     */

    new cdk.CfnOutput(this, "MediaBucketName", {
      value: mediaBucket.bucketName,
    });

    new cdk.CfnOutput(this, "JobQueueName", {
      value: jobQueue.queueName,
    });

    new cdk.CfnOutput(this, "JobQueueUrl", {
      value: jobQueue.queueUrl,
    });

    new cdk.CfnOutput(this, "ServerTaskRoleName", {
      value: serverTaskRole.roleName,
    });

    new cdk.CfnOutput(this, "WorkerTaskRoleName", {
      value: workerTaskRole.roleName,
    });
  }
}
