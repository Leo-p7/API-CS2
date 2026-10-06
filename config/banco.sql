CREATE DATABASE IF NOT EXISTS cs2;
USE cs2;

CREATE TABLE IF NOT EXISTS times (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    sigla VARCHAR(10) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    regiao VARCHAR(30) NOT NULL,
    ano_fundacao INT NOT NULL,
    ranking INT NOT NULL
);

-- Dados de exemplo (pode editar/trocar à vontade)
INSERT INTO times (nome, sigla, pais, regiao, ano_fundacao, ranking) VALUES
('FURIA Esports', 'FUR', 'Brasil', 'América do Sul', 2017, 5),
('MIBR', 'MIBR', 'Brasil', 'América do Sul', 2003, 25),
('paiN Gaming', 'PAIN', 'Brasil', 'América do Sul', 2010, 20),
('Imperial Esports', 'IMP', 'Brasil', 'América do Sul', 2015, 22),
('Natus Vincere', 'NAVI', 'Ucrânia', 'Europa', 2009, 4),
('FaZe Clan', 'FAZE', 'Estados Unidos', 'Europa', 2010, 10),
('Team Vitality', 'VIT', 'França', 'Europa', 2013, 1),
('G2 Esports', 'G2', 'Alemanha', 'Europa', 2013, 6),
('Team Spirit', 'TS', 'Rússia', 'Europa', 2015, 3),
('MOUZ', 'MOUZ', 'Alemanha', 'Europa', 2002, 7);
