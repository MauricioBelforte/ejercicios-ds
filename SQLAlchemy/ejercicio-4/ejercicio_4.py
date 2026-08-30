"""
Ejercicio 4 — Modelo Curso

Crear el modelo `Curso` (`id`, `titulo`, `creditos`).

Un profesor puede dictar muchos cursos, pero un curso es dictado por un único
profesor.

Añadir la clave foránea `profesor_id` en `Curso` y la relación correspondiente
en ambos modelos (`Profesor` y `Curso`).
"""

from pathlib import Path
from typing import List, Optional
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy.engine import create_engine

# 1. Base
class Base(DeclarativeBase):
    pass

# 2. Modelo Curso (Lado Uno)
class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(Integer)

    # Clave Foránea en el lado "Muchos" (Apunta a la TABLA profesores, un curso es dictado por un único profesor)
    profesor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("profesores.id"))

    # Relación hacia Profesor OBJETO (Guarda la referencia al profesor dictante)
    # Relación para acceder al OBJETO Profesor desde un curso
    # CARDINALIDAD =(0,1)
    # SIMILAR A UML CADA INSTANCIA DE CURSO PUEDE GUARDAR UN OBJETO PROFESOR
    profesor: Mapped[Optional["Profesor"]] = relationship(back_populates="cursos")


    def __repr__(self) -> str:
        return f"Curso(id={self.id}, titulo='{self.titulo}', creditos={self.creditos})"

# 3. Modelo Profesor modificado (Lado Muchos)
class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # CARDINALIDAD =(1,N)
    # Relación hacia Cursos (Un profesor puede tener una lista con muchos cursos)
    # Relación hacia Curso OBJETO (Guarda la referencia al objeto Curso)
    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")



    def __repr__(self) -> str:
        return f"Profesor(id={self.id}, nombre='{self.nombre}')"

# 4. Configuración de la Base de Datos (en la misma carpeta del script)
DIRECTORIO_ACTUAL = Path(__file__).parent
RUTA_DB = DIRECTORIO_ACTUAL / "universidad.db"

engine = create_engine(f"sqlite:///{RUTA_DB}", echo=False)
Base.metadata.create_all(engine)

# 5. Prueba de inserción y consulta
if __name__ == "__main__":

    # Consultar y mostrar por consola
    with Session(engine) as session:
        
        prof1 = Profesor(nombre="Marcos Aguirre", email="marcos@email.org")
        prof2 = Profesor(nombre="Pepito Lopez", email="pepito@email.org")
        prof3 = Profesor(nombre="Jorge Ramirez", email="jorge@email.org")

        curso_programacion = Curso(titulo="Programacion", creditos=3, profesor=prof1)
        curso_matematica = Curso(titulo="Matemática", creditos=4, profesor=prof2)
        curso_fisica = Curso(titulo="Física", creditos=5, profesor=prof3)


        session.add_all([curso_programacion, curso_matematica, curso_fisica, prof1, prof2, prof3])
        session.commit()

    # Consultar y mostrar por consola usando la relación en ambos sentidos
    with Session(engine) as session:
       
        # Sentido 1: De Profesor -> Cursos
        profesores = session.scalars(select(Profesor)).all()
        print("PROFESORES Y SUS CURSOS")
        for profe in profesores:
            print(f"👨‍🏫 Profesor: {profe.nombre}")
            for curso in profe.cursos:
                print(f"   └─ 📚 Curso: {curso.titulo} ({curso.creditos} crs.)")

        print("\n" + "="*40 + "\n")

        # Sentido 2: De Curso -> Profesor
        cursos = session.scalars(select(Curso)).all()
        print("CURSOS Y SU PROFESOR DICTANTE")
        for curso in cursos:
            nombre_profesor = curso.profesor.nombre if curso.profesor else "Sin Profesor"
            print(f"📚 Curso: {curso.titulo} | Dictado por: {nombre_profesor}")