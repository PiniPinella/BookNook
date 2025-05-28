CREATE TRIGGER IF NOT EXISTS log_stock_update
AFTER UPDATE ON stock
BEGIN
    INSERT INTO aenderungslog (timestamp, operation, tabelle, eintrag_id, details)
    VALUES (CURRENT_TIMESTAMP, 'UPDATE', 'stock', 1, 'Stock values changed');
END;