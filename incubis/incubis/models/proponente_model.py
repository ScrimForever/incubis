from ..core.database import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class Proponente(Base):
    __tablename__ = "proponentes"
    proponente_id = Column(Integer, primary_key=True, index=True)
    proponente_nome = Column(String, unique=True, nullable=True)
    proponente_nome_negocio = Column(String, unique=True, nullable=True)
    proponente_cnpj = Column(String, unique=True, nullable=True)
    proponente_razao_social = Column(String, unique=True, nullable=True)
    # Foreign Keys
    # proponente_user = ForeignKey("users.user_id")
    
