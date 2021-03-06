# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()