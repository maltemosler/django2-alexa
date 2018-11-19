
# Django2 app for creating Alexa Skills
Django app for easily creating Amazon Alexa Skills. *By Tim Woocker & Malte Mosler*

## Table of Content
1. [Prerequisites](#1-prerequisites)
2. [Getting Started](#2-getting-started)
3. [Settings](#3-settings)
4. [Examples](#4-examples)
5. [Support](#3-support)

## 1. Prerequisites
If you're using Apache HTTP Server, **use v2.4.10 or later**!
From [Amazon's Docs](https://developer.amazon.com/de/docs/custom-skills/request-and-response-json-reference.html):
> Note: if you are using Apache HTTP Server to host your web service, use version 2.4.10 or later. Earlier versions of Apache HTTP Server send an "unrecognized name" warning if the server is not configured with a ServerName or ServerAlias in the configuration files. This prevents the Alexa service from sending the customer's request to your server. To address this, either upgrade to 2.4.10 or later, or add ServerName / ServerAlias to your server's configuration file.

## 2. Getting Started
You can use pip to install this app:

	pip install django2-alexa

In your django *settings.py* add `"django2_alexa"` to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
	...
    'django2_alexa',
	...
]
```
In your current path create a django app with:
```python
python manage.py startapp YourAppName
```

Import & create the `Skill` object in your *views.py*:
```python
from django2_alexa.interfaces.alexa import Skill

skill = Skill()
```

Import the `skill` in your *urls.py*  and add the view to your urlpatterns:
```python
from YourAppName.views import skill

urlpatterns = [
	...
    path('', skill.view)
	...
]
```

You can use this library with `DEBUG` mode on in *settings.py*. The amazon server verification for timestamps however will be skipped. This will cause amazon to not accept your skill if you try to publish your skill in `DEBUG` mode.

Now you are ready to develope your own skill for alexa! You can find a few examples  [here](#4-examples).

## 3. Settings
This django app adds some settings to your project:

|Name|Type|Default|Description|
|--|--|--|--|
|`ALEXA_VERIFY_CONN`|`bool`|`True`|This setting specifies if every request to an alexa skill should be verified against the amazon servers. This is useful when testing your skill without Amazon's service.|

## 4. Examples
[Audio Response](https://github.com/timwoocker/django2-alexa/blob/master/examples/audio/views.py)
[Card Response](https://github.com/timwoocker/django2-alexa/blob/master/examples/card/views.py)
[Slots](https://github.com/timwoocker/django2-alexa/blob/master/examples/slots/views.py)
## 5. Support

Twitter: [@Tim Woocker](https://twitter.com/crey4fun) [@DeemonRider](https://twitter.com/crey4fun)