INSERT INTO credentials (username, passwd) VALUES
('devanandan', 'kakakaka'),
('anantha', 'kookookookoo');

INSERT INTO publishers (name, contact, details) VALUES
('Scholastic Press', 1234567890, 'Leading publisher of children''s books'),
('Penguin Random House', 2345678901, 'Major publisher of adult and children''s books'),
('Hachette Book Group', 3456789012, 'Major publisher of institutional knowledge books');

INSERT INTO members (name, address, phone, gender, class) VALUES
('John Doe', '123 Main Street', 4598465494, 'Male', 1),
('Jane Doe', '456 Elm Street', 4842168451, 'Female', 2),
('Peter Smith', '789 Oak Street', 489752542, 'Male', 3),
('Susan Jones', '101 Maple Street', 8952152156, 'Female', 1),
('David Brown', '202 Pine Street', 87841584544, 'Male', 2),
('Elizabeth Green', '303 Elm Street', 487487875, 'Female', 3),
('Michael Williams', '404 Oak Street', 545488884, 'Male', 1),
('Sarah Johnson', '505 Maple Street', 1489744946, 'Female', 3),
('William Thomas', '606 Pine Street', 994719894, 'Male', 3),
('Catherine Anderson', '707 Elm Street', 8998465165, 'Female', 1);

INSERT INTO authors (name, gender, dob, country, info, phone, contact) VALUES 
(
    'J.K. Rowling', 'Female', '1965-07-31', 
    'United Kingdom', 'Best-selling author known for Harry Potter series', 
    1234567890, 'jkrowling@example.com'
  ), 
  (
    'George R.R. Martin', 'Male', '1948-09-20', 
    'United States', 'Author of A Song of Ice and Fire series', 
    9876543210, 'grrmartin@example.com'
  ), 
  (
    'Harper Lee', 'Female', '1926-04-28', 
    'United States', 'Author of To Kill a Mockingbird', 
    5678901234, 'harperlee@example.com'
  );
  
INSERT INTO books (aid, pid, title, genre, type, isbn, availability, 
  edition, no_of_copies, description, location) VALUES 
  (
    1, 1, 'Harry Potter and the Chamber of Secrets', 
    'Fantasy', 'Fiction', 9780747538493, 
    true, 1, 5, 'Second book in the Harry Potter series', 
    'Library A Shelf 15 Row 2'
  ), 
  (
    1, 1, 'Harry Potter and the Prisoner of Azkaban', 
    'Fantasy', 'Fiction', 9780439136365, 
    true, 1, 3, 'Third book in the Harry Potter series', 
    'Library A'
  ), 
  (
    2, 2, 'A Game of Thrones', 'Fantasy', 
    'Fiction', 9780553381689, true, 1, 
    7, 'First book in A Song of ice and Fire series', 
    'Library B'
  ), 
  (
    2, 2, 'A Clash of Kings', 'Fantasy', 
    'Fiction', 9780553381696, true, 2, 
    5, 'Second book in A Song of Ice and Fire series', 
    'Library B'
  ), 
  (
    3, 3, 'To Kill a Mockingbird', 'Fiction', 
    'Novel', 9780446310789, true, 1, 4, 
    'Classic novel set during the Great Depression', 
    'Library C'
  );

