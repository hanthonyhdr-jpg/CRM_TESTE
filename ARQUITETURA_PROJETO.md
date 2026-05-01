# 🏗️ ARQUITETURA DO SISTEMA - CRM COMUNICAÇÃO VISUAL

## Stack Tecnológico

- **Backend**: Python + FastAPI
- **Banco de Dados**: SQLite (.db)
- **Frontend**: HTML5 + CSS3 + JavaScript Vanilla
- **API**: REST com autenticação JWT
- **Servidor**: Uvicorn (FastAPI)
- **ORM**: SQLAlchemy
- **Autenticação**: JWT + SHA-256

---

## 📁 Estrutura de Pastas

```
crm-comunicacao-visual/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Inicialização FastAPI
│   │   ├── config.py               # Configurações (.env)
│   │   ├── database.py             # Conexão SQLite + SQLAlchemy
│   │   ├── schemas.py              # Pydantic models (validação)
│   │   ├── models.py               # SQLAlchemy models (tabelas)
│   │   │
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # POST /login, /logout, /register
│   │   │   ├── services.py         # Lógica de autenticação
│   │   │   └── jwt_handler.py      # Geração e validação de tokens
│   │   │
│   │   ├── usuarios/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de usuários
│   │   │   └── services.py         # Lógica de negócio
│   │   │
│   │   ├── empresa/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # GET/PUT empresa
│   │   │   └── services.py
│   │   │
│   │   ├── clientes/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de clientes
│   │   │   └── services.py
│   │   │
│   │   ├── produtos/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de produtos
│   │   │   └── services.py
│   │   │
│   │   ├── categorias/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de categorias
│   │   │   └── services.py
│   │   │
│   │   ├── orcamentos/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de orçamentos
│   │   │   ├── services.py         # Cálculos, numeração
│   │   │   └── calculos.py         # Lógica de cálculo detalhada
│   │   │
│   │   ├── orcamento_itens/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de itens
│   │   │   └── services.py
│   │   │
│   │   ├── assinaturas/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # POST assinatura, GET validação
│   │   │   └── services.py         # Hash SHA-256, validação
│   │   │
│   │   ├── ordens/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD de ordens de serviço
│   │   │   └── services.py
│   │   │
│   │   ├── financeiro/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # CRUD financeiro
│   │   │   └── services.py
│   │   │
│   │   ├── dashboard/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # GET /kpis, /graficos
│   │   │   └── services.py
│   │   │
│   │   ├── relatorios/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── services.py
│   │   │
│   │   ├── logs/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── services.py
│   │   │
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   ├── auth_middleware.py  # Verificação JWT
│   │   │   └── cors_middleware.py
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── validators.py       # Validações (CPF, CNPJ, email)
│   │   │   ├── formatters.py       # Formatação de dados
│   │   │   ├── hash_utils.py       # SHA-256, UUID
│   │   │   └── cep_utils.py        # Integração ViaCEP
│   │   │
│   │   └── migrations/
│   │       └── alembic/ (se usar)
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_clientes.py
│   │   ├── test_orcamentos.py
│   │   └── ...
│   │
│   ├── .env                         # Variáveis de ambiente
│   ├── .env.example
│   ├── requirements.txt
│   ├── run.py                       # Script para rodar servidor
│   └── database.db                  # Arquivo SQLite (gerado)
│
├── frontend/
│   ├── css/
│   │   ├── style.css               # Design system completo
│   │   └── responsive.css          # Media queries
│   │
│   ├── js/
│   │   ├── api.js                  # Cliente HTTP (fetch)
│   │   ├── auth.js                 # Login, logout, sessão
│   │   ├── utils.js                # Formatação, máscaras, validações
│   │   ├── calculos.js             # Lógica de cálculo do orçamento
│   │   ├── pdf.js                  # Geração de PDF (jsPDF)
│   │   ├── assinatura.js           # Canvas de assinatura
│   │   ├── app.js                  # Inicialização global
│   │   └── components.js           # Componentes reutilizáveis
│   │
│   ├── pages/
│   │   ├── index.html              # Redirecionador
│   │   ├── login.html
│   │   ├── setup-inicial.html
│   │   ├── dashboard.html
│   │   ├── clientes.html
│   │   ├── cliente-form.html
│   │   ├── cliente-detalhe.html
│   │   ├── produtos.html
│   │   ├── produto-form.html
│   │   ├── categorias.html
│   │   ├── orcamentos.html
│   │   ├── orcamento-form.html
│   │   ├── orcamento-detalhe.html
│   │   ├── orcamento-preview.html
│   │   ├── assinar.html
│   │   ├── ordens.html
│   │   ├── financeiro.html
│   │   ├── relatorios.html
│   │   ├── configuracoes.html
│   │   ├── usuarios.html
│   │   └── 404.html
│   │
│   └── images/
│       └── logo-default.png
│
├── docker-compose.yml (opcional)
├── README.md
├── .gitignore
└── run.sh / run.bat

```

