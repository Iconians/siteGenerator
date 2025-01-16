from textnode import TextNode, TextType
from htmlnode import LeafNode

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
        if text_node.url is None:
            raise ValueError("URL must be provided for link text nodes.")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGES.value:
        if text_node.url is None:
            raise ValueError("URL must be provided for image text nodes.")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")