const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Serve dashboard
app.use("/web", express.static(path.join(__dirname, "web")));

// Attach your withdraws API
app.use("/withdraws", require("./scripts/withdraws"));

// Health check
app.get("/", (req, res) => {
  res.send("Nexus Builder Fund API is running");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