---

## 🗄️ Schema SQLite Completo

```sql
-- Limpar banco anterior (desenvolvimento)
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS financeiro;
DROP TABLE IF EXISTS assinaturas;
DROP TABLE IF EXISTS orcamento_itens;
DROP TABLE IF EXISTS orcamentos;
DROP TABLE IF EXISTS ordens_servico;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS unidades_medida;
DROP TABLE IF EXISTS categorias_produto;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS empresa;
DROP TABLE IF EXISTS usuarios;

-- ============================================================
-- TABELA: usuarios
-- ============================================================
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL,
    perfil TEXT NOT NULL CHECK(perfil IN ('admin', 'gerente', 'vendedor', 'financeiro')),
    ativo BOOLEAN NOT NULL DEFAULT 1,
    ultimo_acesso TIMESTAMP,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_perfil ON usuarios(perfil);

-- ============================================================
-- TABELA: empresa
-- ============================================================
CREATE TABLE empresa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_fantasia TEXT NOT NULL,
    razao_social TEXT NOT NULL,
    cnpj TEXT NOT NULL UNIQUE,
    telefone TEXT,
    whatsapp TEXT,
    email TEXT,
    site TEXT,
    cep TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    estado TEXT,
    logo_base64 LONGTEXT,
    cor_primaria TEXT DEFAULT '#2563EB',
    cor_secundaria TEXT DEFAULT '#64748B',
    texto_rodape_orcamento TEXT,
    texto_condicoes_padrao TEXT,
    prazo_validade_orcamento INTEGER DEFAULT 7,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA: clientes
-- ============================================================
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL CHECK(tipo IN ('PF', 'PJ')),
    nome_razao TEXT NOT NULL,
    cpf_cnpj TEXT NOT NULL UNIQUE,
    rg_ie TEXT,
    data_nascimento TEXT,
    email TEXT,
    telefone TEXT,
    whatsapp TEXT,
    cep TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    estado TEXT,
    tipo_cliente TEXT CHECK(tipo_cliente IN ('eventual', 'recorrente', 'corporativo', 'agencia')),
    ramo_atividade TEXT,
    como_conheceu TEXT CHECK(como_conheceu IN ('indicacao', 'instagram', 'google', 'fachada', 'outro')),
    possui_arte_propria BOOLEAN DEFAULT 0,
    prefere_contato TEXT CHECK(prefere_contato IN ('whatsapp', 'email', 'telefone', 'presencial')),
    desconto_especial DECIMAL(5,2) DEFAULT 0,
    limite_credito DECIMAL(12,2),
    prazo_pgto_padrao INTEGER DEFAULT 0,
    observacoes TEXT,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    usuario_id INTEGER NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ultima_atualizacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE INDEX idx_clientes_cpf_cnpj ON clientes(cpf_cnpj);
CREATE INDEX idx_clientes_email ON clientes(email);
CREATE INDEX idx_clientes_nome_razao ON clientes(nome_razao);
CREATE INDEX idx_clientes_ativo ON clientes(ativo);

-- ============================================================
-- TABELA: categorias_produto
-- ============================================================
CREATE TABLE categorias_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,
    cor_hex TEXT NOT NULL,
    icone TEXT NOT NULL,
    ordem INTEGER NOT NULL DEFAULT 0,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_categorias_ativo ON categorias_produto(ativo);

-- ============================================================
-- TABELA: unidades_medida
-- ============================================================
CREATE TABLE unidades_medida (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sigla TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    tipo_calculo TEXT NOT NULL CHECK(tipo_calculo IN ('area', 'linear', 'hora', 'unidade', 'verba')),
    permite_decimal BOOLEAN NOT NULL DEFAULT 1,
    casas_decimais INTEGER NOT NULL DEFAULT 2,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_unidades_sigla ON unidades_medida(sigla);

-- ============================================================
-- TABELA: produtos
-- ============================================================
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria_id INTEGER NOT NULL,
    codigo TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    descricao_curta TEXT,
    descricao_tecnica TEXT,
    unidade_id INTEGER NOT NULL,
    unidade_sigla TEXT NOT NULL,
    preco_custo DECIMAL(12,2) NOT NULL,
    margem_padrao DECIMAL(5,2) NOT NULL DEFAULT 40,
    preco_venda DECIMAL(12,2) NOT NULL,
    preco_minimo DECIMAL(12,2) NOT NULL,
    permite_desconto BOOLEAN NOT NULL DEFAULT 1,
    desconto_maximo DECIMAL(5,2) NOT NULL DEFAULT 10,
    largura_minima DECIMAL(8,3),
    largura_maxima DECIMAL(8,3),
    altura_minima DECIMAL(8,3),
    altura_maxima DECIMAL(8,3),
    area_minima_cobranca DECIMAL(8,4) DEFAULT 0,
    tempo_producao_dias INTEGER DEFAULT 3,
    fornecedor TEXT,
    observacoes_producao TEXT,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ultima_atualizacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias_produto(id),
    FOREIGN KEY (unidade_id) REFERENCES unidades_medida(id)
);

CREATE INDEX idx_produtos_categoria_id ON produtos(categoria_id);
CREATE INDEX idx_produtos_codigo ON produtos(codigo);
CREATE INDEX idx_produtos_nome ON produtos(nome);
CREATE INDEX idx_produtos_ativo ON produtos(ativo);

-- ============================================================
-- TABELA: orcamentos
-- ============================================================
CREATE TABLE orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL UNIQUE,
    cliente_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    data_emissao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_validade TIMESTAMP NOT NULL,
    status TEXT NOT NULL DEFAULT 'rascunho' CHECK(status IN ('rascunho', 'enviado', 'aprovado', 'em_producao', 'entregue', 'cancelado')),
    prazo_entrega_dias INTEGER NOT NULL DEFAULT 5,
    local_instalacao TEXT,
    requer_instalacao BOOLEAN DEFAULT 0,
    requer_arte BOOLEAN DEFAULT 0,
    requer_visita_tecnica BOOLEAN DEFAULT 0,
    subtotal DECIMAL(12,2) NOT NULL DEFAULT 0,
    desconto_geral_tipo TEXT CHECK(desconto_geral_tipo IN ('percentual', 'valor')),
    desconto_geral_valor DECIMAL(12,2) DEFAULT 0,
    desconto_geral_calculado DECIMAL(12,2) DEFAULT 0,
    valor_frete DECIMAL(12,2) DEFAULT 0,
    valor_total DECIMAL(12,2) NOT NULL DEFAULT 0,
    forma_pagamento TEXT CHECK(forma_pagamento IN ('avista', '50_50', 'parcelado', 'boleto', 'pix')),
    condicao_pagamento TEXT,
    observacoes_cliente TEXT,
    observacoes_internas TEXT,
    token_publico TEXT UNIQUE,
    assinatura_id INTEGER,
    data_envio TIMESTAMP,
    data_aprovacao TIMESTAMP,
    data_cancelamento TIMESTAMP,
    motivo_cancelamento TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (assinatura_id) REFERENCES assinaturas(id)
);

CREATE INDEX idx_orcamentos_numero ON orcamentos(numero);
CREATE INDEX idx_orcamentos_cliente_id ON orcamentos(cliente_id);
CREATE INDEX idx_orcamentos_usuario_id ON orcamentos(usuario_id);
CREATE INDEX idx_orcamentos_status ON orcamentos(status);
CREATE INDEX idx_orcamentos_token_publico ON orcamentos(token_publico);
CREATE INDEX idx_orcamentos_data_emissao ON orcamentos(data_emissao);

-- ============================================================
-- TABELA: orcamento_itens
-- ============================================================
CREATE TABLE orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orcamento_id INTEGER NOT NULL,
    ordem INTEGER NOT NULL,
    tipo TEXT NOT NULL CHECK(tipo IN ('produto', 'servico', 'desconto_item', 'texto')),
    produto_id INTEGER,
    descricao TEXT NOT NULL,
    unidade TEXT NOT NULL,
    tipo_calculo TEXT NOT NULL CHECK(tipo_calculo IN ('area', 'linear', 'hora', 'unidade', 'verba')),
    largura DECIMAL(8,4),
    altura DECIMAL(8,4),
    comprimento DECIMAL(8,4),
    quantidade_calculada DECIMAL(12,4),
    quantidade_manual DECIMAL(12,4),
    usar_quantidade_manual BOOLEAN DEFAULT 0,
    quantidade_final DECIMAL(12,4),
    preco_unitario DECIMAL(12,2),
    desconto_item_tipo TEXT CHECK(desconto_item_tipo IN ('percentual', 'valor')),
    desconto_item_valor DECIMAL(12,2) DEFAULT 0,
    desconto_item_calculado DECIMAL(12,2) DEFAULT 0,
    valor_item DECIMAL(12,2),
    observacao_item TEXT,
    cor_material TEXT,
    especificacao_tecnica TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE INDEX idx_orcamento_itens_orcamento_id ON orcamento_itens(orcamento_id);
CREATE INDEX idx_orcamento_itens_produto_id ON orcamento_itens(produto_id);

-- ============================================================
-- TABELA: assinaturas
-- ============================================================
CREATE TABLE assinaturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orcamento_id INTEGER NOT NULL UNIQUE,
    cliente_id INTEGER NOT NULL,
    nome_confirmado TEXT NOT NULL,
    imagem_base64 LONGTEXT,
    ip_address TEXT,
    user_agent TEXT,
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    hash_validacao TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'valida' CHECK(status IN ('valida', 'revogada')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE INDEX idx_assinaturas_orcamento_id ON assinaturas(orcamento_id);
CREATE INDEX idx_assinaturas_cliente_id ON assinaturas(cliente_id);
CREATE INDEX idx_assinaturas_status ON assinaturas(status);

-- ============================================================
-- TABELA: ordens_servico
-- ============================================================
CREATE TABLE ordens_servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL UNIQUE,
    orcamento_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    usuario_responsavel_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'aguardando_arte' CHECK(status IN ('aguardando_arte', 'arte_aprovada', 'em_producao', 'producao_concluida', 'aguardando_instalacao', 'instalado', 'entregue')),
    arte_recebida BOOLEAN DEFAULT 0,
    arte_aprovada_cliente BOOLEAN DEFAULT 0,
    data_inicio_producao TIMESTAMP,
    data_conclusao_producao TIMESTAMP,
    data_instalacao_agendada TIMESTAMP,
    data_entrega TIMESTAMP,
    observacoes_producao TEXT,
    observacoes_instalacao TEXT,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (usuario_responsavel_id) REFERENCES usuarios(id)
);

CREATE INDEX idx_ordens_numero ON ordens_servico(numero);
CREATE INDEX idx_ordens_orcamento_id ON ordens_servico(orcamento_id);
CREATE INDEX idx_ordens_cliente_id ON ordens_servico(cliente_id);
CREATE INDEX idx_ordens_status ON ordens_servico(status);

-- ============================================================
-- TABELA: financeiro
-- ============================================================
CREATE TABLE financeiro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL CHECK(tipo IN ('receita', 'despesa')),
    categoria TEXT NOT NULL CHECK(categoria IN ('venda', 'servico', 'material', 'aluguel', 'salario', 'imposto', 'outro')),
    descricao TEXT NOT NULL,
    valor DECIMAL(12,2) NOT NULL,
    data_lancamento TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_vencimento TIMESTAMP NOT NULL,
    data_pagamento TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pendente' CHECK(status IN ('pendente', 'pago', 'cancelado')),
    orcamento_id INTEGER,
    cliente_id INTEGER,
    forma_pagamento TEXT,
    comprovante_base64 LONGTEXT,
    observacoes TEXT,
    usuario_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE INDEX idx_financeiro_tipo ON financeiro(tipo);
CREATE INDEX idx_financeiro_status ON financeiro(status);
CREATE INDEX idx_financeiro_data_lancamento ON financeiro(data_lancamento);
CREATE INDEX idx_financeiro_orcamento_id ON financeiro(orcamento_id);

-- ============================================================
-- TABELA: logs
-- ============================================================
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    acao TEXT NOT NULL,
    tabela TEXT NOT NULL,
    registro_id INTEGER,
    dados_anteriores TEXT,
    dados_novos TEXT,
    ip TEXT,
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE INDEX idx_logs_usuario_id ON logs(usuario_id);
CREATE INDEX idx_logs_data_hora ON logs(data_hora);
CREATE INDEX idx_logs_tabela ON logs(tabela);

-- ============================================================
-- Inserir dados padrão
-- ============================================================

-- Categorias padrão
INSERT INTO categorias_produto (nome, descricao, cor_hex, icone, ordem, ativo) VALUES
('Impressão', 'Serviços de impressão geral', '#3B82F6', 'printer', 1, 1),
('Recorte e Acabamento', 'Recorte, laminação, verniz', '#8B5CF6', 'scissors', 2, 1),
('Letreiro e Sinalização', 'Letreiros, placas, sinalização', '#F59E0B', 'zap', 3, 1),
('Fachadas e ACM', 'Painéis de fachada, ACM, dibond', '#10B981', 'building', 4, 1),
('Instalação', 'Serviços de instalação', '#EF4444', 'wrench', 5, 1),
('Arte e Projeto', 'Criação e design de arte', '#6366F1', 'pen-tool', 6, 1),
('Transporte e Frete', 'Transporte e frete', '#64748B', 'truck', 7, 1);

-- Unidades de medida padrão
INSERT INTO unidades_medida (sigla, descricao, tipo_calculo, permite_decimal, casas_decimais, ativo) VALUES
('m²', 'Metro Quadrado', 'area', 1, 4, 1),
('ml', 'Metro Linear', 'linear', 1, 2, 1),
('cm', 'Centímetro', 'linear', 1, 2, 1),
('hr', 'Hora', 'hora', 1, 2, 1),
('un', 'Unidade', 'unidade', 0, 0, 1),
('pç', 'Peça', 'unidade', 0, 0, 1),
('kit', 'Kit', 'unidade', 0, 0, 1),
('vb', 'Verba', 'verba', 0, 0, 1);
```

