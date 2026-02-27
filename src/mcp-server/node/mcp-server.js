const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/time', (req, res) => {
  res.json({ currentTime: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`MCP Time Server running on port ${PORT}`);
});
