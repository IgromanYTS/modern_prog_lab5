FROM python:3.12.3-alpine3.18

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "test_calc.py"]
