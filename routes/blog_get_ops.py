from routes import blog_post_ops
from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

# @router.get('/blogs/all')
# def get_all_blogs():
#     return {'message': 'Retrieved all blogs'}

# Query Params

@router.get('/all', 
         summary = "Retrieve all blogs", 
         description = "The api call simulates fetching all blogs.", 
         response_description = "The list of available blogs"
         )
def get_all_blogs(page: int = 1, page_size: Optional[int] = None, required_param: dict = Depends(blog_post_ops.required_functionality)):
    return {'message': f'All {page_size} blogs on page {page} retireved', 'req': required_param}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}', tags=['blogs', 'type'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

# multi query params 
@router.get('/{id}/comments/{comment_id}', tags=['comments'])
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

@router.get('/{id}', status_code = status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog with id {id} retrieved successfully'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id} retrieved successfully'}
    
