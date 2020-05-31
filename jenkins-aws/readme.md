# Course Details



**Course:** Running Jenkins on AWS

**Author:**  Michael Jenkins

**Link:** [LinkedIn](#https://www.linkedin.com/learning/running-jenkins-on-aws)



# Table of Contents 

[TOC]



## Create a security group (jenkins master)

Instance will be running on a public internet, using security group give us easy way to limit access to services.

- AWS console > log in (super user) > select  region (↗) > EC2 dashboard
- network and swequrity > create sequrity group > name, description: jenkins master > vpc(default)
- outbound: all traffic
- inbound (incoming traffic) > add rule > 
- SSH, my IP (only traffic from my house)
-  http, port 80, source (leave zeroes) - requests from any ipv4, ipv6 addresss allowed
-  https, port 443, source (leave zeroes)

