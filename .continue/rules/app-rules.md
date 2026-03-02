---
description: "vscode-settings-ai" description
---

# Purpose of the project

1. Develop a VSCode configuration for project development using AI.
2. Develop demo MCP servers for using AI.
3. Demonstrate the project using docker-compose.yml

## Project Architecture

This is a complex application with:

- AI implementation by plugin "Continue" for VSCode.
Use config `.continue/agents/app-config.yaml` for define AI Models.
- MCP severs for Continue defined in `.continue/mcpServers/` folder.
- Docker Compose - configuration for demo services on `docker-compose.yml`
- Dockerfile for "MCP Server by NodeJs" in `docker/node-mcp-server/Dockerfile`
- All source code in `src/`
- Source for MCP Server in `src/mcp-server`
- Source for MCP Server by NodeJs `src/mcp-server/node`
Configuration file for npm packages of this project in `package.json`.
- Source for MCP Server by Python `src/mcp-server/python`


## Coding Standards

- Follow the existing naming conventions
- Write tests for all new features