<script>
  async function runDuneAnomalyScan(approvalItem) {
    const preview = document.getElementById('dune-preview');
    preview.textContent = "Running Dune anomaly scan…";

    try {
      // Replace with your real Dune API key
      const DUNE_API_KEY = "YOUR_DUNE_API_KEY";

      // Your Dune query ID (from your open tab 1923353)
      const QUERY_ID = 1923353;

      // Build query execution payload
      const payload = {
        query_parameters: {
          contract: approvalItem.request?.from || approvalItem.request?.contract || null,
          chain_id: approvalItem.chainId || 1
        }
      };

      // Execute the query
      const execRes = await fetch(
        `https://api.dune.com/api/v1/query/${QUERY_ID}/execute`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Dune-Api-Key": DUNE_API_KEY
          },
          body: JSON.stringify(payload)
        }
      );

      if (!execRes.ok) {
        preview.textContent = "Failed to execute Dune query.";
        return;
      }

      const execData = await execRes.json();
      const executionId = execData.execution_id;

      // Poll for results
      let resultData = null;
      for (let i = 0; i < 10; i++) {
        const resultRes = await fetch(
          `https://api.dune.com/api/v1/execution/${executionId}/results`,
          {
            headers: { "X-Dune-Api-Key": DUNE_API_KEY }
          }
        );

        if (resultRes.ok) {
          const json = await resultRes.json();
          if (json.state === "QUERY_STATE_COMPLETED") {
            resultData = json;
            break;
          }
        }

        await new Promise(r => setTimeout(r, 1500));
      }

      if (!resultData) {
        preview.textContent = "Dune query timed out.";
        return;
      }

      // Extract anomalies
      const rows = resultData.result?.rows || [];
      const anomalies = rows.filter(r => r.anomaly_score > 0.5);

      preview.textContent = JSON.stringify({
        anomalies_found: anomalies.length,
        anomalies: anomalies.slice(0, 5),
        total_rows: rows.length
      }, null, 2);

    } catch (err) {
      preview.textContent = "Error running Dune anomaly scan.";
      console.error("Dune error:", err);
    }
  }

  // Extend DETAILS handler to trigger Dune scan
  document.addEventListener('click', function (e) {
    const btn = e.target;
    if (!btn.dataset.id) return;

    if (btn.classList.contains('btn-details')) {
      const id = btn.dataset.id;
      const item = approvalsCache.find(a => a.id === id);

      // Run Dune anomaly scan
      runDuneAnomalyScan(item);
    }
  });
</script>
