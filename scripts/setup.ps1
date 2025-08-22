# OrchestrateX Setup Script for Windows
Write-Host "🚀 Setting up OrchestrateX Conference Planning Platform..." -ForegroundColor Green

# Check if Node.js is installed
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js is not installed. Please install Node.js 18+ first." -ForegroundColor Red
    exit 1
}

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed. Please install Python 3.11+ first." -ForegroundColor Red
    exit 1
}

# Check if pip is installed
try {
    $pipVersion = pip --version
    Write-Host "✅ pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ pip is not installed. Please install pip first." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Prerequisites check passed" -ForegroundColor Green

# Install root dependencies
Write-Host "📦 Installing root dependencies..." -ForegroundColor Yellow
npm install

# Install frontend dependencies
Write-Host "📦 Installing frontend dependencies..." -ForegroundColor Yellow
Set-Location frontend
npm install
Set-Location ..

# Install backend dependencies
Write-Host "📦 Installing backend dependencies..." -ForegroundColor Yellow
Set-Location backend
pip install -r requirements.txt
Set-Location ..

# Create environment files if they don't exist
Write-Host "🔧 Setting up environment files..." -ForegroundColor Yellow

if (-not (Test-Path "frontend/.env.local")) {
    Copy-Item "frontend/env.example" "frontend/.env.local"
    Write-Host "✅ Created frontend/.env.local (please edit with your values)" -ForegroundColor Green
}

if (-not (Test-Path "backend/.env")) {
    Copy-Item "backend/env.example" "backend/.env"
    Write-Host "✅ Created backend/.env (please edit with your values)" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Edit frontend/.env.local with your frontend configuration" -ForegroundColor White
Write-Host "2. Edit backend/.env with your backend configuration" -ForegroundColor White
Write-Host "3. Start the development servers with: npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "Frontend will be available at: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Backend will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API documentation will be available at: http://localhost:8000/docs" -ForegroundColor Cyan
