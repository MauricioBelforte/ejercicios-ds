"""
Ejercicio 2 — Modelo Departamento

1. Crear un nuevo modelo `Departamento` (`id`, `nombre`).
2. Modificar el modelo `Profesor` para agregarle una clave foránea
   `departamento_id`.
3. Utilizar `relationship` en el modelo `Departamento` para acceder a la
   lista de sus profesores.

Insertar un par de registros de prueba y mostrarlos por consola.
"""


from pathlib import Path
from typing import List, Optional
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy.engine import create_engine

# 1. Base
class Base(DeclarativeBase):
    pass

# 2. Modelo Departamento (Lado Uno)
class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    # Relación para acceder a la lista de profesores OBJETOS desde un departamento 
    #CARDINALIDAD =(1,N) 
    # SIMILAR A UML CADA INSTANCIA DE DEPARTAMENTO PUEDE GUARDAR UNA LISTA CON MUCHOS PROFESORES
    profesores: Mapped[List["Profesor"]] = relationship(back_populates="departamento")

    def __repr__(self) -> str:
        return f"Departamento(id={self.id}, nombre='{self.nombre}')"

# 3. Modelo Profesor modificado (Lado Muchos)
class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # Clave Foránea apuntando a la TABLA departamentos 
    # CARDINALIDAD =(0,1)
    departamento_id: Mapped[Optional[int]] = mapped_column(ForeignKey("departamentos.id"))

    # Relación hacia Departamento OBJETO (Guarda la referencia al objeto Departamento)
    departamento: Mapped[Optional["Departamento"]] = relationship(back_populates="profesores")

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

        depto_programacion = Departamento(nombre="Programacion")
        depto_matematica = Departamento(nombre="Matemática")

        prof1 = Profesor(nombre="Marcos Aguirre", email="marcos@email.org", departamento=depto_programacion)
        prof2 = Profesor(nombre="Pepito Lopez", email="pepito@email.org", departamento=depto_programacion)
        prof3 = Profesor(nombre="Jorge Ramirez", email="jorge@email.org", departamento=depto_matematica)

        session.add_all([depto_programacion, depto_matematica, prof1, prof2, prof3])
        session.commit()

    # Consultar y mostrar por consola usando la relación
    with Session(engine) as session:
        departamentos = session.scalars(select(Departamento)).all()

        for depto in departamentos:
            print(f"Departamento: {depto.nombre}")
            for prof in depto.profesores:
                print(f"  └─ Profesor: {prof.nombre} ({prof.email})")