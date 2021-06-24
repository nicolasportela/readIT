# readIT

ReadIT, an expression that seeks to encourage reading but also conveys its belonging to the booming technology and information (IT) industry, constitutes a platform that aims to facilitate cultural access and spreading through the implementation of a second-hand books network, also contributing to sustainable consumption, lengthening the life of those books, and spreading community values, with the shared reading as a factor of union between people.

Reading let us grow, learn from others, develop our critical spirit, feed our curiosity, live in worlds where the impossible is possible, and we think sharing that with others elevate the experience.
In these times that we all live in a rush, reading a book means taking some time for yourself, and we can't measure how much a book will impact us, just think about that book that you couldn't stop reading, or what about that one you never finished, doesn't it deserve another chance? 

That’s what readIT means for us, click on http://35.196.233.214 and spread the culture!


### Authors 
* Luciana Sarachu [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/luciana-sarachu)  [![GitHub](https://i.stack.imgur.com/tskMh.png)](https://github.com/luciana-sarachu)
&nbsp;
*  Nicolás Portela [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/nicolasportela)  [![GitHub](https://i.stack.imgur.com/tskMh.png)](https://github.com/nicolasportela) 
&nbsp;
*  Roberto Ribeiro [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/ribeiro-uy)  [![GitHub](https://i.stack.imgur.com/tskMh.png)](https://github.com/ribeiro-uy)
&nbsp;
* Sebastián Olmos [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/sebasti%C3%A1n-olmos)  [![GitHub](https://i.stack.imgur.com/tskMh.png)](https://github.com/sebastian-olmos)
&nbsp;


## Table of contents
1. [Installation and Usage](#1)
   1. [Devs](#11)
   2. [Users](#12)
   3. [Usage](#13)
   4. [Examples](#14)
   5. [Demo](#15)
2. [Roadmap](#2)
3. [Documentation](#3)
4. [License](#4)

## 1. Installation and Usage <a name="1"></a>

### i. Devs <a name="11"></a>
As a developer you only need 10 steps to run readIT locally and start using the app:

**First**. Install Git:
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install git
```                      
**Second**. Clone this repository in a Linux environment:
```
$ git clone https://github.com/nicolasportela/readIT.git
$ cd readIT
```
**Third**. Install Python3.6:
```
$ sudo apt-get -y install python3-pip
$ sudo apt-get install python3.6
```
**Fourth**. Install Python decouple package:
```
$ sudo pip install python-decouple
```
**Fifth**. Install mysql:
``` 
$ sudo apt-get install mysql-server
$ sudo mysql_secure_installation
```
**Sixth**. Install MySQLdb:
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```
**Seventh**. Install SQLAlchemy module:
```
$ sudo pip3 install SQLAlchemy
```
**Eighth**. In order to create database with tables, run mysql script:
```
$ cat resources/tables.sql | mysql -uroot -p
```
**Nineth**. Install flask: 
```
$ Sudo pip install flask flask-sqlalchemy flask-login
```
**Tenth**. Now you are ready to run the Application:
```
$ export FLASK_APP=web
$ flask run
```

**Before starting, you must consider:**
* You will need to save your mysql password in .env file; this password is represented in the source code by environment variable, DBPASS (Database password).
* You can test the app with files located in directory `testMainFiles` or run unittests outside directory tests: 
```
$ python3 -m unittest discover tests
```

### ii. Users <a name="12"></a>
In order to start using the app just go to you favorite browser, type http://35.196.233.214 , signup or login and start the adventure of reading and sharing! Help Us to Spread The Culture!.

### iii. Usage <a name="13"></a>
With readIT you can share a book with the community or take it. We believe this will benefit readers of all ages, as well as publishers and authors, who could be benefited from the circulation of texts and the spread of reading, as it constitutes a strategy to attract new audiences to invest in new publications.

* `/Home`: Short introduction.
* `/Sign Up`: First time register.
* `/Login`: Sign in into your account.
* `/Profile`: Options for users, including add a book, accept or confirm request, and Logout.

### iv. Examples <a name="14"></a>
![readIT Preview](https://i.imgur.com/nNdilzd.jpg)

### v. Demo <a name="15"></a>
[![readIT Demo](https://lh3.googleusercontent.com/pw/ACtC-3ejrphnMJ9rzNUVoOf9Hf83tpynsSYMg3RqoTqf8OwlyDEyUe93jKSwxVgo0Tzpykrk8JI5LpYwwJ0PJJnputa_-CwQFMiVbrocqNLUkFLSfd02uRTDP3uR0rZsHzbOzgx5RX-_Lt1bgjWZUO7Sbvg=w1280-h720-no?authuser=0)](https://youtu.be/EZbmrCQOGHA)

## 2. Roadmap <a name="2"></a>

The following features are on our road map to implement in a short, medium and long term:   
   - Cancel registration option
   - Users and books evaluation system (comments or score)
   - Profile page with more details (books borrowed and lent)
   - Website suitable for blind people

## 3. Documentation <a name="3"></a>
* [Bulma](https://bulma.io/)
* [Digital Ocean](https://do.co/3gx7Kqy)
* [Google APIs](https://www.googleapis.com)
* [Open Library](https://openlibrary.org/isbn)

## 4. License <a name="4"></a>
Copyright 2021 readIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

</br>
