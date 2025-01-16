def markdown_to_blocks(markdown):
    # Split the markdown text into blocks based on double newlines
    blocks = markdown.split('\n\n')
    
    # Strip leading and trailing whitespace from each block
    blocks = [block.strip() for block in blocks]
    
    # Remove any empty blocks
    blocks = [block for block in blocks if block]
    
    return blocks