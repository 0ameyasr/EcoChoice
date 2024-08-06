FROM python AS base
WORKDIR /app
COPY Model_APIs/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS final
WORKDIR /app
COPY Model /app/Model
COPY Model_APIs /app/Model_APIs
ENV FLASK_APP=Model_APIs/ecf_classifier.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]