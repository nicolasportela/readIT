# readIT

ReadIT, an expression that seeks to encourage reading but also conveys its belonging to the booming technology and information (IT) industry, constitutes a platform that aims to facilitate cultural access and spreading through the implementation of a second-hand books network, also contributing to sustainable consumption, lengthening the life of those books, and spreading community values, with the shared reading as a factor of union between people.

### Table of contents
1. [Installation and Usage](#1)
   1. [Devs](#11)
   2. [Users](#12)
   3. [Usage](#13)
   4. [Examples](#14)
   5. [Demo](#15)
2. [Roadmap](#2)
3. [Authors](#3)
4. [Documentation](#4)

## 1. Installation and Usage <a name="1"></a>

### i. Devs <a name="11"></a>
As a developer you only need 10 steps to run readIT locally and start using the app:

**First**. Install Git: `sudo apt-get update`\
                         `sudo apt-get upgrade`\
                         `sudo apt-get install git`\
**Second**. Clone this repository in a Linux environment: `git clone https://github.com/nicolasportela/readIT.git`\
**Third**. Install Python3.6: `sudo apt-get -y install python3-pip`\
                              `sudo add-apt-repository ppa:deadsnakes/ppa`\
                              `sudo apt-get install python3.6`\
           Or Change default python3 alternatives: `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1`\
                                                   `sudo update-alternatives --config python3`\
**Fourth**. Install Python decouple package: `sudo pip install python-decouple`\
**Fifth**. Install mysql: `sudo apt-get install mysql-server`\
                           `sudo mysql_secure_installation`\
**Sixth**. Install MySQLdb: `sudo apt-get install python3-dev`\
                            `sudo apt-get install libmysqlclient-dev`\
                            `sudo apt-get install zlib1g-dev`\
                            `sudo pip3 install mysqlclient`\
**Seventh**. Install SQLAlchemy module: `sudo pip3 install SQLAlchemy`\
**Eighth**. Located into resources directory, in order to create database with tables, run command `cat tables.sql | mysql -uroot -p`\
**Nineth**. Install flask: `Sudo pip install flask flask-sqlalchemy flask-login`\
**Tenth**. Run Flask: located in readIT directory  `export FLASK_APP=web` and `flask run`.


**Before starting, you must consider:**
* You will need to save your mysql password in .env file; this password is represented in the source code by environment variable, DBPASS (Database password).
* You can test the app with files located in directory `testMainFiles` or run unittests outside directory tests: `python3 -m unittest discover tests`.

### ii. Users <a name="12"></a>
In order to start using the app just go to you favorite browser, type `35.196.233.214`, signup or login and start the adventure of reading and sharing! Help Us to Spread The Culture!.

### iii. Usage <a name="13"></a>
With readIT you can share a book with the community or take it. We believe this will benefit readers of all ages, as well as publishers and authors, who could be benefited from the circulation of texts and the spread of reading, as it constitutes a strategy to attract new audiences to invest in new publications.

* `/Home`: Short introduction.
* `/Sign Up`: First time register.
* `/Login`: Sign in into your account.
* `/Profile`: Options for users, including add a book, accept or confirm request, and Logout.

### iv. Examples <a name="14"></a>


### v. Demo <a name="15"></a>


## 2. Roadmap <a name="2"></a>

The following features are on our road map to implement in a short, medium and long term:   
   - Cancel registration option
   - Users and books evaluation system (comments or score)
   - Profile page with more details (books borrowed and lent)
   - Website suitable for blind people

## 3. Authors <a name="3"></a>
           [Nicolás Portela](https://github.com/nicolasportela)
           [Roberto Ribeiro](https://github.com/ribeiro-uy)
           [Sebastián Olmos](https://github.com/olmoshbtn)
           [Luciana Sarachu](https://github.com/luciana-sarachu)

## 4. Documentation <a name="4"></a>
* [Bulma](https://bulma.io/)
* [Digital Ocean] (https://do.co/3gx7Kqy)
* [Google APIs] (https://www.googleapis.com)
* [Open Library] (https://openlibrary.org/isbn)
</br>