---

## 🔌 Endpoints REST (API)

### **1. AUTENTICAÇÃO**

```
POST   /api/auth/register          # Registro inicial (admin)
POST   /api/auth/login             # Login
POST   /api/auth/logout            # Logout
POST   /api/auth/refresh           # Refresh token
GET    /api/auth/me                # Dados do usuário logado
```

### **2. USUÁRIOS** (Admin)

```
GET    /api/usuarios               # Listar todos
POST   /api/usuarios               # Criar novo
GET    /api/usuarios/{id}          # Obter um
PUT    /api/usuarios/{id}          # Atualizar
DELETE /api/usuarios/{id}          # Deletar
PATCH  /api/usuarios/{id}/ativar   # Ativar/desativar
```

### **3. EMPRESA** (Admin/Gerente)

```
GET    /api/empresa                # Obter dados da empresa
PUT    /api/empresa                # Atualizar dados
POST   /api/empresa/logo           # Upload de logo (base64)
```

### **4. CLIENTES**

```
GET    /api/clientes               # Listar (filtros: ativo, tipo)
POST   /api/clientes               # Criar novo
GET    /api/clientes/{id}          # Obter um (com histórico)
PUT    /api/clientes/{id}          # Atualizar
DELETE /api/clientes/{id}          # Soft delete (marcar inativo)
GET    /api/clientes/search        # Buscar por nome/CPF/CNPJ
GET    /api/clientes/{id}/historico # Histórico de orçamentos
```

