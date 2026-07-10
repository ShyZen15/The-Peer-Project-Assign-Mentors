from fastapi import FastAPI


from App.api.mentor import router as mentor_router
from App.api.mentee import router as mentee_router
from App.api.assignment import router as assignment_router
from App.api.admin import router as admin_router
from fastapi.middleware.cors import CORSMiddleware

# Initial Setup
app = FastAPI(
    title="Peer Project Backend",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router Registration
app.include_router(mentor_router)
app.include_router(mentee_router)
app.include_router(assignment_router)
app.include_router(admin_router)

@app.get("/")
async def root():
    return {
            "message": 'Hello World',
            "Status": 'Running'
        }