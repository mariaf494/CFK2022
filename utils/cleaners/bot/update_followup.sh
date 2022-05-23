#!/usr/bin/env bash
python3 ~/docker-compose/streamlit/CFK2022/utils/cleaners/bot/update_xlsx.py

cd ~/mariana
./gdrive sync upload ~/docker-compose/streamlit/CFK2022/data/descargables/ 10-vecqL2rtGRXkZ4H6xkI4DY1Z5wr7fw
./gdrive sync upload ~/docker-compose/streamlit/CFK2022/utils/cleaners/bot/eliminados 1xaulGr1dAuJqx2AwtGRKCcRhm9jQZCUP

#cd ~/docker-compose/streamlit/CFK2022
#git add .
#git commit -m "Actualización"
#git push origin master
