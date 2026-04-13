#!/usr/bin/env pwsh
# Windows PowerShell Build Script for Deployment

Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Collecting static files..." -ForegroundColor Green
python manage.py collectstatic --noinput

Write-Host "Running migrations..." -ForegroundColor Green
python manage.py migrate

Write-Host "Build completed successfully!" -ForegroundColor Green
