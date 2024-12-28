<h1 align="center">Hi there, I'm <a href="https://github.com/andrejevdenis" target="_blank">Denis</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Computer science student</h3>

<h3 align="left">My stack:</h3>

![Python](/icons/Python.svg)
![Pytest](/icons/Pytest.svg)
![IntelliJ IDEA](/icons/IntelliJ_IDEA.svg)
![PyCharm](/icons/PyCharm.svg)
![Git](/icons/Git.svg)
![Jenkins](/icons/Jenkins.svg)
![Postman](/icons/Postman.svg)
![Swagger](/icons/Swagger.svg)
![Jira](/icons/Jira.svg)
![Confluence](/icons/Confluence.svg)
![ElasticSearch](/icons/ElasticSearch.svg)
![Grafana](/icons/Grafana.svg)
![MySQL](/icons/MySQL.svg)
![Postgres](/icons/Postgres.svg)
![Windows](/icons/Windows.svg)
![Android](/icons/Android.svg)
![Ubuntu](/icons/Ubuntu.svg)
![Firefox](/icons/Firefox.svg)
![Google Chrome](/icons/Google_Chrome.svg)
![IE](/icons/Internet_Explorer.svg)
![Opera](/icons/Opera.svg)
![Tor](/icons/Tor.svg)
![Adobe Premiere Pro](/icons/Adobe_Premiere_Pro.svg)
![Adobe Photoshop](/icons/Adobe_Photoshop.svg)
![Notepad++](/icons/Notepad.svg)

## Table of Contents
- [About](#-about)
- [How to Build](#-how-to-build)
- [Summary](#-summary)
- [Contacts](#O%EF%B8%8F-contacts)

## 🚀 About 
I'm **AQA Engineer**, born in 1986 Samara, Russia, here is some facts about me and my QA experience:

- **Education**: 

    2008 - graduated from [The International Market Institute](https://www.imi-samara.ru/), faculty of Economics and Management, specialization in finance and credit.

    2016 - graduated from [City Business School](https://e-mba.ru/catalog/mini-mba), Mini-MBA Professional program, specialization logistics management.  

    2020 - graduated from [Yandex Practicum](https://practicum.yandex.ru/) courses "Test engineer"

    2024 - graduated from [QA-Guru](https://qa.guru/) courses "Python test automation"
- **My QA manual experience**: 

    In 2020 i had my first experience in testing acquired as a tester-assistant in [Yandex](https://yandex.ru/company). 
 
    From 2022 worked in [AvantLab](https://avantlab.ru/) on position JuniorQA, there i gained skills in working with Postman, Git, Jankins, Confluense, Postgress etc. 

    Having gained a certain experience, i been able to get a position of MiddleQA in [AO-RR](https://ao-rr.ru/#main__slider), from 04.2024.
- **My AQA experience**: After i graduated from [QA-Guru](https://qa.guru/) courses i started apply automation at work


## 📝 How to Build

Features for this test:

Website https://www.takamul.net.sa is heavy and if i try run it remotely by Chrome browser on https://selenoid.autotests.cloud it must be windowed on 320x480 size and it takes much more time for each iteration.  
Because of it the test setuped for Firefox browser.  
Or it can be runed local by Chrome browser without any problems.


To build the test local follow these steps:

```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed

# Clone the repository
git clone https://github.com/andrejevdenis/Takamul_proj

# Download last version of Allure
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

# Set up it to main folder of project, rename like "allure"
cd ..\Takamul_proj\allure

# For run it by local browser, apply the specified features in conftest.py
# Run project to build first allure report
pytest tests

# Build allure report
allure/bin/allure.bat serve tests/allure-results

# Troubleshooting 

1. Check installed python packages. Use pip install for packages from requirements.txt
2. Check path environment variable windows
```
## 📈 Summary
First test is just an example of valid test. I fill an incorrect email in order not to clog the production. But it passed!=) And here we go to interesting part of my test...  
Second and third shows bugs on https://www.takamul.net.sa
If i truly worked on it, for failed autotests i go there and manually locate this bug, check what can be wrong else? And then i can create a bug report for developers/

## 🗨️ Contacts

For more details about my experience, services, or any general information, feel free to reach out to me. Below are the best ways to contact:

- **Email**: Send your inquiries at [andrejevdenis00@gmail.com](mailto:andrejevdenis00@gmail.com).
- **Telegram**: Also you can call me or send a message at [t.me/DenisAKtrue](https://t.me/DenisAKtrue).

Looking forward to assisting you and ensuring your business with me is successful and enjoyable!

[Back to top](#top)
