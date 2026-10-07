# Nexus Protocol — Dockerfile
FROM node:20-alpine

WORKDIR /app

# Install dependencies first (cache layer)
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# Copy application files
COPY server.js nexus-config.js nexus-signal-bus.js \
     approval-service-server.js financial-ops-rest-server.js \
     .approval-service-state.json* ./

COPY scripts/ ./scripts/
COPY nexus/    ./nexus/
COPY *.html    ./

EXPOSE 3000 8787 8788 8789 8790

ENV NODE_ENV=production \
    NEXUS_ENV=remote \
    PORT=3000

CMD ["node", "server.js"]
