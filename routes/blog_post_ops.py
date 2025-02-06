from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int =1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }
    
@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
                   comment_id: int = Query(None, 
                                           title= 'Id of the comment', 
                                           description= 'Query description',
                                           alias= 'commentId',
                                           deprecated=True
                                           ),
                   content: str = Body(...)
                   ):
    return {
        'id': id,
        'blog': blog,
        'comment_id': comment_id
    }