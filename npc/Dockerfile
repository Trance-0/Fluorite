FROM alpine:3.20
LABEL org.opencontainers.image.authors="trance-0@hotmail.com"

WORKDIR /

RUN set -x && \
	wget --no-check-certificate https://github.com/ehang-io/nps/releases/download/v0.26.10/linux_386_client.tar.gz && \ 
	mkdir \npc && \
	mv linux_386_client* /npc && \
	cd /npc && \
	tar xzf linux_386_client.tar.gz && \
	rm -rf *.tar.gz

ENV SERVERIP 127.0.0.1:8284
ENV VKEY 123

CMD /npc/npc -server=${SERVERIP} -vkey=${VKEY}