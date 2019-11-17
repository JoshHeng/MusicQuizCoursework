# Music-Quiz-Python-NEA-Coursework-
This is a music quiz in Python and PHP for the OCR GCSE Computing 9-1 NEA Coursework.

## Features
* A quiz of the names of current songs from the [charts](https://www.officialcharts.com/charts/singles-chart/)
* Beautiful Graphical User Interface
* User account system
* Leaderboard

## Usage 
To run the program, run `Client - Python/Main.py` file. During registration, you will need your account to be authorised - run `Client - Python/AuthoriseAccount.py` to do this.
By default, the program will use my global server. If you would like to use your own server, please refer to the instructions below
### Server Installation
1. You will need web-accessible directory on your webserver which can run PHP files
2. Copy the files in `Server - PHP` to your webroot
3. Create a database and run the following command
```sql
DROP TABLE IF EXISTS `mq_users`;
DROP TABLE IF EXISTS `mq_tokens`;
DROP TABLE IF EXISTS `mq_scores`;

CREATE TABLE mq_users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    username VARCHAR(32) NOT NULL,
    password VARCHAR(256) NOT NULL,
    highscore INT(11) DEFAULT 0 NOT NULL,
    authorised TINYINT(4) DEFAULT 0 NOT NULL
);
CREATE TABLE mq_tokens (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    user_id INT(11) NOT NULL,
    token VARCHAR(128) NOT NULL,
    status TINYINT(4) DEFAULT 0 NOT NULL,
    created_at DATETIME NOT NULL,
    expires_at DATETIME NOT NULL
);
CREATE TABLE mq_scores (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    user_id INT(11) NOT NULL,
    score INT(11) DEFAULT 0 NOT NULL,
    created_at DATETIME NOT NULL
);
```
4. Rename `databaseCredentials.example.php` to `databaseCredentials.php` and fill in your database information
5. For the client files in `Client - Python`, make the following changes:
    1. Change the variable `base_url` on line 8 in `network.py` to your webroot path
    2. Change the variable `url` on line 2 in `AuthoriseAccount.py` to the path of `AuthoriseUser.php` on your webserver

## Known Bugs
* Long song or artist names can result in GUI elements (e.g. buttons) being misaligned
* Song name input boxes can sometimes stop working and not automatically change focus to the next box. Either click the next box manually or press tab to continue, making sure only one character is in the box. This is a Tkinter bug.