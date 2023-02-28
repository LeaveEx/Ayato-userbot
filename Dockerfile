FROM python:3.9.7-slim-buster

RUN git clone -b main https://github.com/LeaveEx/Ayato-userbot /home/Ayato/
WORKDIR /home/Ayato

RUN wget https://raw.githubusercontent.com/LeaveEx/Ayato-userbot/main/requirements.txt \
    && pip3 install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt \
    && rm requirements.txt
CMD bash start
