// PM2 Ecosystem Config — Nexus Protocol
// Manages all Node.js services as a process cluster.
//
// Install PM2:  npm install -g pm2
// Start all:    pm2 start ecosystem.config.js
// Save state:   pm2 save
// Auto-start:   pm2 startup  (follow printed command)
// Status:       pm2 status
// Logs:         pm2 logs
// Stop all:     pm2 stop all

module.exports = {
  apps: [
    {
      name:        "nexus-dashboard",
      script:      "./server.js",
      instances:   1,
      autorestart: true,
      watch:       false,
      max_memory_restart: "256M",
      env: {
        NODE_ENV:    "production",
        NEXUS_ENV:   "remote",
        PORT:        process.env.PORT || 3000,
      },
    },
    {
      name:        "nexus-approval",
      script:      "./approval-service-server.js",
      instances:   1,
      autorestart: true,
      watch:       false,
      env: {
        NEXUS_ENV:            "remote",
        APPROVAL_SERVICE_PORT: process.env.APPROVAL_SERVICE_PORT || 8787,
      },
    },
    {
      name:        "nexus-financial",
      script:      "./financial-ops-rest-server.js",
      instances:   1,
      autorestart: true,
      watch:       false,
      env: {
        NEXUS_ENV:              "remote",
        FINANCIAL_OPS_REST_PORT: process.env.FINANCIAL_OPS_REST_PORT || 8788,
      },
    },
    {
      name:        "nexus-signal-bus",
      script:      "./nexus-signal-bus.js",
      instances:   1,
      autorestart: true,
      watch:       false,
      env: {
        NEXUS_ENV:             "remote",
        NEXUS_SIGNAL_BUS_PORT: process.env.NEXUS_SIGNAL_BUS_PORT || 8790,
      },
    },
  ],
};
