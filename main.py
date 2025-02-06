from fastapi import FastAPI
from routes import blog_get_ops, blog_post_ops

app = FastAPI(
    title="My First FastAPI Training",
    description="Udemy FastAPI Training",
    version="1.0.0"
)
app.include_router(blog_get_ops.router)
app.include_router(blog_post_ops.router)

@app.get('/')
def index():
    return {'message': 'I am working'}