### **5. CATEGORIAS**

```
GET    /api/categorias             # Listar todas
POST   /api/categorias             # Criar (admin)
PUT    /api/categorias/{id}        # Atualizar (admin)
DELETE /api/categorias/{id}        # Deletar (admin)
```

### **6. UNIDADES DE MEDIDA**

```
GET    /api/unidades               # Listar todas
POST   /api/unidades               # Criar (admin)
PUT    /api/unidades/{id}          # Atualizar (admin)
DELETE /api/unidades/{id}          # Deletar (admin)
```

### **7. PRODUTOS**

```
GET    /api/produtos               # Listar (filtros: categoria, ativo)
POST   /api/produtos               # Criar (gerente/admin)
GET    /api/produtos/{id}          # Obter um
PUT    /api/produtos/{id}          # Atualizar (gerente/admin)
DELETE /api/produtos/{id}          # Soft delete
GET    /api/produtos/search        # Buscar por nome/código
GET    /api/produtos/categoria/{id} # Listar por categoria
```

### **8. ORÇAMENTOS**

```
GET    /api/orcamentos             # Listar (filtros: status, cliente, período)
POST   /api/orcamentos             # Criar rascunho
GET    /api/orcamentos/{id}        # Obter um com itens
PUT    /api/orcamentos/{id}        # Atualizar rascunho
POST   /api/orcamentos/{id}/enviar # Mudar status para 'enviado'
POST   /api/orcamentos/{id}/aprovar # Mudar status para 'aprovado'
POST   /api/orcamentos/{id}/cancelar # Cancelar com motivo
DELETE /api/orcamentos/{id}        # Deletar rascunho
GET    /api/orcamentos/{id}/pdf    # Gerar/baixar PDF
GET    /api/orcamentos/numero/{numero} # Buscar por número
GET    /api/orcamentos/token/{token} # Obter público (sem auth)
POST   /api/orcamentos/{id}/recalcular # Recalcular totais
```

