"""
Ejercicio 1 — Modelo Profesor

Crear el archivo de configuración de la base de datos (puede ser SQLite en
memoria o archivo) y definir el primer modelo `Profesor` con los campos:
`id`, `nombre`, `email` y `fecha_ingreso` (Ver `DateTime`).

Insertar un par de registros de prueba y mostrarlos por consola.
"""
from datetime import datetime
from sqlalchemy import String, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.engine import create_engine

# 1. Definimos la clase base de la cual heredan todos los modelos
class Base(DeclarativeBase):
    pass

# 2. Definimos el modelo Profesor
class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    # DateTime con valor por defecto de la fecha/hora actual
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Profesor(id={self.id}, nombre='{self.nombre}', email='{self.email}')"

# 3. Creamos el engine (usamos archivo 'universidad.db')
# Para que sea en memoria, cambiar la URL a: "sqlite:///:memory:"
engine = create_engine("sqlite:///universidad.db", echo=False)

# Creamos las tablas en la base de datos
Base.metadata.create_all(engine)


# 4. Insertar registros de prueba y mostrarlos
if __name__ == "__main__":
    with Session(engine) as session:
        # Creamos un par de objetos de prueba
        prof1 = Profesor(nombre="Juancito", email="juancito@example.com")
        prof2 = Profesor(nombre="Pepito", email="pepito@example.com")

        # Los agregamos a la sesión y guardamos en la base de datos
        session.add_all([prof1, prof2])
        session.commit()
        print("✅ Registros insertados correctamente.\n")

    # Abrimos una nueva sesión para consultar y verificar
    with Session(engine) as session:
        # Construimos la consulta para traer todos los profesores
        stmt = select(Profesor)
        profesores = session.scalars(stmt).all()

        print("Lista de Profesores en la Base de Datos")
        for prof in profesores:
            print(f"ID: {prof.id} | Nombre: {prof.nombre} | Email: {prof.email} | Fecha Ingreso: {prof.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S')}")


