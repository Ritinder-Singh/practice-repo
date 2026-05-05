// =============================================================================
// n8n — Workflow Automation Practice
// =============================================================================
// Docs: https://docs.n8n.io
// Run: npx n8n  (or: docker run -it --rm -p 5678:5678 n8nio/n8n)
// Open: http://localhost:5678
// Key concepts: nodes, triggers, expressions, credentials, error workflows
// =============================================================================

// n8n is visual — this file is a structured study guide with JS expression practice.
// The Code node in n8n executes JavaScript. These patterns cover real use cases.

// ─── TODO 1: HTTP Request + data transformation ───────────────────────────────
// Build a workflow that:
//   1. Trigger: Schedule (every hour)
//   2. HTTP Request → GET https://jsonplaceholder.typicode.com/posts
//   3. Code node → filter only posts with userId === 1
//   4. HTTP Request → POST each filtered post to a webhook endpoint
//
// Code node (filter + reshape):
const filterAndReshape = (items) => {
  return items
    .filter(item => item.json.userId === 1)
    .map(item => ({
      json: {
        title: item.json.title,
        body: item.json.body.substring(0, 100),
        source: "jsonplaceholder",
        processedAt: new Date().toISOString(),
      }
    }));
};
// In n8n Code node: return filterAndReshape($input.all());

// ─── TODO 2: CRM integration (like Genius365 HubSpot/GoHighLevel work) ───────
// Build a workflow that syncs a new contact from one CRM to another:
//   1. Trigger: Webhook (POST /webhook/new-contact from CRM A)
//   2. Code node → validate and normalize the contact data
//   3. IF node → check if email already exists in CRM B (HTTP GET)
//   4. Branch A (exists) → update the contact (HTTP PATCH)
//   5. Branch B (new)    → create the contact (HTTP POST)
//   6. Slack node        → notify #crm-sync channel with result
//
// Code node — normalize contact from HubSpot to GoHighLevel format:
const normalizeContact = (hubspotContact) => {
  const props = hubspotContact.properties;
  return {
    firstName: props.firstname,
    lastName: props.lastname,
    email: props.email,
    phone: props.phone,
    tags: ["hubspot-sync"],
    source: "HubSpot",
    customFields: {
      hubspot_id: hubspotContact.id,
      synced_at: new Date().toISOString(),
    }
  };
};

// ─── TODO 3: Error handling & retries ─────────────────────────────────────────
// TODO 3a: Add a Try/Catch wrapper to any workflow:
//   - On success: continue to next node
//   - On error: send a Slack/email alert with the error details, then stop
//
// TODO 3b: Set up an Error Workflow in n8n settings:
//   - A dedicated workflow that receives errors from ALL other workflows
//   - Logs to a Google Sheet or Postgres
//   - Sends a Slack DM with: workflow name, error message, execution ID, timestamp
//
// Error Workflow Code node — format the alert message:
const formatErrorAlert = (errorData) => {
  return {
    text: [
      `❌ *Workflow Failed*`,
      `*Workflow:* ${errorData.workflow.name}`,
      `*Error:* ${errorData.execution.error.message}`,
      `*Execution ID:* ${errorData.execution.id}`,
      `*Time:* ${new Date().toLocaleString()}`,
      `<https://n8n.yourdomain.com/execution/${errorData.execution.id}|View Execution>`,
    ].join("\n")
  };
};

// ─── TODO 4: Webhook → process → respond ──────────────────────────────────────
// Build a workflow that acts as a lightweight API endpoint:
//   1. Webhook trigger (respond: "Using Respond to Webhook Node")
//   2. Validate the incoming payload (Code node)
//   3. Query PostgreSQL for related data
//   4. Transform the result
//   5. Respond to Webhook node → return JSON response
//
// This is how n8n replaced a microservice in the Genius365 QA pipeline.
//
// Code node — validate webhook payload:
const validatePayload = (body) => {
  const required = ["call_id", "transcript", "agent_id"];
  const missing = required.filter(k => !body[k]);
  if (missing.length > 0) {
    throw new Error(`Missing required fields: ${missing.join(", ")}`);
  }
  return {
    callId: body.call_id,
    transcript: body.transcript.trim(),
    agentId: body.agent_id,
    receivedAt: new Date().toISOString(),
  };
};

// ─── TODO 5: Scheduling + idempotency ─────────────────────────────────────────
// Build a workflow that runs daily and processes records only once:
//   1. Schedule trigger (every day at 06:00)
//   2. PostgreSQL node → SELECT records WHERE processed_at IS NULL LIMIT 100
//   3. SplitInBatches node → process 10 at a time (avoid rate limits)
//   4. HTTP Request → external API per record
//   5. PostgreSQL node → UPDATE records SET processed_at = NOW() WHERE id = $id
//
// Key: the WHERE processed_at IS NULL ensures idempotency — safe to re-run.

// ─── TODO 6: n8n expressions reference ───────────────────────────────────────
// n8n expressions use {{ }} syntax in node parameters:
//
// Reference previous node output:
//   {{ $json.email }}                    — field from current item
//   {{ $node["HTTP Request"].json.id }}  — field from a specific node
//   {{ $input.first().json.name }}       — first item from input
//   {{ $input.all().length }}            — count of all input items
//
// Built-in helpers:
//   {{ $now.toISO() }}                   — current timestamp ISO string
//   {{ $now.minus({ hours: 24 }).toISO() }}  — 24 hours ago
//   {{ $json.name.toUpperCase() }}       — string methods
//   {{ $json.items.filter(i => i.active) }}  — array filter
//
// Conditional (ternary):
//   {{ $json.status === "active" ? "✅ Active" : "⛔ Inactive" }}

// ─── KEY CONCEPTS TO UNDERSTAND ──────────────────────────────────────────────
// Trigger nodes:    Webhook, Schedule, Database polling, App events (HubSpot, Slack)
// Core nodes:       HTTP Request, Code, IF, Switch, SplitInBatches, Merge, Set
// Error handling:   Try/Catch node, Error Workflow setting, Stop and Error node
// Credentials:      Stored encrypted — never hardcode API keys in expressions
// Executions:       Each run is logged — inspect input/output of every node
// Self-host:        docker run -v ~/.n8n:/home/node/.n8n -p 5678:5678 n8nio/n8n
