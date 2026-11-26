from fastapi import FastAPI

app = FastAPI(
    title = "LifePilot API",
    description  = "AI-Powered everyday assistance platform",
    version = "1.0.0"
)

@app.get("/")
def home():
    return{
        "message" : "Welocome to LifePilot API",
        "status" : "Running"
    }
    
@app.get("/health")
def health_check():
    return{
        "status" : "healthy"
    }