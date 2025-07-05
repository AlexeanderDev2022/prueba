CREATE TABLE
    "Estudiante" (
        id_estudiante SERIAL PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        dni VARCHAR(8),
        email VARCHAR(120),
        estado VARCHAR(30)
    );

CREATE TABLE
    "Profesor" (
        id_profesor SERIAL PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        dni VARCHAR(8),
        email VARCHAR(120)
    );

CREATE TABLE
    "Curso" (
        id_curso SERIAL PRIMARY KEY,
        nombre VARCHAR(120),
        descripcion VARCHAR(50),
        id_profesor INTEGER REFERENCES "Profesor" (id_profesor)
    );

CREATE TABLE
    "Estudiante_Curso" (
        id_estudiante_cur SERIAL PRIMARY key,
        id_estudiante INTEGER REFERENCES "Estudiante" (id_estudiante),
        id_curso INTEGER REFERENCES "Curso" (id_curso)
    );

CREATE TABLE
    "Asistencia" (
        id_asistencia SERIAL PRIMARY KEY,
        id_estudiante_cur INTEGER REFERENCES "Estudiante_Curso" (id_estudiante),
        fecha date not null,
        estado VARCHAR(30) REFERENCES "Estudiante" (estado)
    );
    CREATE table "Registrar"(
        Id_registro SERIAL PRIMARY KEY,
        nombre VARCHAR(50),
        email VARCHAR(150),
        descripcion VARCHAR(300)

    )