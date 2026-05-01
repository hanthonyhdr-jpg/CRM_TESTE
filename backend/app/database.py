"""
Configuração do banco de dados SQLite com SQLAlchemy.
Gerencia conexões, sessions e inicialização do banco.
"""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.pool import StaticPool
from app.config import settings
import os
from pathlib import Path

# Base para todos os modelos
Base = declarative_base()

# Criar diretório se não existir
db_dir = Path(settings.database_url.replace("sqlite:///", "")).parent
db_dir.mkdir(parents=True, exist_ok=True)

# Configurar engine SQLite
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Necessário para SQLite em desenvolvimento
    echo=settings.debug  # Log de SQL em desenvolvimento
)

# Factory de sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """
    Habilita foreign keys no SQLite
    (Por padrão SQLite desabilita foreign keys)
    """
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def get_db() -> Session:
    """
    Dependency injection para FastAPI.
    Fornece uma sessão do banco em cada request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Cria todas as tabelas no banco de dados.
    Executar apenas uma vez no startup.
    """
    Base.metadata.create_all(bind=engine)
    print("✅ Banco de dados inicializado com sucesso!")


def drop_db():
    """
    Remove todas as tabelas do banco de dados.
    ⚠️ APENAS PARA DESENVOLVIMENTO!
    """
    print("⚠️ Deletando todas as tabelas...")
    Base.metadata.drop_all(bind=engine)
    print("✅ Banco de dados limpo!")


def seed_db():
    """
    Insere dados padrão no banco (categorias, unidades, etc).
    Executar após init_db().
    """
    from app.models import CategoriasProduto, UnidadesMedida
    
    db = SessionLocal()
    
    try:
        # Verificar se já existem categorias
        if db.query(CategoriasProduto).first():
            print("⚠️ Dados padrão já existem, pulando seed.")
            return
        
        # Inserir categorias padrão
        categorias = [
            CategoriasProduto(
                nome="Impressão",
                descricao="Serviços de impressão geral",
                cor_hex="#3B82F6",
                icone="printer",
                ordem=1,
                ativo=True
            ),
            CategoriasProduto(
                nome="Recorte e Acabamento",
                descricao="Recorte, laminação, verniz",
                cor_hex="#8B5CF6",
                icone="scissors",
                ordem=2,
                ativo=True
            ),
            CategoriasProduto(
                nome="Letreiro e Sinalização",
                descricao="Letreiros, placas, sinalização",
                cor_hex="#F59E0B",
                icone="zap",
                ordem=3,
                ativo=True
            ),
            CategoriasProduto(
                nome="Fachadas e ACM",
                descricao="Painéis de fachada, ACM, dibond",
                cor_hex="#10B981",
                icone="building",
                ordem=4,
                ativo=True
            ),
            CategoriasProduto(
                nome="Instalação",
                descricao="Serviços de instalação",
                cor_hex="#EF4444",
                icone="wrench",
                ordem=5,
                ativo=True
            ),
            CategoriasProduto(
                nome="Arte e Projeto",
                descricao="Criação e design de arte",
                cor_hex="#6366F1",
                icone="pen-tool",
                ordem=6,
                ativo=True
            ),
            CategoriasProduto(
                nome="Transporte e Frete",
                descricao="Transporte e frete",
                cor_hex="#64748B",
                icone="truck",
                ordem=7,
                ativo=True
            ),
        ]
        db.add_all(categorias)
        
        # Inserir unidades de medida padrão
        unidades = [
            UnidadesMedida(
                sigla="m²",
                descricao="Metro Quadrado",
                tipo_calculo="area",
                permite_decimal=True,
                casas_decimais=4,
                ativo=True
            ),
            UnidadesMedida(
                sigla="ml",
                descricao="Metro Linear",
                tipo_calculo="linear",
                permite_decimal=True,
                casas_decimais=2,
                ativo=True
            ),
            UnidadesMedida(
                sigla="cm",
                descricao="Centímetro",
                tipo_calculo="linear",
                permite_decimal=True,
                casas_decimais=2,
                ativo=True
            ),
            UnidadesMedida(
                sigla="hr",
                descricao="Hora",
                tipo_calculo="hora",
                permite_decimal=True,
                casas_decimais=2,
                ativo=True
            ),
            UnidadesMedida(
                sigla="un",
                descricao="Unidade",
                tipo_calculo="unidade",
                permite_decimal=False,
                casas_decimais=0,
                ativo=True
            ),
            UnidadesMedida(
                sigla="pç",
                descricao="Peça",
                tipo_calculo="unidade",
                permite_decimal=False,
                casas_decimais=0,
                ativo=True
            ),
            UnidadesMedida(
                sigla="kit",
                descricao="Kit",
                tipo_calculo="unidade",
                permite_decimal=False,
                casas_decimais=0,
                ativo=True
            ),
            UnidadesMedida(
                sigla="vb",
                descricao="Verba",
                tipo_calculo="verba",
                permite_decimal=False,
                casas_decimais=0,
                ativo=True
            ),
        ]
        db.add_all(unidades)
        
        db.commit()
        print("✅ Dados padrão inseridos com sucesso!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inserir dados padrão: {str(e)}")
    finally:
        db.close()
