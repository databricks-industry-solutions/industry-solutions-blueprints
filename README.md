# Databricks Solution Accelerator Template

[![Databricks](https://img.shields.io/badge/Databricks-Solution_Accelerator-FF3621?style=for-the-badge&logo=databricks)](https://databricks.com)
[![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-Enabled-00A1C9?style=for-the-badge)](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)
[![Serverless](https://img.shields.io/badge/Serverless-Compute-00C851?style=for-the-badge)](https://docs.databricks.com/en/compute/serverless.html)

This repository provides a modern template for creating Databricks solution accelerators with a beautiful, consistent documentation website.

## ✨ Features

- **Single-Page Application**: All documentation and notebooks in one cohesive interface
- **Consistent Rendering**: Both `.ipynb` and `.py` notebooks render identically with syntax highlighting
- **Responsive Design**: Works beautifully on desktop and mobile devices
- **Databricks Branding**: Professional styling with Databricks colors and fonts
- **GitHub Pages**: Automatic deployment of documentation website
- **Content Containment**: Images, tables, and code blocks stay within proper bounds

## 🚀 Getting Started

### 1. Use This Template

Click "Use this template" to create your new solution accelerator repository.

### 2. Customize Your Project

- **Update `databricks.yml`**: Change `project_name` and configure your resources
- **Replace example notebooks**: Add your actual `.ipynb` and `.py` notebooks to the `notebooks/` folder
- **Update this README**: Replace this content with your solution accelerator description
- **Add your content**: Include any additional apps, dashboards, or scripts

### 3. Deploy to Databricks

Follow the standard Databricks Asset Bundles deployment process:

1. Clone your project into your Databricks Workspace
2. Open the Asset Bundle Editor in the Databricks UI
3. Click "Deploy" to deploy your resources
4. Navigate to the Deployments tab and run your workflow

### 4. Documentation Website

Your documentation website will be automatically generated and deployed to GitHub Pages whenever you push to the main branch.

## 📁 Project Structure

```text
├── notebooks/                    # Your notebook files (.ipynb and .py)
├── apps/                         # Databricks Apps (optional)
├── dashboards/                   # Dashboard definitions (optional)
├── scripts/                      # Deployment and utility scripts
├── .github/
│   ├── workflows/publish.yaml    # Automated documentation deployment
│   └── scripts/convert_notebooks.py  # Notebook conversion utility
├── databricks.yml               # Databricks Asset Bundle configuration
└── README.md                    # Your solution accelerator documentation
```

## 🎨 Documentation Features

The generated documentation website includes:

- **Overview page**: Renders your README content
- **Notebook pages**: All notebooks with syntax highlighting and consistent styling
- **Navigation**: Smooth single-page navigation between sections
- **Mobile responsive**: Optimized for all screen sizes
- **Professional styling**: Databricks-branded design

## 🔧 Customization

### Adding Notebooks
Simply add `.ipynb` or `.py` notebook files to the `notebooks/` folder. They will be automatically:
- Converted to HTML with syntax highlighting
- Added to the navigation menu
- Styled consistently with Databricks branding

### Configuring Resources
Edit `databricks.yml` to define your:
- Job workflows and notebook dependencies
- Databricks Apps (if applicable)
- Dashboards (if applicable)
- Environment variables and settings

### Styling Customization
The documentation styling can be customized by editing the CSS in `.github/workflows/publish.yaml`.

## 📝 Development

### Local Testing
```bash
# Install dependencies
pip install databricks-cli

# Validate your bundle
databricks bundle validate

# Deploy to development environment
databricks bundle deploy --target dev
```

### Contributing Guidelines
1. **Clone** this repository locally
2. **Test changes** using the Databricks CLI against your workspace
3. **Submit pull requests** with clear descriptions and second-party reviews

## 📄 License

© 2025 Databricks, Inc. All rights reserved. The source in this project is provided subject to the [Databricks License](https://databricks.com/db-license-source).

---

**Template Instructions**: Replace this entire README with your solution accelerator's specific documentation, including problem description, solution overview, implementation details, and usage instructions.