"""
Custom exceptions for GraphRAG MCP Server.
"""


class GraphRAGError(Exception):
    """Base exception for GraphRAG MCP Server errors."""

    def __init__(self, message: str, error_code: str = "UNKNOWN"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class ResourceNotFoundError(GraphRAGError):
    """Raised when a requested resource is not found."""

    def __init__(self, resource_uri: str):
        message = f"Resource not found: {resource_uri}"
        super().__init__(message, "RESOURCE_NOT_FOUND")
        self.resource_uri = resource_uri


class ContentGenerationError(GraphRAGError):
    """Raised when content generation fails."""

    def __init__(self, resource_uri: str, reason: str):
        message = f"Failed to generate content for {resource_uri}: {reason}"
        super().__init__(message, "CONTENT_GENERATION_FAILED")
        self.resource_uri = resource_uri
        self.reason = reason


class PromptNotFoundError(GraphRAGError):
    """Raised when a requested prompt is not found."""

    def __init__(self, prompt_name: str):
        message = f"Prompt not found: {prompt_name}"
        super().__init__(message, "PROMPT_NOT_FOUND")
        self.prompt_name = prompt_name


class ToolNotFoundError(GraphRAGError):
    """Raised when a requested tool is not found."""

    def __init__(self, tool_name: str):
        message = f"Tool not found: {tool_name}"
        super().__init__(message, "TOOL_NOT_FOUND")
        self.tool_name = tool_name


class ToolExecutionError(GraphRAGError):
    """Raised when tool execution fails."""

    def __init__(self, tool_name: str, details: str):
        message = f"Failed to execute tool {tool_name}: {details}"
        super().__init__(message, "TOOL_EXECUTION_FAILED")
        self.tool_name = tool_name
        self.details = details