--- book

CREATE TRIGGER log_book_insert
AFTER INSERT ON book
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('INSERT', 'book', NEW.id, 'New book added: ' || NEW.title);
END;

CREATE TRIGGER IF NOT EXISTS log_book_update
AFTER UPDATE ON book
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('UPDATE', 'book', NEW.id, 'Book updated: ' || OLD.title || ' → ' || NEW.title);
END;

CREATE TRIGGER IF NOT EXISTS log_book_delete
AFTER DELETE ON book
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('DELETE', 'book', OLD.id, 'Book deleted: ' || OLD.title);
END;

--- ebook

CREATE TRIGGER IF NOT EXISTS log_ebook_insert
AFTER INSERT ON ebook
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('INSERT', 'ebook', NEW.id, 'New ebook added: ' || NEW.title);
END;

CREATE TRIGGER IF NOT EXISTS log_ebook_update
AFTER UPDATE ON ebook
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('UPDATE', 'ebook', NEW.id, 'Ebook updated: ' || OLD.title || ' → ' || NEW.title);
END;

CREATE TRIGGER IF NOT EXISTS log_ebook_delete
AFTER DELETE ON ebook
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('DELETE', 'ebook', OLD.id, 'Ebook deleted: ' || OLD.title);
END;

-- movie

CREATE TRIGGER IF NOT EXISTS log_movie_insert
AFTER INSERT ON movie
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('INSERT', 'movie', NEW.id, 'New movie added: ' || NEW.title);
END;

CREATE TRIGGER IF NOT EXISTS log_movie_update
AFTER UPDATE ON movie
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('UPDATE', 'movie', NEW.id, 'movie updated: ' || OLD.title || ' → ' || NEW.title);
END;

CREATE TRIGGER IF NOT EXISTS log_movie_delete
AFTER DELETE ON movie
BEGIN
    INSERT INTO log (operation, db_table, entry_id, details)
    VALUES ('DELETE', 'movie', OLD.id, 'movie deleted: ' || OLD.title);
END;
