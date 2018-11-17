# Django2 app for creating Alexa Skills
Django app for easily creating Amazon Alexa Skills

## Table of Content
1. [Prerequisites](#1-prerequisites)
2. [Getting Started](#2-getting-strated)

## 1. Prerequisites
If you're using Apache HTTP Server, **use v2.4.10 or later**!
From [Amazon's Docs](https://developer.amazon.com/de/docs/custom-skills/request-and-response-json-reference.html):
> Note: if you are using Apache HTTP Server to host your web service, use version 2.4.10 or later. Earlier versions of Apache HTTP Server send an "unrecognized name" warning if the server is not configured with a ServerName or ServerAlias in the configuration files. This prevents the Alexa service from sending the customer's request to your server. To address this, either upgrade to 2.4.10 or later, or add ServerName / ServerAlias to your server's configuration file.

## 2. Getting Started
You can use this library with `DEBUG` mode on. The amazon server verification for timestamps however will be skipped. This will cause amazon to not accept your skill if you try to publish your skill in `DEBUG` mode.