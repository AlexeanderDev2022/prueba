
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from utils.response_handler import handle_exception
from routes.estudiante import documento as reg_estudinate
from fastapi.middleware.cors import CORSMiddleware


from starlette.exceptions import HTTPException as StarletteHTTPException
# import threading
# from events.event_listener import listen_for_events

app = FastAPI()
origins = [
    "*"
    # Another example origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(reg_estudinate)
# Iniciar el listener de eventos en segundo plano
# event_thread = threading.Thread(target=listen_for_events, daemon=True)
# event_thread.start()

# Manejador global para errores de validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return handle_exception(exc)

# Manejador global para errores HTTP


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return handle_exception(exc)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Seguridad"}
