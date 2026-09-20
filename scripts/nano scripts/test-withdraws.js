const fetch = require("node-fetch");

(async () => {
  try {
    const res = await fetch("http://localhost:8789/withdraws");
    const data = await res.json();
    console.log(JSON.stringify(data, null, 2));
  } catch (err) {
    console.error("Error:", err.message);
  }
})();
