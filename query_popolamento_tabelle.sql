USE pos_management;

-- Popolamento della tabella Aziende
INSERT INTO Aziende (nome, indirizzo, p_iva) VALUES 
('Edilizia Milano SRL', 'Via Roma, 10, Milano', '12345678901'),
('Costruzioni Verona SPA', 'Via Verdi, 15, Verona', '98765432109'),
('Imprese Edili Torino', 'Corso Torino, 21, Torino', '10293847566');

-- Popolamento della tabella Cantieri
INSERT INTO Cantieri (id_azienda, nome_cantiere, indirizzo_cantiere, data_inizio, data_fine) VALUES
(1, 'Cantiere Milano Centro', 'Via Dante, 25, Milano', '2023-01-10', '2023-12-20'),
(2, 'Cantiere Verona Sud', 'Via Mazzini, 18, Verona', '2023-05-15', '2024-03-30'),
(3, 'Cantiere Torino Nord', 'Piazza Castello, Torino', '2023-08-01', '2024-07-15');

-- Popolamento della tabella Dipendenti
INSERT INTO Dipendenti (id_azienda, nome, cognome, ruolo, formazione) VALUES
(1, 'Mario', 'Rossi', 'Capo Cantiere', 'Corso di sicurezza avanzata'),
(1, 'Luca', 'Bianchi', 'Operaio', 'Formazione base rischio medio'),
(2, 'Anna', 'Verdi', 'Ingegnere', 'Master sicurezza sul lavoro'),
(2, 'Sara', 'Gialli', 'Operaio', 'Formazione rischio alto'),
(3, 'Giovanni', 'Neri', 'Tecnico', 'Formazione antincendio e primo soccorso');

-- Popolamento della tabella Rischi
INSERT INTO Rischi (nome_rischio, descrizione) VALUES
('Caduta dall’alto', 'Rischio di caduta dai ponteggi o da superfici elevate'),
('Inalazione di polveri', 'Rischio di inalazione di polveri nocive durante la lavorazione'),
('Rumore', 'Esposizione prolungata a livelli di rumore elevati'),
('Scivolamento', 'Possibilità di scivolamento su superfici scivolose o bagnate');

-- Popolamento della tabella Misure_di_sicurezza
INSERT INTO Misure_di_sicurezza (id_rischio, descrizione) VALUES
(1, 'Utilizzo di imbracature di sicurezza e parapetti'),
(2, 'Mascherine e sistemi di ventilazione nei luoghi di lavoro'),
(3, 'Cuffie antirumore obbligatorie per il personale esposto'),
(4, 'Pavimentazione antiscivolo e segnaletica nelle aree di rischio');

-- Popolamento della tabella Pos
INSERT INTO Pos (id_cantiere, data_creazione, data_scadenza) VALUES
(1, '2023-01-10', '2023-12-20'),
(2, '2023-05-15', '2024-03-30'),
(3, '2023-08-01', '2024-07-15');

-- Popolamento della tabella Pos_Rischi
INSERT INTO Pos_Rischi (id_pos, id_rischio) VALUES
(1, 1), -- POS per il Cantiere Milano Centro con rischio Caduta dall’alto
(1, 2), -- POS per il Cantiere Milano Centro con rischio Inalazione di polveri
(2, 3), -- POS per il Cantiere Verona Sud con rischio Rumore
(3, 4); -- POS per il Cantiere Torino Nord con rischio Scivolamento
