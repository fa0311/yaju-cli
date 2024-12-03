FROM node:22
WORKDIR /app

COPY ./dist/main.js /app/main.js

CMD ["node", "main.js"]