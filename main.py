import os

def validate_content(content):
    try:
        if not (1 <= len(content) <= 279):
            return False
        if not content.strip():
            return False
        if content.count(chr(10)) != 1:
            return False
        if not content.endswith(chr(10)):
            return False
        return True
    except Exception:
        return False

def main():
    LINE = '1 star. Roots rot in this black plastic pot, a "minimalist upgrade" with no drainage. Daily misting breeds mold; two predecessors died here. Strangled by interior design. One star for the elegance of my decomposition in this vessel with no exit.'
    
    content = LINE + chr(10)
    if not validate_content(content):
        raise ValueError(f'Validation failed')
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or '/output'
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, 'entry.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Output path: {output_file}, character count: {len(content)}')

if __name__ == "__main__":
    main()