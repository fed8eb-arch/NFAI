"""Expose the public NFAI memory index over a local, read-only MCP server."""
from mcp.server.fastmcp import FastMCP

from query import load_graph

server = FastMCP("NFAI Memory")


@server.tool()
def memory_list(kind: str = "") -> list[dict]:
    """List graph nodes, optionally filtered by kind such as role or task."""
    nodes, _ = load_graph()
    return [
        {"id": node["id"], "kind": node["kind"], "label": node["label"]}
        for node in nodes.values()
        if not kind or node["kind"] == kind
    ]


@server.tool()
def memory_show(node_id: str) -> dict:
    """Read one graph node, evidence paths, and incoming and outgoing edges."""
    nodes, edges = load_graph()
    if node_id not in nodes:
        raise ValueError(f"Unknown node: {node_id}. Use memory_list to find the ID.")
    return {
        "node": nodes[node_id],
        "edges": [edge for edge in edges if node_id in (edge["source"], edge["target"])],
    }


if __name__ == "__main__":
    server.run(transport="stdio")
