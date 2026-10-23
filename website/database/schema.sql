-- Lab 2: Login & To-Do Application
-- Authors: Kirollos Serag Mouner (2304102), Ahmed Ramdan Mohamed (2304109)
-- Re-runnable: drops and recreates the whole database. No data inserted.

DROP DATABASE IF EXISTS registration;
CREATE DATABASE registration;
USE registration;

CREATE TABLE users (
    user_id           INT          NOT NULL AUTO_INCREMENT,
    email             VARCHAR(255) NOT NULL,
    name              VARCHAR(100) NOT NULL,
    password_hash     VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id),
    UNIQUE (email)
);

CREATE TABLE todos (
    todo_id    INT          NOT NULL AUTO_INCREMENT,
    user_id    INT          NOT NULL,
    title      VARCHAR(200) NOT NULL,
    is_done    TINYINT(1)   NOT NULL DEFAULT 0,
    created_at TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (todo_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);
