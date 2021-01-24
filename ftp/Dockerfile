FROM python:3.7-alpine 
RUN pip3 install pyftpdlib
ADD ftp.py /bin/
RUN mkdir /ftp/
CMD python3 /bin/ftp.py 201921
EXPOSE 201921 5000-5100
