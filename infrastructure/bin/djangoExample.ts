#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { DjangoExampleStack } from "../lib/DjangoExampleStack";

const app = new cdk.App();

new DjangoExampleStack(app, "DjangoExample-Dev", {
  description: "Resources needed for the Django Example app development",
  tags: {
    Application: "DjangoExample",
    Environment: "Development",
    Service: "DjangoExample: Dev Resources",
  },
});
