# from dependencies import initialize_db, create_superuser, required_folders
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Depends
from routers import core, cars


tags_metadata = [
    {
        "name": "Authentication",
        "description": "You can perform the authentication process using the APIs of this section.",
    },
    {
        "name": "Core",
        "description": "Using the APIs of this section, you can receive comments and also provide a new analysis.",
    },
]

description = """
<img src="/static/images/sm2.png" width="300" alt="Logo">
<h2>Cost Logestic</h2>

<p>Take the cost of sending your goods.</p>
"""

app = FastAPI(
    # openapi_tags=tags_metadata,
    title="Cost Logestic",
    description=description,
    version="0.0.1",
    docs_url="/",
    # dependencies=[
    #     Depends(initialize_db),
    #     Depends(create_superuser),
    #     Depends(required_folders)
    # ]
)

# app.include_router(auth.router, tags=['Authentication'])
app.include_router(core.router, tags=['Products'])
app.include_router(cars.router, tags=['Cars'])

app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/templates", StaticFiles(directory="templates"), name="templates")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.on_event("startup")
# async def startup_event():
#     initialize_db()
#     create_superuser()
#     required_folders()
