#!/usr/bin/env bash
sudo docker exec streamlit_cfk2022 python3 /home/app/utils/cleaners/bot/update_xlsx.py
cd ~/docker-compose/streamlit/CFK2022
git add .
git commit -m "Actualización"
git push origin master
