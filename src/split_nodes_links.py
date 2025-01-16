import re
from textnode import TextNode, TextType

def split_nodes_link(old_nodes):
    new_nodes = []
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    for node in old_nodes:
        if node.text_type == TextType.NORMAL.value:
            parts = re.split(link_pattern, node.text)
            for i in range(0, len(parts), 3):
                if i < len(parts):
                    new_nodes.append(TextNode(parts[i], TextType.NORMAL))
                if i + 1 < len(parts) and i + 2 < len(parts):
                    new_nodes.append(TextNode(parts[i + 1], TextType.LINKS, parts[i + 2]))
        else:
            new_nodes.append(node)
    # return new_nodes
    return [node for node in new_nodes if node.text] 