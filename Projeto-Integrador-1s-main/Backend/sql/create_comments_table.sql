-- Cria a tabela de comentários para as ocorrências

CREATE TABLE IF NOT EXISTS comentarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    solicitacao_id INT NOT NULL,
    usuario_id INT NOT NULL,
    tipo_autor VARCHAR(20) NOT NULL,
    mensagem TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX (solicitacao_id)
);
