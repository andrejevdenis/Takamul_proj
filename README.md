<h1 align="center">Hi there, I'm <a href="https://github.com/andrejevdenis" target="_blank">Denis</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Computer science student</h3>

<h3 align="left">My stack:</h3>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJIDEA-000000.svg?style=for-the-badge&logo=intellij-idea&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)
![Confluence](https://img.shields.io/badge/confluence-%23172BF4.svg?style=for-the-badge&logo=confluence&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)
![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)
![IE](https://img.shields.io/badge/Internet%20Explorer-0076D6?style=for-the-badge&logo=Internet%20Explorer&logoColor=white)
![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white)
![Tor](https://img.shields.io/badge/Tor-7D4698?style=for-the-badge&logo=Tor-Browser&logoColor=white)
![Adobe Premiere Pro](https://img.shields.io/badge/Adobe%20Premiere%20Pro-9999FF.svg?style=for-the-badge&logo=Adobe%20Premiere%20Pro&logoColor=white)
![Adobe Photoshop](https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white)
![Notepad++](https://img.shields.io/badge/Notepad++-90E59A.svg?style=for-the-badge&logo=notepad%2b%2b&logoColor=black)


## Table of Contents
- [About](#-about)
- [How to Build](#-how-to-build)
- [Summary](#-summary)
- [Contacts](#-contacts)

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

>Website https://www.takamul.net.sa is heavy if i try run it remotly on https://selenoid.autotests.cloud  
Because of it the test setuped fro Firefox browser.
It posible to run it remotly on https://selenoid.autotests.cloud by Chrome browser, it must be windowed on 320*480 size and it takes much more time for each iteration.  
Or we can run it local by Chrome browser without any problems.


To build the packages local, follow these steps:

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

# Run project to build first allure report
pytest tests
For run on local browser delete (browser_management) fixture from "test takamul.py" file

# Build allure report
allure/bin/allure.bat serve tests/allure-results

# Troubleshooting 
1. Check for installed python packages. Use "pip install" for packages from "requirements.txt"
2. Check "path" environment variable windows
```
## 📈 Summary
>First test is just an example of valid test. I fill an incorrect email in order not to clog the production. But it passed!=) And here we go to interesting part of my test...  
Second and third shows bugs on https://www.takamul.net.sa
If i truly worked on it, for failed autotests i go there and manually locate this bug, check what can be wrong else? And then i can create a bug report for developers/

## 🗨️ Contacts

For more details about my experience, services, or any general information, feel free to reach out to me. Below are the best ways to contact:

- **Email**: Send your inquiries at [andrejevdenis00@gmail.com](mailto:andrejevdenis00@gmail.com).
- **Telegram**: Also you can call me or send a message at [t.me/DenisAKtrue](https://t.me/DenisAKtrue).

Looking forward to assisting you and ensuring your business with me is successful and enjoyable!

[Back to top](#top)