### **9. ITENS DO ORÇAMENTO**

```
POST   /api/orcamentos/{id}/itens              # Adicionar item
GET    /api/orcamentos/{id}/itens             # Listar itens
PUT    /api/orcamentos/{id}/itens/{item_id}   # Atualizar item
DELETE /api/orcamentos/{id}/itens/{item_id}   # Remover item
POST   /api/orcamentos/{id}/itens/reordenar   # Reordenar (drag-drop)
```

### **10. ASSINATURAS DIGITAIS** (Públicas)

```
GET    /api/assinaturas/validar/{token}       # Verificar token válido
POST   /api/assinaturas/{token}               # Salvar assinatura + nome
GET    /api/assinaturas/{token}/status        # Verificar se já assinado
```

### **11. ORDENS DE SERVIÇO**

```
GET    /api/ordens                 # Listar (filtros: status, período)
POST   /api/ordens                 # Criar a partir de orçamento aprovado
GET    /api/ordens/{id}            # Obter uma ordem
PUT    /api/ordens/{id}            # Atualizar status/observações
GET    /api/ordens/orcamento/{id}  # Obter ordem de um orçamento
POST   /api/ordens/{id}/entregar   # Finalizar ordem
```

### **12. FINANCEIRO**

```
GET    /api/financeiro             # Listar (filtros: tipo, status, período)
POST   /api/financeiro             # Registrar transação
GET    /api/financeiro/{id}        # Obter uma
PUT    /api/financeiro/{id}        # Atualizar
DELETE /api/financeiro/{id}        # Deletar (pendentes)
POST   /api/financeiro/{id}/pagar  # Marcar como pago
GET    /api/financeiro/resumo      # Resumo mês (receita/despesa)
```

