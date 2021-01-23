FROM alpine
RUN apk add python3 py3-pip
RUN pip3 install pyftpdlib pyopenssl requests
ADD ftp.py /bin/
RUN mkdir /ftp/
CMD python3 /bin/ftp.py 21
EXPOSE 21