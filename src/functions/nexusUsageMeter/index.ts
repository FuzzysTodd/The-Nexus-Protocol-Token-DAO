import { AzureFunction, Context } from "@azure/functions";
import {
  NexusAutomationRequest,
  NexusAutomationResponse,
  validateNexusRequest,
  NexusServiceType,
} from "../../config/nexusApiSchema";

import { EventHubProducerClient } from "@azure/event-hubs";
import { BlobServiceClient } from "@azure/storage-blob";

// ------------------------------------------------------------
// ENVIRONMENT VARIABLES (set these in GitHub Secrets + Azure)
// ------------------------------------------------------------
const EVENT_HUB_CONNECTION = process.env.NEXUS_EVENT_HUB_CONNECTION!;
const EVENT_HUB_NAME = process.env.NEXUS_EVENT_HUB_NAME!;
const BLOB_CONNECTION = process.env.NEXUS_BLOB_CONNECTION!;
const BLOB_CONTAINER = process.env.NEXUS_BLOB_CONTAINER!;

// ------------------------------------------------------------
// NEXUS USAGE METERING FUNCTION
// Logs every automation event to:
// 1. Azure Event Hub (real-time analytics)
// 2. Azure Blob Storage (permanent ledger)
// ------------------------------------------------------------

const httpTrigger: AzureFunction = async function (
  context: Context,
  req
): Promise<void> {
  context.log("Nexus Usage Meter triggered.");

  const body: NexusAutomationRequest = req.body;

  // Validate request
  const validation = validateNexusRequest(body);
  if (!validation.valid) {
    const errorResponse: NexusAutomationResponse = {
      success: false,
      usageEventId: body?.usageEventId || "unknown",
      nexusWorkflowId: body?.nexusWorkflowId || "unknown",
      nexusServiceType: body?.nexusServiceType || NexusServiceType.AUTOMATION,
      timestamp: new Date().toISOString(),
      errors: validation.errors,
    };

    context.res = {
      status: 400,
      body: errorResponse,
    };
    return;
  }

  // ------------------------------------------------------------
  // 1. SEND TO EVENT HUB (real-time metering)
  // ------------------------------------------------------------
  try {
    const producer = new EventHubProducerClient(
      EVENT_HUB_CONNECTION,
      EVENT_HUB_NAME
    );

    const batch = await producer.createBatch();
    batch.tryAdd({ body });

    await producer.sendBatch(batch);
    await producer.close();
  } catch (err: any) {
    context.log.error("Event Hub error:", err.message);
  }

  // ------------------------------------------------------------
  // 2. WRITE TO BLOB STORAGE (permanent ledger)
  // ------------------------------------------------------------
  try {
    const blobService = BlobServiceClient.fromConnectionString(
      BLOB_CONNECTION
    );

    const container = blobService.getContainerClient(BLOB_CONTAINER);
    await container.createIfNotExists();

    const blobName = `${body.timestamp}_${body.usageEventId}.json`;
    const blockBlob = container.getBlockBlobClient(blobName);

    await blockBlob.upload(JSON.stringify(body, null, 2), Buffer.byteLength(JSON.stringify(body)));
  } catch (err: any) {
    context.log.error("Blob Storage error:", err.message);
  }

  // ------------------------------------------------------------
  // SUCCESS RESPONSE
  // ------------------------------------------------------------
  const response: NexusAutomationResponse = {
    success: true,
    usageEventId: body.usageEventId,
    nexusWorkflowId: body.nexusWorkflowId,
    nexusServiceType: body.nexusServiceType,
    timestamp: new Date().toISOString(),
    result: { message: "Usage event logged successfully." },
  };

  context.res = {
    status: 200,
    body: response,
  };
};

export default httpTrigger;
