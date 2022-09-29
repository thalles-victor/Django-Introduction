import asyncio
import json
from textwrap import indent
from urllib import response
from prisma import Prisma
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render


async def getInformation(request, id):
    db = Prisma()
    await db.connect()

    if request.method == 'GET':

        found = json.loads(
            (await db.post.find_unique(where={'id': id}))
            .json(indent=2)
        )

        response = found

        return JsonResponse(response)

    if request.method == 'POST':
        data = json.loads(
            request.body
        )

        post = await db.post.create(
            {
                'title': data['title'],
                'desc': data['description'],
                'published': data['published']
            }
        )

        response = json.loads((post).json(indent=2))

        return JsonResponse(
            response
        )

    await db.disconnect()
