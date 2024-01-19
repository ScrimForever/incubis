from ..core.database import Base
from sqlalchemy import Integer, String, ForeignKey, Column, Text


class Integrante(Base):
    __tablename__ = "integrante"
    integrante_id = Column(Integer, primary_key=True, index=True)
    integrante_nome = Column(String, unique=True)
    integrante_experiencia = Column(Text, nullable=True)

    # Foreign Keys
    equipe_fk = ForeignKey("equipe.equipe_id")
    formacao_academica_fk = ForeignKey("formacao_academica.formacao_academica_id")

    def __str__(self):
        return self.integrante_nome