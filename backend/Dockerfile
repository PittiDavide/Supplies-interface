FROM node:19 as svelte_builder

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY frontend .

RUN npm run build

FROM python:3.11.3-buster

RUN apt-get update && apt-get upgrade -y 

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install -r requirements.txt

COPY backend .

COPY --from=svelte_builder /app/public /app/static

CMD ["sh", "run-server.sh"]