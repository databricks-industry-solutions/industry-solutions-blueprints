#!/usr/bin/env python3

import os
import re
import markdown
import glob
import html


def parse_databricks_notebook(filepath):
    """Parse a Databricks .py notebook format into cells"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split by COMMAND ----------
    sections = re.split(r'# COMMAND ----------', content)
    cells = []
    
    for section in sections:
        if not section.strip():
            continue
            
        # Check if this is a markdown cell
        if '# MAGIC %md' in section:
            # Extract markdown content
            lines = section.split('\n')
            md_lines = []
            for line in lines:
                if line.startswith('# MAGIC %md'):
                    # Remove '# MAGIC %md'
                    md_lines.append(line[11:].strip())
                elif line.startswith('# MAGIC '):
                    # Remove '# MAGIC '
                    md_lines.append(line[8:])
                elif line.startswith('# MAGIC'):
                    # Remove '# MAGIC'
                    md_lines.append(line[7:])
            
            md_content = '\n'.join(md_lines)
            cells.append({'type': 'markdown', 'content': md_content})
        else:
            # This is a code cell
            # Remove any leading comments that aren't actual code
            lines = section.split('\n')
            code_lines = []
            for line in lines:
                if not line.startswith('# DBTITLE'):
                    code_lines.append(line)
            
            code_content = '\n'.join(code_lines).strip()
            if code_content:
                cells.append({'type': 'code', 'content': code_content})
    
    return cells


def convert_to_html(filepath):
    """Convert Databricks .py notebook to HTML exactly matching nbconvert structure"""
    filename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(filename)[0]
    
    cells = parse_databricks_notebook(filepath)
    html_content = []
    
    # Start with nbconvert container structure (matching what nbconvert generates)
    html_content.append('<div class="container" id="notebook-container">')
    
    for i, cell in enumerate(cells):
        if cell['type'] == 'markdown':
            # Convert markdown to HTML using nbconvert structure
            md_html = markdown.markdown(
                cell['content'], 
                extensions=['fenced_code', 'tables', 'nl2br', 'toc']
            )
            html_content.append(f'''<div class="cell border-box-sizing text_cell rendered">
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
{md_html}
</div>
</div>
</div>''')
        elif cell['type'] == 'code':
            # Create code cell exactly matching nbconvert structure
            escaped_code = html.escape(cell['content'])
            html_content.append(f'''<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
<div class="input_area">
<div class="highlight hl-ipython3"><pre><span></span>{escaped_code}</pre></div>
</div>
</div>
</div>
</div>''')
    
    html_content.append('</div>')  # Close container
    
    # Create minimal HTML document structure (no full styles, will be wrapped later)
    body_content = '\\n'.join(html_content)
    
    # Create simple HTML structure that matches what nbconvert generates
    simple_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{name_without_ext}</title>
</head>
<body>
{body_content}
</body>
</html>'''
    
    # Write HTML file
    output_path = f"site/{name_without_ext}.html"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(simple_html)
    
    return name_without_ext


if __name__ == "__main__":
    # Process all .py files in notebooks directory
    for py_file in glob.glob('notebooks/*.py'):
        convert_to_html(py_file)
        print(f"Converted {py_file} to HTML")