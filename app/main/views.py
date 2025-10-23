from django.shortcuts import render

# apps/views.py
from django.http import JsonResponse
from postgres.database import get_db
from postgres.models import Test

def get_users(request):
    db = next(get_db())
    users = db.query(Test).all()
    users_data = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        for user in users
    ]
    return JsonResponse(users_data, safe=False)

def create_user(request):
    if request.method == 'POST':
        db = next(get_db())
        user = Test(
            email=request.POST.get('email'),
            name=request.POST.get('name'),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return JsonResponse({'id': user.id, 'message': 'User created'})
