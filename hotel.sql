CREATE SCHEMA data_reservasi;
USE data_reservasi;

CREATE TABLE reservasi(nama varchar(50) NOT NULL,
 tanggal_pesanan DATE NOT NULL, 
 nomer_kamar INT NOT NULL PRIMARY KEY, 
 jenis_kamar VARCHAR(50)NOT NULL);
 