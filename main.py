from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'I am working'}

# @app.get('/blogs/all')
# def get_all_blogs():
#     return {'message': 'Retrieved all blogs'}

# Query Params

@app.get('/blogs/all', 
         tags=['blogs'], 
         summary = "Retrieve all blogs", 
         description = "The api call simulates fetching all blogs.", 
         response_description = "The list of available blogs"
         )
def get_all_blogs(page: int = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page} retireved'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}', tags=['blogs', 'type'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

# multi query params 
@app.get('/blog/{id}/comments/{comment_id}', tags=['blogs', 'comments'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog.

    **Parameters:**

    - **id**: Mandatory path parameter.
    - **comment_id**: Mandatory path parameter.
    - **valid** (bool, optional): Optional query parameter. Defaults to True.
    - **username** (Optional[str], optional): Optional query parameter. Defaults to None.
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

@app.get('/blog/{id}', status_code = status.HTTP_200_OK, tags=['blogs'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog with id {id} retrieved successfully'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id} retrieved successfully'}