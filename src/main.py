from textnode import TextNode, TextType
from copy_directory import copy_directory
from generate_page import generate_pages_recursive
print("hello world")

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    src_directory = "/Users/claytoncripe/Desktop/Personal projects/siteGenerator/static"
    dst_directory = "/Users/claytoncripe/Desktop/Personal projects/siteGenerator/public"
    copy_directory(src_directory, dst_directory)

    content_dir = "/Users/claytoncripe/Desktop/Personal projects/siteGenerator/content"
    template_path = "/Users/claytoncripe/Desktop/Personal projects/siteGenerator/template.html"
    dest_dir = "/Users/claytoncripe/Desktop/Personal projects/siteGenerator/public"
    generate_pages_recursive(content_dir, template_path, dest_dir)

if __name__ == "__main__":
    main()