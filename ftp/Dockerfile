FROM python:3.7-alpine3.10
RUN pip3 install pyftpdlib
ADD ftp.py /bin/
RUN mkdir /ftp/
CMD python3 /bin/ftp.py 20121
EXPOSE 20121 5000-5100
