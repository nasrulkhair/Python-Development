/*
--Creating Performance table
CREATE TABLE Performance (
    timestamp DATETIME,
    cpu_usage FLOAT,
    memory_usage FLOAT,
    cpu_interrupts INT,
    cpu_calls INT,
    memory_used BIGINT,
    memory_free BIGINT,
    bytes_sent BIGINT,
    bytes_received BIGINT,
    disk_usage FLOAT
);
*/

SELECT * FROM Performance

-- Testing Final Result

DELETE FROM Performance