### **13. DASHBOARD**

```
GET    /api/dashboard/kpis         # KPIs principais (JSON)
GET    /api/dashboard/graficos     # Dados para gráficos
GET    /api/dashboard/alertas      # Orçamentos vencendo, OS atrasadas
```

### **14. RELATÓRIOS**

```
GET    /api/relatorios/vendas      # Relatório de vendas (período)
GET    /api/relatorios/clientes    # Relatório de clientes
GET    /api/relatorios/faturamento # Faturamento por período
GET    /api/relatorios/exportar    # Exportar para CSV/Excel
```

### **15. LOGS** (Admin)

```
GET    /api/logs                   # Listar logs
GET    /api/logs/usuario/{id}      # Logs de um usuário
GET    /api/logs/tabela/{tabela}   # Logs de uma tabela
```

---

## 🔐 Autenticação & Autorização

### **Headers padrão**
```
Authorization: Bearer {JWT_TOKEN}
Content-Type: application/json
```

### **Resposta de erro padrão**
```json
{
  "detail": "Erro descrição",
  "status": 400,
  "timestamp": "2026-05-01T10:30:00Z"
}
```

### **Token JWT**
```
Header: {"alg": "HS256", "typ": "JWT"}
Payload: {
  "sub": "usuario_id",
  "email": "email@empresa.com",
  "perfil": "admin",
  "iat": 1234567890,
  "exp": 1234571490  (8 horas)
}
```

