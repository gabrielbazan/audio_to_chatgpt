FROM ubuntu:22.04


ARG PROJECT_PACKAGE_NAME=audio_to_chatgpt

ARG WORK_DIR=/code
ARG REQUIREMENTS_FILENAME=requirements.frozen


WORKDIR ${WORK_DIR}


RUN apt update
RUN apt upgrade -y


RUN apt install ffmpeg python3.10 python3-pip -y


COPY ${REQUIREMENTS_FILENAME} .
RUN pip3 install -r ${REQUIREMENTS_FILENAME}


COPY ${PROJECT_PACKAGE_NAME} .


CMD python3.10 run.py
