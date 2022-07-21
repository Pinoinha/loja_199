CREATE TABLE IF NOT EXISTS Colaborador (
    matricula VARCHAR(7),
    tipoColaborador VARCHAR(10),
    nome VARCHAR(100),
    dataAdmissao DATE,
    salarioBruto MONEY,
    salarioLiquido MONEY,
    percentualComissao FLOAT,
    PRIMARY KEY(matricula)
);

CREATE TABLE IF NOT EXISTS Presenca (
    matricula VARCHAR(7),
    dataHora DATETIME,
    condicao BOOL,
    PRIMARY KEY(matricula, dataHora)
);

CREATE TABLE IF NOT EXISTS Venda (
    matricula VARCHAR(7),
    idVenda INTEGER,
    dataVenda DATE,
    valorTotal NUMERIC(3,2),
    PRIMARY KEY(matricula, idVenda)
);

CREATE TABLE IF NOT EXISTS ProdutoVenda (
    idVenda INTEGER,
    idProduto INTEGER,
    quantidadeVendida INTEGER,
    PRIMARY KEY(idVenda, idProduto)
);

CREATE TABLE IF NOT EXISTS Produto (
    idProduto INTEGER,
    nome VARCHAR(100),
    preco NUMERIC(3,2),
    quantidadeEstoque INTEGER,
    PRIMARY KEY(idProduto)
);

ALTER TABLE Presenca ADD FOREIGN KEY (matricula) references Colaborador;

ALTER TABLE Venda ADD FOREIGN KEY (matricula) references Colaborador;

ALTER TABLE ProdutoVenda ADD FOREIGN KEY (idVenda) references Venda;

ALTER TABLE ProdutoVenda ADD FOREIGN KEY (idProduto) references Produto;
