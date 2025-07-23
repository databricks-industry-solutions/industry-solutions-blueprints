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
    """Convert Databricks .py notebook to HTML matching nbconvert structure"""
    filename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(filename)[0]
    
    cells = parse_databricks_notebook(filepath)
    html_content = []
    
    # Add notebook container matching nbconvert structure
    html_content.append('<div class="jp-Notebook" data-jp-theme-light="true">')
    
    for i, cell in enumerate(cells):
        if cell['type'] == 'markdown':
            # Convert markdown to HTML
            md_html = markdown.markdown(
                cell['content'], 
                extensions=['fenced_code', 'tables', 'nl2br']
            )
            html_content.append(f'''
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
{md_html}
</div>
</div>
</div>''')
        elif cell['type'] == 'code':
            # Create code cell matching nbconvert structure
            escaped_code = html.escape(cell['content'])
            html_content.append(f'''
<div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="CodeMirror cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span>{escaped_code}</pre></div>
</div>
</div>
</div>
</div>
</div>''')
    
    html_content.append('</div>')
    
    # Create full HTML document with minimal structure
    full_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{name_without_ext}</title>
    <style>
        .jp-RenderedHTMLCommon {{ font-family: 'DM Sans', sans-serif; color: #1B3139; }}
        .jp-RenderedHTMLCommon h1, .jp-RenderedHTMLCommon h2, .jp-RenderedHTMLCommon h3 {{ color: #1B3139; }}
        .jp-RenderedHTMLCommon code {{ background-color: #F5F5F5; padding: 2px 4px; border-radius: 3px; }}
        .highlight pre {{ background-color: #F5F5F5; padding: 16px; border-radius: 4px; overflow-x: auto; }}
    </style>
</head>
<body>
{''.join(html_content)}
</body>
</html>'''
    
    # Write HTML file
    output_path = f"site/{name_without_ext}.html"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(full_html)
    
    return name_without_ext


if __name__ == "__main__":
    # Process all .py files in notebooks directory
    for py_file in glob.glob('notebooks/*.py'):
        convert_to_html(py_file)
        print(f"Converted {py_file} to HTML")