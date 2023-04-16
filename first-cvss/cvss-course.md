---
tags: [security, course]
aliases: []
description:
public: true
created: 2023-03-06
---

# cvss course

## Links

- [Severity Levels for Security Issues | Atlassian](https://www.atlassian.com/trust/security/security-severity-levels)
- <https://learning.first.org/courses/course-v1:FIRST+CVSSv3.1+2020/courseware/4cb813b88c7243e7a682470fd77bc61f/06c052ee2bf3459db35b3f491321f68a/?child=first#>!tab_17
- <https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator>
- <https://learning.first.org/dashboard>
- [CVSS v3.1 Specification Document](https://www.first.org/cvss/specification-document)

## What is CVSS

CVSS stands for the Common Vulnerability Scoring System and is a vendor-agnostic, industry-open standard designed to convey vulnerability severity and help determine urgency and priority of response.

Currently maintained by Forum of Incident Response and Security Teams (FIRST)

![image](./attachments/MetricGroups.svg)

## CVSS 3.1

- The language in CVSS version 3.1 has been updated to specify that a comprehensive risk assessment should employ more than a CVSS Base Score.
- CVSS v3.1 retains the CVSS v3.0 scoring framework while emphasizing that CVSS measures severity, not risk.
- The language in CVSS version 3.1 has been updated to specify that a comprehensive risk assessment should employ more than a CVSS Base Score.
- Updated the Scope explanation and the concepts of the impacted component and the vulnerable component
- Additional privileges assigned to the Impact metrics
- Additional guidance around scoring software libraries and vulnerability changes

## Terminology

B
Before we get further into the vulnerability, you need to know some key terminology:

The collection of privileges defined by a security authority when granting access to computing resources is the security scope.

> The vulnerable component is the thing that is vulnerable, and is typically a software application, module, driver, or possibly a hardware device.

## Attack Vector

This metric reflects the context by which vulnerability exploitation is possible.

- Network
- Adjacent
- Local
- Physical

![image](./attachments/Mod3_Slide019.jpeg)
![image](./attachments/Mod3_Slide024.jpg)
![image](./attachments/Mod3_Slide024_vector_attack_increase.jpg)

## Attack complexity

![image](./attachments/Mod3_Slide027_complexity.jpeg)

- Low (L) Specialized access conditions or extenuating circumstances do not exist. An attacker can expect repeatable success when attacking the vulnerable component.

- High (H) A successful attack depends on conditions beyond the attacker's control. That is, a successful attack cannot be accomplished at will, but requires the attacker to invest in some measurable amount of effort in preparation or execution against the vulnerable component before a successful attack can be expected.[^2] For example, a successful attack may depend on an attacker overcoming any of the following conditions:
  - The attacker must gather knowledge about the environment in which the vulnerable target/component exists. For example, a requirement to collect details on target configuration settings, sequence numbers, or shared secrets.
  - The attacker must prepare the target environment to improve exploit reliability. For example, repeated exploitation to win a race condition, or overcoming advanced exploit mitigation techniques.
  - The attacker must inject themselves into the logical network path between the target and the resource requested by the victim in order to read and/or modify network communications (e.g., a man in the middle attack).

Low (L). Attacker can reliably exploit the vulnerability at any time

## Privileges Required

This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability.

| Metric Value | Description |
| --- | --- |
| None (N) | The attacker is unauthorized prior to attack, and therefore does not require any access to settings or files of the vulnerable system to carry out an attack. |
| Low (L) | The attacker requires privileges that provide basic user capabilities that could normally affect only settings and files owned by a user. Alternatively, an attacker with Low privileges has the ability to access only non-sensitive resources. |
| High (H) | The attacker requires privileges that provide significant (e.g., administrative) control over the vulnerable component allowing access to component-wide settings and files. |

![image](./attachments/Mod3_Slide034_privileges_increase.jpeg)

## User interaction

This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component. This metric determines whether the vulnerability can be exploited solely at the will of the attacker, or whether a separate user (or user-initiated process) must participate in some manner

| Metric Value | Description |
| --- | --- |
| None (N) | The vulnerable system can be exploited without interaction from any user. |
| Required (R) | Successful exploitation of this vulnerability requires a user to take some action before the vulnerability can be exploited. For example, a successful exploit may only be possible during the installation of an application by a system administrator. |

![image](./attachments/Mod3_Slide043_user_interaction.jpeg)

## Scope

Regarding vulnerable components and impacted components:

A vulnerable component is the thing that is vulnerable; also it’s the security scope that contains the vulnerability.
An impacted component is the thing that suffers the impact; also it’s the security scope that is affected by the vulnerability.

When a vulnerability in a component governed by one security authority is able to affect resources governed by another security authority, a Scope change has occurred. Vulnerable component (web application) is also an impacted component. Sope is unchanged.

The following example vulnerabilities look at different aspects of scoring Scope:

1. A vulnerability in a virtual machine that enables an attacker to read and/or delete files on the host operating system (perhaps even its own virtual machine) is considered a Scope change. In this example, there are two separate security authorities: one that defines and enforces access control for the virtual machine and its users, and another that defines and enforces access control for the host system within which the virtual machine runs.
2. A Scope change occurs when a vulnerability in a web application impacts user clients, e.g., web browsers. Common vulnerabilities of this type include cross-site scripting and URL redirection. The vulnerability is in the web application, but there is an impact to the data/behavior of the victim users’ web browsers, which are within a different security scope.
3. A SQL injection vulnerability in a web application is not usually considered a Scope change assuming the credentials are shared between web application and impacted SQL database, and therefore they are part of the same security scope.
4. A vulnerability that crashes a web server or SSH server is not considered a Scope change since the impact is limited only to the service provided by the affected server. The impact on users is secondary and is not considered a Scope change as users are not considered components.
5. A vulnerability that permits an attacker to exhaust a shared system resource, such as filling up a file system, should not be considered a Scope change as the attacker is still acting under the usual capabilities of the application and not breaching any security boundary.
6. By exploiting a vulnerability in an application that allows users restricted access to resources shared with other components across multiple security scopes (e.g., operating system resources such as system files), an attacker can access resources that they should not be able to access. Since there is already a valid path across the trust boundary, there is no Scope change.

Example: 

> Karen works on the computer security incident response team (CSIRT) for an international bank. She gets an email from a constituent showing that the bank's website is vulnerable to reflected cross-site scripting (XSS). A successful attack requires an attacker to trick a legitimate bank user into browsing to a specific URL. This URL points to the bank's website, but it contains malicious URL parameters that trigger the vulnerability. 
> 
> The malicious code is only able to access information associated with the bank's vulnerable web site due to Same Origin Policy (SOP) restrictions in web browsers. 
>
> What is the Scope metric value Karen assigns?
>
> Answer: 
> The vulnerable component is the web server vulnerable to cross-site scripting, and the impacted component is the victim's browser, so the Scope is Changed. The vulnerable component and the impacted component are not the same thing, so the Scope cannot be Unchanged. 


![image](./attachments/cvss_m003s049a.png)
![image](./attachments/Mod3_Slide051.jpeg)
![image](./attachments/Mod3_Slide054.jpeg)



## Confidentiality 

The Confidentiality Requirement of a system should be based on the classification level of the data that is stored or used by the user and/or applications running on the target system. Encryption of the data at rest on this device should also be taken into consideration when establishing the Confidentiality Requirement. Data that passes through a device without being consumed or processed (e.g., a switch or firewall) should not be taken into consideration when assessing this attribute. See below for examples.

Note: The volume of data may influence the value of the attribute, but should not have as much impact as the classification (i.e., type) of data that is being stored or used.

A device that stores data classified at the highest level should have this attribute rated as High. However, if the sensitive data is encrypted at rest, this attribute may be rated Medium.

A device that stores data classified as non-public but not as high as the highest level should have this attribute rated as Medium. However, if the sensitive data is encrypted at rest, this attribute can be rated Low.

A device that stores data that can be openly shared publicly should have this attribute rated as Low.

Network equipment such as a router, switch, or firewall will generally be rated as Medium due strictly to the sensitivity of information such as routing tables, etc.

Any system that stores login credentials without encryption should have this attribute rated as High. This includes service accounts and credentials embedded into scripts or source code.
<table>

<thead>

<tr>

<th>Metric Value</th>

<th>Description</th>

</tr>

</thead>

<tbody>

<tr>

<td>High (H)</td>

<td>There is a total loss of confidentiality, resulting in all resources within the impacted component being divulged to the attacker. Alternatively, access to only some restricted information is obtained, but the disclosed information presents a direct, serious impact. For example, an attacker steals the administrator's password, or private encryption keys of a web server.</td>

</tr>

<tr>

<td>Low (L)</td>

<td>There is some loss of confidentiality. Access to some restricted information is obtained, but the attacker does not have control over what information is obtained, or the amount or kind of loss is limited. The information disclosure does not cause a direct, serious loss to the impacted component.</td>

</tr>

<tr>

<td>None (N)</td>

<td>There is no loss of confidentiality within the impacted component.</td>

</tr>

</tbody>

</table>

![image](./attachments/Mod3_Slide067.jpeg)

Continue: 
https://learning.first.org/courses/course-v1:FIRST+CVSSv3.1+2020/courseware/4cb813b88c7243e7a682470fd77bc61f/08fe398c02f44f13a2cce41b3d7b2ce8/?child=first#!tab_21


https://www.first.org/cvss/specification-document

https://chandanbn.github.io/cvss/#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N