"""
Ejercicio 7 — Many-to-Many enriquecida

Transformar la tabla asociativa anterior para añadir los atributos
`fecha_inscripcion` y `calificacion_final`.

Modificar las relaciones en `Estudiante` y `Curso` utilizando `secondary` o
mapeo directo para mantener la relación Many-to-Many enriquecida.
"""


from datetime import datetime
from pathlib import Path
from typing import Optional , List
from sqlalchemy import DateTime, ForeignKey, Integer, String, select, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy.engine import create_engine


# Base
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
    # CARDINALIDAD =(0,1)
    profesor: Mapped[Optional["Profesor"]] = relationship("Profesor", back_populates="cursos")

    # Un curso tiene muchas clases (One-to-Many)
    # CARDINALIDAD =(1,N)
    clases: Mapped[list["Clase"]] = relationship("Clase", back_populates="curso")

    # Relación hacia la tabla de asociación
    # CARDINALIDAD =(0,N)
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso", cascade="all, delete-orphan")

class Inscripcion(Base):
    __tablename__ = "inscripciones"

    # Claves foráneas que componen la relación
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)

    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    calificacion_final: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    # Relaciones inversas hacia las entidades principales
    # CARDINALIDAD =(1,1)
    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    # CARDINALIDAD =(1,1)
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")

    def __repr__(self) -> str:
        return f"Inscripcion(estudiante_id={self.estudiante_id}, curso_id={self.curso_id})"

    
class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[str] = mapped_column(String(20), unique=True)

    # Relación hacia la tabla de asociación
    # CARDINALIDAD =(0,N)
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Estudiante(id={self.id}, nombre='{self.nombre}', legajo='{self.legajo}')"

    
class Clase(Base):
    """Modelo de una clase."""

    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150))
    duracion_minutos: Mapped[int] = mapped_column(Integer)

    # CARDINALIDAD =(1,1)
    curso_id : Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    curso: Mapped["Curso"] = relationship("Curso", back_populates="clases")

#  Configuración de la Base de Datos (en la misma carpeta del script)
DIRECTORIO_ACTUAL = Path(__file__).parent
RUTA_DB = DIRECTORIO_ACTUAL / "universidad.db"

engine = create_engine(f"sqlite:///{RUTA_DB}", echo=False)
Base.metadata.create_all(engine)

if __name__ == "__main__":

    with Session(engine) as session:
        # Creamos cursos
        curso_programacion = Curso(titulo="Programación I", creditos=5)
        curso_matematica = Curso(titulo="Matemática", creditos=4)
        curso_fisica = Curso(titulo="Física", creditos=5)

        # Creamos estudiantes
        estudiante_ana = Estudiante(nombre="Ana García", legajo="INF-101")
        estudiante_juan = Estudiante(nombre="Juan Pérez", legajo="INF-102")
        estudiante_lucia = Estudiante(nombre="Lucía Gómez", legajo="INF-103")

        # Inscribimos alumnos en diferentes cursos mediante el objeto Inscripcion
        inscripcion_1 = Inscripcion(estudiante=estudiante_ana, curso=curso_programacion, calificacion_final=9.5, fecha_inscripcion=datetime(2025, 3, 15))
        inscripcion_2 = Inscripcion(estudiante=estudiante_ana, curso=curso_matematica, calificacion_final=8.0, fecha_inscripcion=datetime(2024, 3, 16))
        inscripcion_3 = Inscripcion(estudiante=estudiante_juan, curso=curso_programacion, calificacion_final=7.5, fecha_inscripcion=datetime(2026, 3, 17))
        inscripcion_4 = Inscripcion(estudiante=estudiante_lucia, curso=curso_fisica, calificacion_final=9.0, fecha_inscripcion=datetime(2024, 3, 18))
        inscripcion_5 = Inscripcion(estudiante=estudiante_lucia, curso=curso_programacion, calificacion_final=8.5, fecha_inscripcion=datetime(2024, 3, 19))

        session.add_all([curso_programacion, curso_matematica, curso_fisica, estudiante_ana, estudiante_juan, estudiante_lucia, inscripcion_1, inscripcion_2, inscripcion_3, inscripcion_4, inscripcion_5])
        session.commit()

    # --- CONSULTA 1: Cursos de una estudiante específica ---
    with Session(engine) as session:
        stmt = select(Estudiante).where(Estudiante.nombre == "Ana García")
        estudiante = session.scalars(stmt).first()

        if estudiante:
            print(f"🎓 Cursos en los que está inscripta {estudiante.nombre} (Legajo: {estudiante.legajo}):")
            for inscripcion in estudiante.inscripciones:
                print(f" └─ 📚 {inscripcion.curso.titulo} ({inscripcion.curso.creditos} crs.) -- Nota: {inscripcion.calificacion_final}")

    print("\n" + "=" * 50 + "\n")

    # --- CONSULTA 2: Estudiantes inscriptos en un curso específico ---
    with Session(engine) as session:
        stmt = select(Curso).where(Curso.titulo == "Programación I")
        curso = session.scalars(stmt).first()

        if curso:
            print(f"👥 Estudiantes inscriptos en '{curso.titulo}':")
            for inscripcion in curso.inscripciones:
                print(f" └─ 👤 {inscripcion.estudiante.nombre} (Legajo: {inscripcion.estudiante.legajo}) -- Nota: {inscripcion.calificacion_final}")