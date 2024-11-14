-- Creazione del database
CREATE DATABASE IF NOT EXISTS pos_management;
USE pos_management;

-- Creazione delle tabelle
CREATE TABLE Aziende (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    indirizzo VARCHAR(150),
    p_iva VARCHAR(11) UNIQUE  -- Aggiunta unicità per la partita IVA
);

CREATE TABLE Cantieri (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_azienda INT,
    nome_cantiere VARCHAR(100) NOT NULL,
    indirizzo_cantiere VARCHAR(150),
    data_inizio DATE,
    data_fine DATE,
    FOREIGN KEY (id_azienda) REFERENCES Aziende(id) ON DELETE CASCADE
);

CREATE TABLE Dipendenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_azienda INT,
    nome VARCHAR(100),
    cognome VARCHAR(100),
    ruolo VARCHAR(50),
    formazione VARCHAR(100),
    FOREIGN KEY (id_azienda) REFERENCES Aziende(id) ON DELETE CASCADE
);

CREATE TABLE Rischi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_rischio VARCHAR(100) NOT NULL,
    descrizione TEXT,
    id_cantiere INT,  -- Se vuoi associare rischi a cantieri
    FOREIGN KEY (id_cantiere) REFERENCES Cantieri(id) ON DELETE SET NULL  -- Puoi decidere se rimuovere o settare NULL
);

CREATE TABLE Misure_di_sicurezza (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_rischio INT,
    descrizione TEXT,
    misura_sicurezza TEXT,
    FOREIGN KEY (id_rischio) REFERENCES Rischi(id) ON DELETE CASCADE
);

CREATE TABLE Pos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cantiere INT,
    data_creazione DATE,
    data_scadenza DATE,
    FOREIGN KEY (id_cantiere) REFERENCES Cantieri(id) ON DELETE CASCADE
);

CREATE TABLE Pos_Rischi (
    id_pos INT,
    id_rischio INT,
    PRIMARY KEY (id_pos, id_rischio),
    FOREIGN KEY (id_pos) REFERENCES Pos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_rischio) REFERENCES Rischi(id) ON DELETE CASCADE
);
