"""
Ejercicio 5 — Modelo Clase (One-to-Many)

Crea el modelo `Clase` (`id`, `tema`, `duracion_minutos`).

Un curso se compone de muchas clases.

Configurar la relación One-to-Many entre `Curso` y `Clase`.

Escribir una consulta que devuelva todas las clases de un curso específico a
través del ORM.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional
from sqlalchemy import DateTime, ForeignKey, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy.engine import create_engine


# 1. Base
class Base(DeclarativeBase):
    pass


class Profesor(Base):
    """Modelo de un profesor."""

    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # CARDINALIDAD =(1,N)
    cursos: Mapped[list["Curso"]] = relationship(back_populates="profesor")

    def __repr__(self) -> str:
        return f"Profesor(id={self.id}, nombre='{self.nombre}')"


class Curso(Base):
    """Modelo de un curso."""

    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(Integer)
    profesor_id : Mapped[Optional[int]] = mapped_column(ForeignKey("profesores.id"))

    # Relación hacia Profesor
    profesor: Mapped[Optional["Profesor"]] = relationship("Profesor", back_populates="cursos")

    # Un curso tiene muchas clases (One-to-Many)
    # CARDINALIDAD =(1,N)
    clases: Mapped[list["Clase"]] = relationship("Clase", back_populates="curso")


class Clase(Base):
    """Modelo de una clase."""

    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150))
    duracion_minutos: Mapped[int] = mapped_column(Integer)

    # CARDINALIDAD =(0,1)
    curso_id : Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    curso: Mapped[Optional["Curso"]] = relationship("Curso", back_populates="clases")

# 4. Configuración de la Base de Datos (en la misma carpeta del script)
DIRECTORIO_ACTUAL = Path(__file__).parent
RUTA_DB = DIRECTORIO_ACTUAL / "universidad.db"

engine = create_engine(f"sqlite:///{RUTA_DB}", echo=False)
Base.metadata.create_all(engine)

# 6. Prueba de inserción y consulta específica
if __name__ == "__main__":

    with Session(engine) as session:
        # Creamos el profesor y el curso
        prof_marcos = Profesor(nombre="Marcos Aguirre", email="marcos@email.org")
        
        curso_programacion = Curso(titulo="Programación I", creditos=5, profesor=prof_marcos)

        # Creamos varias clases asociadas directamente al objeto curso
        clase1 = Clase(tema="Introducción a Python y Variables", duracion_minutos=90, curso=curso_programacion)
        clase2 = Clase(tema="Estructuras de Control ", duracion_minutos=120, curso=curso_programacion)
        clase3 = Clase(tema="Funciones y Módulos", duracion_minutos=90, curso=curso_programacion)

        # También podemos agregar clases asignando a la lista del curso directamente:
        curso_matematica = Curso(titulo="Matemática", creditos=4)
        curso_matematica.clases.append(Clase(tema="Álgebra", duracion_minutos=60))

        session.add_all([prof_marcos, curso_programacion, curso_matematica, clase1, clase2, clase3])
        session.commit()

    # Consulta: Obtener las clases de un curso específico a través del ORM
    with Session(engine) as session:
        # Buscamos el curso por su nombre o id
        stmt = select(Curso).where(Curso.titulo == "Programación I")
        curso = session.scalars(stmt).first()

        if curso:
            print(f"📖 Clases del curso '{curso.titulo}' (Dictado por: {curso.profesor.nombre}):")
            print("=" * 60)
            
            # Acceso directo a las clases a través de la propiedad de relación
            for clase in curso.clases:
                print(f" └─ 📝 Tema: {clase.tema} | Duración: {clase.duracion_minutos} min")
        else:
            print("No se encontró el curso especificado.")