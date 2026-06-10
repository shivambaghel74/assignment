FROM python:3.11-slim

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

COPY cli/list_profiles.py \
/usr/local/bin/list-profiles

COPY etc/default/model_manifest.yaml \
/opt/app/etc/default/model_manifest.yaml

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN chmod +x /usr/local/bin/list-profiles

RUN useradd -m appuser

USER appuser

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
