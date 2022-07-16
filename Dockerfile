FROM xnkitk/ankit:buster

RUN git clone -b AnKiT https://github.com/XnKiTK/AnKiT /home/ankit/ \
    && chmod 777 /home/ankit \
    && mkdir /home/ankit/bin/

WORKDIR /home/ankit/

CMD [ "bash", "start" ]
