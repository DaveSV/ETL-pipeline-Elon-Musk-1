CREATE DATABASE tweets_db;

USE tweets_db;

CREATE TABLE tweets (
    id INT NOT NULL AUTO_INCREMENT,
    tweet_text VARCHAR(280) NOT NULL,
    PRIMARY KEY (id)
);
