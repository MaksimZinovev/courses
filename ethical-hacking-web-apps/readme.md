# Course Details



**Course Name:** Ethical Hacking: Hacking Web Servers and Web Applications

**Author:** Malcolm Shore

**Link:** [LinkedIn](#https://www.linkedin.com/learning/ethical-hacking-hacking-web-servers-and-web-applications)

![featured-image](api-testing-foundations.png)

# Table of Contents 

[TOC]



## Introduction to Web Servers 

## Elements of web-based applications

- browser [desktop, laptop, mobile device] ↔  HTTP(S) ↔ web proxy ↔   [web server [HTML, Script code] ↔ database or flat file]
- web server  ↔  LDAP (user authentication)



- it is a good practice to use **web proxy** to send and reciev requests as they are designed to be secure and safer system than a full web server
- **forward proxy** - means of enabling internen user to connect to an external server
- **reverse**  **proxy**  - controlling external Internet users connecting in through the corporate perimeter to an internal web server



**Web Applications:**

- model-view -controller architecture
  - **model** - defines data structure (back-end system, e.g. SQL lite)
  - **view** - user interface (eg CSS, HTML, JS)
  - **controller** - business logic (eg JS)



 **Deployment Approaches:**

- web server [model-view -controller]  ↔ DB Server

-  web server [view]  ↔  web server [model-controller]  ↔ DB Server
-  web server [model-view -controller-services [REST, SOAP] 



Typical Folder Structure:

- /images
- /styles
- /classes (functions)
- /includes (constant definitions)



## Dissecting the HTTP / HTTPS protocol

