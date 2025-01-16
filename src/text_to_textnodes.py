from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_links import split_nodes_link

# def text_to_textnodes(text):
#     nodes = [TextNode(text, TextType.NORMAL)]
#     print("Initial nodes:", nodes)
    
#     nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
#     print("After splitting bold:", nodes)
    
#     nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
#     print("After splitting italic:", nodes)
    
#     nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
#     print("After splitting code:", nodes)
    
#     nodes = split_nodes_image(nodes)
#     print("After splitting images:", nodes)
    
#     nodes = split_nodes_link(nodes)
#     print("After splitting links:", nodes)
    
#     return nodes

# # Example usage
# if __name__ == "__main__":
#     text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#     nodes = text_to_textnodes(text)
#     for node in nodes:
#         print(node)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

# # Example usage
# if __name__ == "__main__":
#     text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#     nodes = text_to_textnodes(text)
#     for node in nodes:
#         print(node)