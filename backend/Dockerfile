FROM python:3.7-buster

COPY . /main

WORKDIR /main

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

EXPOSE 8601

CMD ["run.py"]
