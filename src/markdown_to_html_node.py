from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_block import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import TextType, TextNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL.value:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD.value:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC.value:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE.value:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINKS.value:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGES.value:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == 'heading':
            level = block.count('#')
            text = block.lstrip('#').strip()
            children.append(LeafNode(tag=f"h{level}", value=text))
        elif block_type == 'paragraph':
            children.append(ParentNode(tag="p", children=text_to_children(block)))
        elif block_type == 'code':
            code_text = block.strip('`')
            code_node = ParentNode(tag="pre", children=[LeafNode(tag="code", value=code_text)])
            children.append(code_node)
        elif block_type == 'quote':
            quote_text = block.lstrip('>').strip()
            children.append(ParentNode(tag="blockquote", children=text_to_children(quote_text)))
        elif block_type == 'unordered_list':
            list_items = block.split('\n')
            list_children = [ParentNode(tag="li", children=text_to_children(item.lstrip('*').lstrip('-').strip())) for item in list_items]
            children.append(ParentNode(tag="ul", children=list_children))
        elif block_type == 'ordered_list':
            list_items = block.split('\n')
            list_children = [ParentNode(tag="li", children=text_to_children(item.split('. ', 1)[1])) for item in list_items]
            children.append(ParentNode(tag="ol", children=list_children))
        else:
            raise ValueError(f"Unsupported block type: {block_type}")

    return ParentNode(tag="div", children=children)

# Example usage
if __name__ == "__main__":
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    
    html_node = markdown_to_html_node(markdown)
    print(html_node.to_html())