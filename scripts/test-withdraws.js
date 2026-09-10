// test-withdraws.js — Quick diagnostic for /withdraws API
const fetch = require("node-fetch");

async function testWithdraws() {
  try {
    const res = await fetch("http://localhost:8789/withdraws");
    const data = await res.json();
    console.log("✅ /withdraws API responded successfully:\n");
    console.log(JSON.stringify(data, null, 2));
  } catch (err) {
    console.error("❌ Error connecting to /withdraws API:", err.message);
  }
}

testWithdraws();
