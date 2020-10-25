# Course Details



**Course Name:** AWS Cloud Practitioner

**Website:** wizlabz

**Link:** [Whizlabs](https://www.whizlabs.com/aws-certified-cloud-practitioner/)

**Date:** July 2020

![featured-image](header-image.png)

# Table of Contents 

- [Course Details](#course-details)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
  * [1. Course Introduction](#1-course-introduction)
  * [Elements of web-based applications](#elements-of-web-based-applications)
  * [2. About the exam](#2-about-the-exam)
- [Cloud Concepts](#cloud-concepts)
  * [3. Agenda](#3-agenda)
  * [4. What is the Cloud?](#4-what-is-the-cloud)
  * [5. What is Amazon Web Services?](#5-what-is-amazon-web-services)
  * [6. AWS Free Account](#6-aws-free-account)
  * [7. AWS Console](#7-aws-console)
  * [8. Regions and Availability Zones](#8-regions-and-availability-zones)
  * [9. AWS Support](#9-aws-support)
  * [10. Summary](#10-summary)
- [AWS Core Services](#aws-core-services)
  * [11. AWS Core Services Overview](#11-aws-core-services-overview)
  * [12. Simple Storage Service](#12-simple-storage-service)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

[TOC]

# Introduction 

## 1. Course Introduction



##  Elements of web-based applications

- browser [desktop, laptop, mobile device] ↔  HTTP(S) ↔ web proxy ↔   [web server [HTML, Script code] ↔ database or flat file]
- web server  ↔  LDAP (user authentication)



## 2. About the exam

**link:** https://aws.amazon.com/certification/certified-cloud-practitioner/

![exam](./ch1/exam.png)



**Abilities Validated by the Certification:**

- Define what the AWS Cloud is and the basic global infrastructure
- Describe basic AWS Cloud architectural principles
- Describe the AWS Cloud value proposition
- Describe key services on the AWS platform and their common use cases (for example, compute and analytics)
- Describe basic security and compliance aspects of the AWS platform and the shared security model
  Define the billing, account management, and pricing models
- Identify sources of documentation or technical assistance (for example, whitepapers or support tickets)
  Describe basic/core characteristics of deploying and operating in the AWS Cloud



# Cloud Concepts



## 3. Agenda



## 4. What is the Cloud?

Examples of lcoud services (internet services)

- Gmail - email
- Dropbox, Google Drive - file sharing
- Youtube - video sharing
- Facebook - social media



Benefits of using CS:

- affordable
- available across the world
- scalable
- reliable



## 5. What is Amazon Web Services?

**AWS:**

- largest CS platform
- launched in 2002
- more than 100 service available currently
- https://aws.amazon.com/

**Some services:**

- Elastic Compute CLoud
- Simple Storage Service
- Relational Database Service
- Virtual Private Service



## 6. AWS Free Account

**Free services:**

![free tier](./ch6/free_tier.png)



**12 months free:**

![12months](./ch6/12months.png)



## 7. AWS Console

- Sign Up new account 
- Sign In
- access services using search field, top menu or scroll down to use simple wizards
- my account ↗
- billing dashboard ↗
- aws region ↗
- aws support ↗



## 8. Regions and Availability Zones

- AWS have regions across the world which can be used to host resources
- new data centers are added as AWS expanding their global infrastructure
- factors influencing region:
  - close proximity to users
  - data requirement for specific region (stored in specific region)



- AWS have multiple data centers in availability zone:

- availability zone (data center 1, data center 2, ...)

- AWS have multiple availability zones  in region:

- region (availability zone 1, availability zone 2, ... )

  ![](./ch8/aws_zones.png)



## 9. AWS Support

- **3 support plans available:**
  - developer - cheapest, but longer response time, starts at $29 per month
  - business
  - enterprise - most expensive, starts at $15K per month response time < 15 min, dedicated  account manager and other features
- Amazon Partner Network (APN) - is the global partner program for technology and consulting businesses
- https://aws.amazon.com/partners/
- APN Partner Types
  - **APN Consulting Partners** - professional services firms that help customers of all types and sizes **design, architect, build, migrate, and manage** their workloads and applications on AWS
  - **APN Technology Partners** - **provide hardware**, connectivity services, or software solutions that are either hosted on, or integrated with, the AWS Cloud

## 10. Summary

- what is cloud computing
- concept of AWS
- tour of AWS console 
- AWS suport plans
- global infrustructure



# AWS Core Services



## 11. AWS Core Services Overview

- Simple Storage Service
- Amazon Glacier
- Virtual Private Cloud
- Elastic Compute Cloud
- Elastick Block Storage
- Costing Aspects



## 12. Simple Storage Service



- object level storage
- allows to store and retrieve any amount of data 
- highly scalable
- highly reliable



**Structure**

- S3 > bucket(s) > object(s)



**Storage classes**

- standard (default) - accessed **frequently**
- reduced redundancy  - to store non-critical data
- STANDARD_IA, ONEZONE_IA - accessed **infrequently**
- GLACIER and DEEP ARCHIVE - for data archival, lower costs



**Other S3 features**

- versioning
- use for static website
- cross region replication - better reliability
- manage access - using Bucket policies



## 13. Lab - Simple Storage Service Part 1

- sign in to AWS Management Console
- ↖ "Services" > S3
- create bucket > name (must be unique across AWS) > create
- click on the bucket name
- upload > add file > upload
- to create folder > select bucket > create folder
- note: anonymous user cannot access bucket  objects via url link



To make object public

- go to bucket > permissions > public access settings > edit
- uncheck Block public access to buckets and objects granted through new access control lists (ACLs) > save > confirm
- select file/object in bucket  > make public
- go to bucket > permissions > Block public access > edit
- uncheck Block public access to buckets and objects granted through any access control lists (ACLs) > save > confirm
- now file/object can be accessed anonymously 



## 14. Lab - Simple Storage Service Part 2

- sign in to AWS Management Console
- ↖ "Services" > S3
- select bucket > Properties > set up necessary properties
  - versioning
  - server access logging
  - static website hosting
  - object level logging
  - default encryption
  - other
- to access objet properties
- select object > properties
  - storage class
  - encryption
  - metadata 
  - tags
  - object lock



## 15.  Lab - S3 - Static Website Hosting

- sign in to AWS Management Console
- ↖ "Services" > S3
- properties > Use this bucket to host a website
- fill in index.html name as default page
- copy endpoint http://mzinb1.s3-website-ap-southeast-2.amazonaws.com
- go to bucket > click file >make public
- visit page using endpoint link
- page shoould be displaying



## 16. Amazon Glacier

- used for cold archive storage
- much lower cost compared to standard class of S3



**How it works**

- create vault to hold the objects
- to upload object need to use AWS CLI or SDK
- Lifecycle feature in S3 can be used to move object to Glacier
- to retrieve object need to submit job request (takes 3-5 hours to download object)
- expedited retrieval (higher cost)



## 17. Lab - Amazon Glacier

- sign in to AWS Management Console
- ↖ "Services" > S3 Glacier
- create vault > enter name > next > next > submit



- to use Lifecycle feature upload object to bucket
- open bucket > management > add lifecycle rule
- enter tag or all objects > next
- current version > add transition > Trnsition to Glacier after <days>
- next > save



## 18. Virtual Private Cloud 

- VPC service allows to have isolated virtual network in AWS.

- VPC allows launch resources such as EC2.

- You can define a network connectivity.

- You can have different networks for different purposes.

- Each network will have the servers placed in them.

- the servers will then get IP addresses.

- AWS VPC will be allocated a CDIDR block (e.g. 10.0.0.0/16).

- Structure:

  - VPC (CIDR block).

    - subnet1 (CIDR block - subset of VPC CIDR).

    - subnet2  (CIDR block - subset of VPC CIDR).

      - EC2.
      - EC2.

      

## 19. Lab - Virtual Private Cloud (Creating a Virtual Private Cloud with VPC Wizard)

**Create VPC**

- select region (for example N. Virginia, remember, VPC is a region specific resource)
- view all services ↖ "Services" > VPC > Launch VPC Wizard
- VPC with a Single Public Subnet > Select
- IPv4 CIDR block and the IPv4 CIDR of public subnet will be automatically assigned to you
- enter subnet name > myfirstvpc
- Leave the other feilds as default
- Create VPC



**Resources Created**

- Dashboard > your VPCs
- Click Subnets ↖ (one subnet per availability zone)
- Click Route Tables ↖ (You can see two route tables (one for public subnet and one for private subnet).)
- Click Internet Gateways ↖ (The Internet Gateway is created and is attached to the public subnet. Internet Gateway connects your VPC to the Internet)

​	



## 20 Elastic Compute Cloud  Service





# Lab: Access and tour AWS console

- sign in and go to AWS Management Console
- view all services ↖ "Services"
- view/select region ↗ "Sydney"
- to add a shortcut click on pushpit icon  ↑
- drag a any service  to navigation bar
- click on pushpit icon  ↑









# Introduction to AWS Identity Access Management (IAM)

**Create new users**

- sign in to AWS Management Console
- to create new user Services  > IAM
- Select  ← "Users" > Add user
- fill in Name 
- Select AWS Access type 
-  AWS Management Console access: Check > Programmatic access: Uncheck
- Require password reset:  Uncheck
- Console password: abcd
- next: Permissions > next: Tags
- Key: team
- Value: developers
- create users
- Note: Ignore  error if it appears while creating Users.

```
Success
You successfully created the users shown below. You can view and download user security credentials. You can also email users instructions for signing in to the AWS Management Console. This is the last time these credentials will be available to download. However, you can create new credentials at any time.

Users with AWS Management Console access can sign-in at: https://
```

- download csv file with sign in link
- click on the sign in link > enter user name > enter password
- you are signed in



**Create IAM Group**

- to create new group  Services  > IAM
- Select  ← "Groups" > Create New Group
- Name: Dev > next step
- Attach policy > AWSCodeDeployFullAccess, AWSCodeDeployRole, Billing (example)
- next step
- create group



**Add IAM user to IAM group**

- Services  > IAM

- Select  ← "Groups" >  select group

- select Users tab

- add users to group > select users > add users

  

