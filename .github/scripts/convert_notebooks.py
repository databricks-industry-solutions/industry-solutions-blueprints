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
    """Convert Databricks .py notebook to HTML"""
    filename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(filename)[0]
    name_without_ext = "notebooks/" + name_without_ext
    
    cells = parse_databricks_notebook(filepath)
    html_content = []
    
    for cell in cells:
        if cell['type'] == 'markdown':
            # Convert markdown to HTML
            md_html = markdown.markdown(
                cell['content'], 
                extensions=['fenced_code', 'tables']
            )
            html_content.append(f'''
            <div class="cell border-box-sizing text_cell rendered">
                <div class="inner_cell">
                    <div class="text_cell_render border-box-sizing rendered_html">
                        {md_html}
                    </div>
                </div>
            </div>
            ''')
        elif cell['type'] == 'code':
            # Create syntax highlighted code cell
            escaped_code = html.escape(cell['content'])
            html_content.append(f'''
            <div class="cell border-box-sizing code_cell rendered">
                <div class="input">
                    <div class="inner_cell">
                        <div class="input_area">
                            <pre><code class="language-python">{escaped_code}</code></pre>
                        </div>
                    </div>
                </div>
            </div>
            ''')
    
    # Create full HTML document with notebook styling
    full_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{name_without_ext}</title>
    <!-- Jupyter notebook CSS styling -->
    <style>
        body {{
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 13px;
            line-height: 1.42857143;
            color: #000;
            background-color: #fff;
            margin: 0;
            padding: 0;
        }}
        
        .container {{
            width: 100%;
            padding: 15px;
        }}
        
        .cell {{
            margin-bottom: 15px;
            padding: 5px 0;
        }}
        
        .text_cell .inner_cell {{
            padding: 5px 5px 5px 0px;
        }}
        
        .text_cell_render {{
            outline: none;
            resize: none;
            width: inherit;
            border-style: none;
            padding: 0.5em 0.5em 0.5em 0.4em;
            color: #000;
            box-sizing: border-box;
        }}
        
        .code_cell {{
            background: #f7f7f7;
            border: none;
            border-radius: 2px;
            padding: 8px;
        }}
        
        .input_area {{
            border: 1px solid #cfcfcf;
            border-radius: 2px;
            background: #f7f7f7;
            line-height: 1.21429em;
        }}
        
        .input_area pre {{
            margin: 0;
            padding: 8px;
            font-family: Monaco, 'DejaVu Sans Mono', monospace;
            font-size: 11px;
            overflow: auto;
            color: #000;
            background-color: transparent;
            border: none;
        }}
        
        .text_cell_render h1 {{
            font-size: 1.8em;
            margin: 0.67em 0;
            color: #1F2937;
        }}
        
        .text_cell_render h2 {{
            font-size: 1.5em;
            margin: 0.83em 0;
            color: #1F2937;
        }}
        
        .text_cell_render h3 {{
            font-size: 1.3em;
            margin: 1em 0;
            color: #1F2937;
        }}
        
        .text_cell_render p {{
            margin: 1em 0;
            line-height: 1.6;
        }}
        
        .text_cell_render ul, .text_cell_render ol {{
            margin: 1em 0;
            padding-left: 2em;
        }}
        
        .text_cell_render li {{
            margin: 0.5em 0;
        }}
        
        .text_cell_render code {{
            background: #f8f9fa;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: Monaco, 'DejaVu Sans Mono', monospace;
            color: #e91e63;
        }}
        
        .text_cell_render pre {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            border: 1px solid #e5e7eb;
        }}
        
        .text_cell_render blockquote {{
            border-left: 4px solid #ddd;
            padding-left: 15px;
            margin: 15px 0;
            color: #666;
        }}
        
        /* Syntax highlighting */
        .language-python {{
            color: #333;
        }}
        
        .highlight {{
            background: #f8f8f8;
        }}
    </style>
    
    <!-- Prism.js for syntax highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/plugins/autoloader/prism-autoloader.min.js"></script>
</head>
<body>
    <div class="container">
        {''.join(html_content)}
    </div>
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