---

## 📦 Configuração (.env)

```env
# Backend
FASTAPI_ENV=development
DEBUG=True
SECRET_KEY=sua_chave_secreta_super_complexa_aqui
DATABASE_URL=sqlite:///./database.db
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=8

# CORS
FRONTEND_URL=http://localhost:8000
ALLOWED_ORIGINS=http://localhost:8000,http://localhost:3000

# Servidor
HOST=0.0.0.0
PORT=8000
RELOAD=true

# Email (opcional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu_email@gmail.com
SMTP_PASSWORD=sua_senha_app

# IA (Anthropic)
ANTHROPIC_API_KEY=sk-xxx-yyy-zzz

# CEP
CEPAPI_URL=https://viacep.com.br/ws

# Logging
LOG_LEVEL=INFO
```

---

## 📋 requirements.txt

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
python-dotenv==1.0.0
requests==2.31.0
cors==1.0.1
email-validator==2.1.0
```

---

## 🚀 Como iniciar

### **Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
# API rodará em http://localhost:8000
# Docs: http://localhost:8000/docs
```

### **Frontend**
```bash
cd frontend
# Servir em um simples servidor HTTP
python -m http.server 8001
# Ou com Live Server (VS Code extension)
# Acesso em http://localhost:8001
```

---

## 📝 Próximos Passos

1. ✅ **Schema SQLite** — Pronto
2. ✅ **Endpoints REST** — Pronto
3. ✅ **Estrutura de pastas** — Pronto
4. ✅ **Configuração (.env)** — Pronto
5. ⏳ **Backend (models.py)** — Aguardando seu comando
6. ⏳ **Backend (routes)** — Aguardando seu comando
7. ⏳ **Frontend (HTML/CSS/JS)** — Aguardando seu comando

**Próximo passo: Deseja que eu gere os arquivos do Backend ou do Frontend primeiro?**

Comande:
- `GERAR BACKEND FASE 1` → database.py + models.py + schemas.py
- `GERAR BACKEND FASE 2` → auth routes + services
- `GERAR FRONTEND FASE 1` → login.html + setup + dashboard
