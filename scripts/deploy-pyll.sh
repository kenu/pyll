. ~/.bash_profile
cd ~/git/pyll
git pull origin main
docker compose down
docker compose up --build -d
curl -X POST -H 'Content-type: application/json' --data '{"content":"⏱️ Deploy Job Finished!\nhttps://justdev.net/"}' $DISCORD_WEBHOOK
