from ..core.database import Base
from sqlalchemy import Integer, String, Column


class FormacaoAcademica(Base):
    __tablename__ = "formacao_academica"
    formacao_academica_id = Column(Integer, primary_key=True, index=True)
    formacao_academica_nome = Column(String, unique=True)
    formacao_academica_descricao = Column(String, unique=True, nullable=True)

    def __str__(self):
        return self.formacao_academica_nome