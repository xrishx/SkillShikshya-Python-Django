--BEGINNERS
-- 1. Select all books from the database.
SELECT * FROM Books;

-- 2. Find the title and category of all books published in 2020.
SELECT title, category FROM Books WHERE published_year = 2020;

--3. List all authors from the USA.
SELECT name FROM Authors WHERE country = 'USA';

--4. Insert a new book into the Books table.
INSERT INTO Books (book_id, title, author_id, category, published_year, copies_available)
VALUES (101, 'The Pragmatic Programmer', 1, 'Programming', 1999, 5);

--5. Find all members who joined in the year 2023.
SELECT * FROM Members WHERE EXTRACT(YEAR FROM membership_date) = 2023;

--6. Update the number of copies available for a specific book.
UPDATE Books SET copies_available = 4 WHERE book_id = 101;

--7. Delete a book from the Books table.
DELETE FROM Books WHERE book_id = 101;

--8. Find all books in the ‘Fiction’ category.
SELECT * FROM Books WHERE category = 'Fiction';

--9. Display the name and email of all members.
SELECT name, email FROM Members;

--10. Count how many books are available in the 'History' category.
SELECT COUNT(*) FROM Books WHERE category = 'History';

--11. Find the title of the book borrowed by the member with ID 3.
SELECT title FROM Books 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE member_id = 3;

--12. Display the name and borrowed_date of all members who borrowed a book in January 2023.
SELECT name, borrowed_date FROM Members 
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id 
WHERE EXTRACT(MONTH FROM borrowed_date) = 1 AND EXTRACT(YEAR FROM borrowed_date) = 2023;

--13. List all books authored by 'George Orwell'.
SELECT title FROM Books 
INNER JOIN Authors ON Books.author_id = Authors.author_id 
WHERE Authors.name = 'George Orwell';

--14. Find all authors who were born before 1950.
SELECT name FROM Authors WHERE birth_year < 1950;

--15. Insert a new author into the Authors table.
INSERT INTO Authors (author_id, name, birth_year, country)
VALUES (5, 'Isaac Asimov', 1920, 'Russia');

--16. Display the total number of members.
SELECT COUNT(*) FROM Members;

--17. Show all borrowings that have not been returned yet.
SELECT * FROM Borrowings WHERE return_date IS NULL;

--18. List all unique categories of books in the library.
SELECT DISTINCT category FROM Books;

--19. Find the number of books available for each category
SELECT category, COUNT(*) AS total_books 
FROM Books 
GROUP BY category;

--20. Display the name of the member who borrowed the book titled '1984'
SELECT Members.name 
FROM Members 
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id 
INNER JOIN Books ON Borrowings.book_id = Books.book_id 
WHERE Books.title = '1984';

--INTERMEDIATE
--1. Find the total number of books borrowed by each member.
SELECT member_id, COUNT(book_id) AS total_borrowed 
FROM Borrowings 
GROUP BY member_id;

--2. Display the title and author of the most borrowed book.
SELECT title, name FROM Books 
INNER JOIN Authors ON Books.author_id = Authors.author_id
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
GROUP BY title, name 
ORDER BY COUNT(Borrowings.book_id) DESC LIMIT 1;

--3. Show the author who has the most books in the library.
SELECT name, COUNT(book_id) AS total_books 
FROM Authors 
INNER JOIN Books ON Authors.author_id = Books.author_id 
GROUP BY name 
ORDER BY total_books DESC LIMIT 1;

--4. Find all members who have borrowed more than 3 books.
SELECT member_id, COUNT(book_id) AS total_borrowed 
FROM Borrowings 
GROUP BY member_id 
HAVING COUNT(book_id) > 3;

--5. List all books that have been borrowed but not returned.
SELECT title FROM Books 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE Borrowings.return_date IS NULL;

--6. Find the average number of copies available per category.
SELECT category, AVG(copies_available) 
FROM Books 
GROUP BY category;

--7. Update the return date of a book borrowed by a member.
UPDATE Borrowings 
SET return_date = '2023-09-10' 
WHERE borrowing_id = 5;

--8. Find the titles of books written by authors born in the 20th century.
SELECT title FROM Books 
INNER JOIN Authors ON Books.author_id = Authors.author_id 
WHERE Authors.birth_year BETWEEN 1901 AND 2000;

--9. Display the total number of borrowings made in 2023.
SELECT COUNT(*) 
FROM Borrowings 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2023;

--10. Delete all books in the 'Science' category.
DELETE FROM Books 
WHERE category = 'Science';

--11. Display the top 5 most recently published books.
SELECT title, published_year 
FROM Books 
ORDER BY published_year DESC 
LIMIT 5;

--12. List the names of members who have borrowed all available books.
SELECT name FROM Members 
WHERE member_id IN 
    (SELECT member_id FROM Borrowings 
    GROUP BY member_id 
    HAVING COUNT(book_id) = (SELECT COUNT(*) FROM Books));

