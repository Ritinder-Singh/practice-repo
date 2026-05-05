// =============================================================================
// Express REST API — Entry Point
// =============================================================================
import express from "express";

const app = express();
const PORT = process.env.PORT || 3000;
app.use(express.json());

// TODO: import and mount routes
// TODO: add global error handler middleware
// TODO: add request logger

app.get("/health", (_req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

app.listen(PORT, () => console.log(`API running on http://localhost:${PORT}`));
export default app;
