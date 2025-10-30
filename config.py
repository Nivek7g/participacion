import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_segura'
    DATABASE = os.environ.get('DATABASE_URL', 'centrocap.db')