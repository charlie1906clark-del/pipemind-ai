FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv/pipemind
COPY pyproject.toml README.md ./
COPY src/ ./src/
COPY docs/ ./docs/
COPY research/ ./research/
COPY tools/ ./tools/
COPY web/ ./web/
RUN python -m pip install --no-cache-dir . && \
    useradd --system --create-home --uid 10001 pipemind && \
    mkdir -p /srv/pipemind/data && chown pipemind:pipemind /srv/pipemind/data
USER pipemind
EXPOSE 8080
ENV PIPEMIND_ENV=production PIPEMIND_DB_PATH=/srv/pipemind/data/pipemind.sqlite
CMD ["uvicorn","pipemind.api.app:app","--host","0.0.0.0","--port","8080","--workers","1"]
