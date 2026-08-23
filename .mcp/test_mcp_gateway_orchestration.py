# Run all tests
pytest -q

# Run MCP Gateway tests only
pytest nexus/test_mcp_gateway_orchestration.py -v

# Run with coverage
pytest --cov=nexus --cov-report=html

# Run specific test class
pytest nexus/test_mcp_gateway_orchestration.py::TestMCPGatewayConfiguration -v
