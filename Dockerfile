FROM python:3.12-alpine

# Define build-time arguments for UID and GID
ARG UID=1000
ARG GID=1000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user with specific UID and GID
RUN addgroup -g ${GID} prod && \
    adduser -u ${UID} -G prod -s /bin/sh -D prod

WORKDIR /app

COPY --chown=${UID}:${GID} requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY --chown=${UID}:${GID} docker/ docker/
COPY --chown=${UID}:${GID} survey_backend/ survey_backend/
