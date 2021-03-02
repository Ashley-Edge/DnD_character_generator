    -- CREATE USER 'ashley'@'172.18.0.2' identified BY 'root';
    -- GRANT ALL PRIVILEGES ON character_db.* TO 'ashley'@'172.18.0.2';
    -- CREATE USER 'ashley'@'172.19.0.2' identified BY 'root';
    -- GRANT ALL PRIVILEGES ON *.* TO 'ashley'@'172.18.0.2';

    -- CREATE USER 'ashley'@'172.19.0.5' identified BY '1234';
    -- GRANT ALL PRIVILEGES ON character_db.* TO 'ashley'@'172.19.0.5';
    -- CREATE USER 'ashley'@'172.19.0.5' identified BY 'root';
    -- GRANT ALL PRIVILEGES ON *.* TO 'ashley'@'172.19.0.5';

    CREATE USER 'ashley'@'%' identified BY '1234';
    GRANT ALL PRIVILEGES ON character_db.* TO 'ashley'@'%';
    GRANT ALL PRIVILEGES ON *.* TO 'ashley'@'%';