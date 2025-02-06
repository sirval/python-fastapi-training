from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

router = APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'},
    imgae: Optional[Image] = None
    

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int =1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }
    
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
                   comment_title: int = Query(None, 
                                           title= 'Title of the comment', 
                                           description= 'Query description',
                                           alias= 'commentTitle',
                                           deprecated=True
                                           ),
                   content: str = Body(..., min_length=10, max_length=11, regex="^[a-z\s]*$"),
                   v: Optional[List[str]] = Query(['1', '2', '3']), #Query(None)
                   comment_id: int = Path(..., gt=5, le=10)
                   ):
    return {
        'id': id,
        'blog': blog,
        'comment_title': comment_title,
        'content': content,
        'version': v
    }
    
def required_functionality():
    return {"message": "Dependency functionality"}