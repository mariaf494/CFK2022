#!/usr/bin/env bash
sudo docker exec streamlit_cfk2022 /bin/rm /home/app/utils/cleaners/bot/eliminados/*.xlsx
sudo docker exec streamlit_cfk2022 python3 /home/app/utils/cleaners/bot/update_xlsx.py
sudo docker cp streamlit_cfk2022:/home/app/utils/cleaners/bot/eliminados/*.xlsx /home/ubuntu/docker-compose/streamlit/CFK2022/utils/cleaners/bot/eliminados

cd ~/docker-compose/streamlit/CFK2022
git add .
git commit -m "Actualización"
git push origin master
