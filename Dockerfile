FROM python:3.7

RUN pip install fastapi uvicorn mangum pydantic

EXPOSE 8080

COPY ./example_app /example_app

CMD ["uvicorn", "example_app.main:app", "--host", "0.0.0.0", "--port", "8080"]
