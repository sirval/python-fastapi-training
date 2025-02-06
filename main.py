from fastapi import FastAPI
from routes import blog_get_ops, blog_post_ops

app = FastAPI()
app.include_router(blog_get_ops.router)
app.include_router(blog_post_ops.router)

@app.get('/')
def index():
    return {'message': 'I am working'}
