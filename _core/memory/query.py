"""Validate and query the shared NFAI memory graph."""
import argparse
import json
from pathlib import Path

DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[1]


def load_graph():
    data = json.loads((DIRECTORY / "graph.json").read_text(encoding="utf-8"))
    if data["version"] != 1:
        raise ValueError("Unsupported graph version")
    nodes = {node["id"]: node for node in data["nodes"]}
    if len(nodes) != len(data["nodes"]):
        raise ValueError("Duplicate node ID")

    def check_source(source):
        path = ROOT / source
        if not path.resolve().is_relative_to(ROOT) or not path.is_file():
            raise ValueError(f"Invalid source: {source}")

    profiles = {
        path.stem for path in (ROOT / "_core/staff").glob("*.md")
        if any(line in {"## Role", "## Role and reporting"}
               for line in path.read_text(encoding="utf-8").splitlines())
    }
    roles = {node["id"] for node in nodes.values() if node["kind"] == "role"}
    if roles != profiles | {"founder", "buddy"}:
        raise ValueError(f"Role profiles and graph differ: {sorted(roles ^ (profiles | {'founder', 'buddy'}))}")
    for node in nodes.values():
        if not node["sources"]:
            raise ValueError(f"Node has no source: {node['id']}")
        for source in node["sources"]:
            check_source(source)

    edges = set()
    parents = {}
    for edge in data["edges"]:
        origin, relation, target = (edge[key] for key in ("source", "relation", "target"))
        triple = origin, relation, target
        if origin not in nodes or target not in nodes or origin == target or triple in edges:
            raise ValueError(f"Invalid edge: {triple}")
        edges.add(triple)
        check_source(edge["evidence"])
        if relation == "reports_to":
            if origin not in roles or target not in roles or origin in parents:
                raise ValueError(f"Invalid reporting line: {triple}")
            parents[origin] = target
    for role in roles:
        current, visited = role, set()
        while current in parents:
            if current in visited:
                raise ValueError(f"Reporting cycle at {role}")
            visited.add(current)
            current = parents[current]
        if current not in {"founder", "business-angel", "ai-certified-mentor"}:
            raise ValueError(f"Reporting line does not reach the founder: {role}")
    return nodes, data["edges"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="validate sources, roles and edges")
    commands.add_parser("list", help="list graph nodes")
    show = commands.add_parser("show", help="show a node and its connections")
    show.add_argument("id")
    args = parser.parse_args()
    nodes, edges = load_graph()
    if args.command == "check":
        roles = sum(node["kind"] == "role" for node in nodes.values())
        print(f"OK: {len(nodes)} nodes, {roles} roles, {len(edges)} edges")
    elif args.command == "list":
        for node in nodes.values():
            print(f"{node['id']} | {node['kind']} | {node['label']}")
    else:
        if args.id not in nodes:
            parser.error(f"Unknown node: {args.id}. Run list for available IDs.")
        node = nodes[args.id]
        print(f"{node['label']} [{node['id']}]")
        for source in node["sources"]:
            print(f"  {source}")
        for edge in edges:
            if args.id in (edge["source"], edge["target"]):
                print(f"  {edge['source']} — {edge['relation']} → {edge['target']} [{edge['evidence']}]")


if __name__ == "__main__":
    main()
