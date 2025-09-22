FROM python:3.12.11-slim
ENV TOKEN='8060085500:AAGylmIDeZq4kdLDtIFAdjDeBZ2ZQ9VOwPY'
WORKDIR /app
COPY /requirements.txt /app/requirements.txt
COPY /bot.py /app/bot.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]