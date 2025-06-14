# PowerShell script to build all Docker images

Write-Host "Building ddos-server..."
Push-Location ./server
docker build -t ddos-server .
Pop-Location

Write-Host "Building ddos-attacker..."
Push-Location ./attacker
docker build -t ddos-attacker .
Pop-Location

Write-Host "Building ddos-botnet..."
Push-Location ./botnet
docker build -t ddos-botnet .
Pop-Location

Write-Host "√ All images built successfully."
