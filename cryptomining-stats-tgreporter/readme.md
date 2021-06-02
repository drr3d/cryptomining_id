# cryptomining-stats-tgreporter

[![License](https://img.shields.io/badge/License-GPLv3+-blue.svg)](https://github.com/drr3d/cryptomining_id/blob/main/cryptomining-stats-tgreporter/LICENSE.txt)

Simple mining application statistic reporter using Telegram Bot.

## Table of Contents

1. [Description](#chapter-001)
2. [Requirements](#chapter-002)
3. [Installation](#chapter-003)
    3.1 [Configuration](#chapter-0031)<br>
4. [Video Tutorial](#chapter-004)
5. [List Supported Mining Software API](#chapter-005)
6. [License and Support](#chapter-006)


## 1. Description <a id="chapter-001"></a>

This piece of code intended to use for windows crypto miners as a support application.

In Windows, we have only a little choice to monitor how our rig condition.

this application intend to simplify how we monitor the rig. Remeber this only for monitoring, so only do one-way communication between
the rig, and you. Two-way communication using Telegram BOT, can be considered just adding more risk to your rig.


## 2. Requirements <a id="chapter-002"></a>

- for required library that support this application, please goto [requirements.txt](https://github.com/drr3d/cryptomining_id/blob/main/cryptomining-stats-tgreporter/requirements.txt)

- you need to create Telegram BOT, using your Telegram Apps, then find BotFather
    * copy the Token provided by BotFather.

## 3. Installation <a id="chapter-003"></a>

- Just download this repository, then extract it

- or you can use git clone this code to your local repository
  ```bash
  $ git clone
  ```

- install [telegram-send](https://github.com/rahiel/telegram-send)
    * you need to paste your copied Telegram bot Token here.
    * after that, you also required to input confimation pin that Telegram send to your apps.
    * don't forget to give star to this awesome [developer](https://github.com/rahiel/telegram-send)

### 3.1 Configuration <a id="chapter-0031"></a>
Configuration file located on [settings.json](https://github.com/drr3d/cryptomining_id/blob/main/cryptomining-stats-tgreporter/settings.json)

in current release, settings.json would look like this:
```json
{
	"miningsoft_cfg":{
		"host":["localhost", "localhost"],
		"port":["10500", "10501"]
	},
    "delay_time":600
}

```

You **must** adjust this file properly, based on how you configure Web API address for each mining software you want to monitor.
1. ```miningsoft_cfg```
    - **host** is a list contained single or multiple address of mining software Web API address/es

        - The standard addres usually formated like this:
        ```
        http://localhost:5555
        ```

        - or if you configure mining software to accept external conection to connect with their API, usually like this:
        ```
        # ip addr: 192.168.100.1 will follow your sistem ip, so check it manually
        # in Windows you can get into Command line then type: ipconfig

        http://192.168.100.1:5555
        ```
    - **port** is a list contained single or multiple port of mining software Web API host port/s

    - When you configure mining software Web API Service to run, normally you must set this two values properly. you cannot just set
    **host** or **port**, you must set both of them.

## 4. List Supported Mining Software API <a id="chapter-004"></a>

- [GMiner v2.54](https://github.com/develsoftware/GMinerRelease/releases/tag/2.54)
- ...

## 5. Video Tutorial <a id="chapter-005"></a>

For more complete tutorial, considered check [my youtube channel](https://www.youtube.com/channel/UCk3KKIUVtdBWWl-wZhUMevg)

## 6. License and Support <a id="chapter-006"></a>

This application is free of use under [certain license](https://github.com/drr3d/cryptomining_id/blob/main/cryptomining-stats-tgreporter/LICENSE.txt).

However, if you find this application is usefull, and wanna support me for future release and improvement
consider buy me a cup of coffe into this ETH address: 0x37c395E2fbDaf62f76A53A1Ea4Fbb693f0938928

