USE library;

INSERT INTO author (author_id, name, country) VALUES
  (1, 'Naguib Mahfouz',   'Egypt'),
  (2, 'Agatha Christie',  'United Kingdom'),
  (3, 'Gabriel Garcia Marquez', 'Colombia'),
  (4, 'Haruki Murakami',  'Japan');

INSERT INTO book (book_id, title, price, author_id) VALUES
  (1, 'Cairo Trilogy: Palace Walk',        18.50, 1),
  (2, 'Midaq Alley',                       12.00, 1),
  (3, 'Murder on the Orient Express',      14.75, 2),
  (4, 'And Then There Were None',          13.25, 2),
  (5, 'One Hundred Years of Solitude',     20.00, 3),
  (6, 'Love in the Time of Cholera',       16.90, 3),
  (7, 'Norwegian Wood',                    15.00, 4);