--13. Find the total number of unique books borrowed by members in 2023.
SELECT COUNT(DISTINCT book_id) 
FROM Borrowings 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2023;

--14. Display the name and email of members who borrowed books more than twice in 2022.
SELECT name, email FROM Members 
WHERE member_id IN 
    (SELECT member_id FROM Borrowings 
    WHERE EXTRACT(YEAR FROM borrowed_date) = 2022 
    GROUP BY member_id HAVING COUNT(borrowing_id) > 2);

--15. Find all books that were borrowed but have not been returned for over 30 days.
SELECT title FROM Books 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE return_date IS NULL 
AND (CURRENT_DATE - borrowed_date) > 30;

--16. Find the youngest author in the library.
SELECT name FROM Authors 
ORDER BY birth_year DESC 
LIMIT 1;

--17. Find the title of books that have more than 10 copies available.
SELECT title FROM Books 
WHERE copies_available > 10;

--18. Create a view that shows all books along with the author's name.
CREATE VIEW BookAuthors AS
SELECT Books.title, Authors.name AS author_name
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.author_id;

--19. Find the top 3 categories with the most books.
SELECT category, COUNT(*) AS book_count 
FROM Books 
GROUP BY category 
ORDER BY book_count DESC 
LIMIT 3;

--20. Display the names of all members who borrowed books written by 'J.K. Rowling'.
SELECT Members.name FROM Members
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id
INNER JOIN Books ON Borrowings.book_id = Books.book_id
INNER JOIN Authors ON Books.author_id = Authors.author_id
WHERE Authors.name = 'J.K. Rowling';

--ADVANCED
--1. Find the member who has borrowed the most unique books.
SELECT member_id, COUNT(DISTINCT book_id) AS unique_books 
FROM Borrowings 
GROUP BY member_id 
ORDER BY unique_books DESC 
LIMIT 1;

--2. Display the name of the member who borrowed a book for the longest time.
SELECT name, (return_date - borrowed_date) AS days_borrowed 
FROM Members
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id 
ORDER BY days_borrowed DESC 
LIMIT 1;

--3. Calculate the total number of copies of books borrowed per author.
SELECT Authors.name, SUM(Books.copies_available) AS total_copies 
FROM Authors
INNER JOIN Books ON Authors.author_id = Books.author_id
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id
GROUP BY Authors.name;

--4. Find the author with the fewest books in the library.
SELECT Authors.name, COUNT(Books.book_id) AS book_count 
FROM Authors 
INNER JOIN Books ON Authors.author_id = Books.author_id 
GROUP BY Authors.name 
ORDER BY book_count ASC 
LIMIT 1;

--5. Write a query to find the members who never borrowed a book.
SELECT name FROM Members 
WHERE member_id NOT IN (SELECT member_id FROM Borrowings);

--6. Display the average number of days books were borrowed before being returned in 2022.
SELECT AVG(return_date - borrowed_date) AS avg_days_borrowed FROM Borrowings 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2022;

--7. Find the total number of books borrowed per month in 2023.
SELECT EXTRACT(MONTH FROM borrowed_date) AS month, COUNT(book_id) AS books_borrowed 
FROM Borrowings WHERE EXTRACT(YEAR FROM borrowed_date) = 2023 
GROUP BY month ORDER BY month;

--8. List all members who borrowed more than 2 books in January 2023 but haven't borrowed any since.
SELECT member_id, COUNT(book_id) AS total_borrowed 
FROM Borrowings 
WHERE EXTRACT(MONTH FROM borrowed_date) = 1 
    AND EXTRACT(YEAR FROM borrowed_date) = 2023
GROUP BY member_id 
HAVING COUNT(book_id) > 2 
    AND member_id NOT IN 
        (SELECT member_id 
        FROM Borrowings 
        WHERE EXTRACT(MONTH FROM borrowed_date) > 1 
            AND EXTRACT(YEAR FROM borrowed_date) = 2023);

--9. Write a query to find the total number of authors who have at least one book borrowed in 2023.
SELECT COUNT(DISTINCT Authors.author_id) AS total_authors FROM Authors 
INNER JOIN Books ON Authors.author_id = Books.author_id 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2023;

--10 .Create a trigger that updates the copies_available field in the Books table whenever a book is borrowed or returned.
CREATE OR REPLACE FUNCTION update_copies_available() RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE Books SET copies_available = copies_available - 1 WHERE book_id = NEW.book_id;
    ELSIF (TG_OP = 'UPDATE') AND NEW.return_date IS NOT NULL THEN
        UPDATE Books SET copies_available = copies_available + 1 WHERE book_id = NEW.book_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_copies_available_trigger
AFTER INSERT OR UPDATE ON Borrowings
FOR EACH ROW EXECUTE FUNCTION update_copies_available();

--END
