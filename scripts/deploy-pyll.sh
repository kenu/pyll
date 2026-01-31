. ~/.bash_profile
cd ~/git/pyll
git pull origin main
docker compose down
docker compose up --build -d
