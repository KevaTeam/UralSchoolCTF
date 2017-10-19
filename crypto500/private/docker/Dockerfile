FROM hardbyte/python3

RUN mkdir /service
COPY service /service
WORKDIR /service

EXPOSE 9999

CMD ["./service.py", "", "9999"]
