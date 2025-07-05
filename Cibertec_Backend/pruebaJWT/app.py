from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import JWTError, jwt
from datetime import datetime, timedelta

# App config
app = FastAPI()
SECRET_KEY = "mi_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

# Usuario simulado
db_estudiante = {
    "admin": {
        "username": "admin",
        "email": "calranderr@gmail.com",
        "password": "12345"
    },
    "Alexader": {
        "username": "admin1",
        "email": "calranderr@gmail.com",
        "password": "12345"
    }
}

# Esquema OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para crear el token


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Función para obtener usuario desde el token


def decode_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None or username not in db_estudiante:
            raise HTTPException(status_code=401, detail="Token inválido")
        return db_estudiante[username]
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Ruta para obtener el token


@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = db_estudiante.get(form_data.username)

    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña incorrectos")

    access_token = create_access_token(
        data={"username": user["username"]}
    )
    return {"access_token": access_token,  "token_type": f"bearer"}


@app.get("/estudiante")
def get_profile(current_user: Annotated[dict, Depends(decode_token)]):
    return db_estudiante
# @app.get("/estudiante/{token}")
# def get_profile(token: str):
#     try:
#         current_user = decode_token(token)
#         return current_user
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail="Error interno del servidor")
