FROM node:22-alpine
WORKDIR /app

COPY ./dist/main.js /app/main.js

CMD ["node", "main.js"]