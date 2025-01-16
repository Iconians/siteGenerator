def block_to_block_type(block):
    lines = block.split('\n')
    
    # Check for heading
    if lines[0].startswith('#') and lines[0].lstrip('#').startswith(' '):
        return 'heading'
    
    # Check for code block
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    # Check for quote block
    if all(line.startswith('>') for line in lines):
        return 'quote'
    
    # Check for unordered list block
    if all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return 'unordered_list'
    
    # Check for ordered list block
    if all(line.split('.')[0].isdigit() and line.split('.')[1].startswith(' ') for line in lines):
        return 'ordered_list'
    
    # Default to paragraph
    return 'paragraph'