DROP TABLE IF EXISTS authors;
CREATE TABLE authors (
  aid int NOT NULL AUTO_INCREMENT,
  name varchar(30) NOT NULL,
  gender varchar(15) DEFAULT NULL,
  dob date DEFAULT NULL,
  country varchar(15) DEFAULT NULL,
  info varchar(255) DEFAULT NULL,
  phone bigint DEFAULT NULL,
  contact varchar(255) DEFAULT NULL,
  PRIMARY KEY (aid)
);

DROP TABLE IF EXISTS books;
CREATE TABLE books (
  bid int NOT NULL AUTO_INCREMENT,
  aid int DEFAULT NULL,
  pid int DEFAULT NULL,
  title varchar(50) NOT NULL,
  genre varchar(30) DEFAULT NULL,
  type varchar(30) DEFAULT NULL,
  isbn bigint DEFAULT NULL,
  availability tinyint(1) DEFAULT NULL,
  edition int DEFAULT NULL,
  no_of_copies int DEFAULT NULL,
  description varchar(255) DEFAULT NULL,
  location varchar(100) DEFAULT NULL,
  PRIMARY KEY (bid),
  KEY aid (aid),
  KEY pid (pid),
  CONSTRAINT books_ibfk_1 FOREIGN KEY (aid) REFERENCES authors (aid),
  CONSTRAINT books_ibfk_2 FOREIGN KEY (pid) REFERENCES publishers (pid)
);

DROP TABLE IF EXISTS credentials;
CREATE TABLE credentials (
  username varchar(20) NOT NULL,
  passwd varchar(30) NOT NULL,
  PRIMARY KEY (username)
);

DROP TABLE IF EXISTS loan;
CREATE TABLE loan (
  bid int NOT NULL,
  mid int NOT NULL,
  date_taken date NOT NULL,
  due_date date NOT NULL,
  KEY bid (bid),
  KEY mid (mid),
  CONSTRAINT loan_ibfk_1 FOREIGN KEY (bid) REFERENCES books (bid),
  CONSTRAINT loan_ibfk_2 FOREIGN KEY (mid) REFERENCES members (mid)
);

DROP TABLE IF EXISTS members;
CREATE TABLE members (
  mid int NOT NULL AUTO_INCREMENT,
  name varchar(30) NOT NULL,
  address varchar(150) DEFAULT NULL,
  phone bigint DEFAULT NULL,
  gender varchar(15) DEFAULT NULL,
  class int DEFAULT NULL,
  no_of_books_rented int NOT NULL DEFAULT '0',
  PRIMARY KEY (mid),
  CONSTRAINT members_chk_1 CHECK ((class in (1,2,3)))
);

DROP TABLE IF EXISTS publishers;
CREATE TABLE publishers (
  pid int NOT NULL AUTO_INCREMENT,
  name varchar(50) DEFAULT NULL,
  contact varchar(255) DEFAULT NULL,
  details varchar(255) DEFAULT NULL,
  PRIMARY KEY (pid)
);

DROP TABLE IF EXISTS reservation;
CREATE TABLE reservation (
  bid int NOT NULL,
  mid int NOT NULL,
  date_reserved date NOT NULL,
  reservation_end_date date NOT NULL,
  KEY bid (bid),
  KEY mid (mid),
  CONSTRAINT reservation_ibfk_1 FOREIGN KEY (bid) REFERENCES books (bid),
  CONSTRAINT reservation_ibfk_2 FOREIGN KEY (mid) REFERENCES members (mid)
);

DROP TABLE IF EXISTS statistics;
CREATE TABLE statistics (
  bid int NOT NULL,
  no_of_loans int NOT NULL DEFAULT '0',
  month int NOT NULL,
  KEY bid (bid),
  CONSTRAINT statistics_ibfk_1 FOREIGN KEY (bid) REFERENCES books (bid)
);