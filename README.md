# Databricks Asset Bundles (DABs) Demo Template

A clean, minimal template for migrating existing projects to Databricks Asset Bundles format.

## Quick Start

1. **Prerequisites**
   ```bash
   pip install databricks-cli
   ```

2. **Configure Databricks**
   ```bash
   # Option A: Use databricks configure (interactive)
   databricks configure
   
   # Option B: Use environment file (recommended for CI/CD)
   cp env.example .env
   # Edit .env with your Databricks workspace URL, token, and warehouse ID
   # Get warehouse ID from: Databricks → SQL Warehouses → Copy warehouse ID
   ```

3. **Deploy Everything**
   ```bash
   ./scripts/deploy.sh
   ```

4. **Clean Up When Done**
   ```bash
   ./scripts/cleanup.sh
   ```

## CI/CD Setup (Optional)

To enable automatic testing on Pull Requests:

1. **Add GitHub Repository Secrets**:
   - Go to your repo → Settings → Secrets and variables → Actions
   - Add secret: `DATABRICKS_TOKEN` (your Databricks token)
   - Optionally add variable: `DATABRICKS_HOST` (defaults to `https://e2-demo-field-eng.cloud.databricks.com/`)

2. **What happens automatically**:
   - **Pull Requests**: Validated and tested with isolated workspace paths
   - **Main branch**: Deployed to your dev environment
   - **PR cleanup**: Resources automatically cleaned up when PR is closed

## What Gets Deployed

- **Workflow**: `Databricks Demo Deployment Example - Two Simple Notebooks` 
- **Notebooks**: `notebook1.ipynb` → `notebook2.ipynb` (sequential execution)
- **Dashboard**: `Demo Dashboard` (deployed alongside notebooks)
- **App**: `demo-app` (Simple Streamlit app)
- **Location**: `/Workspace/Users/your-email@company.com/dbx-dabs-demo-dev/`

## Manual Commands (if you prefer)

```bash
databricks bundle validate    # Check configuration
databricks bundle deploy      # Deploy to workspace
databricks bundle run demo_workflow # Run the demo workflow
databricks bundle summary     # See what's deployed
databricks bundle destroy     # Remove everything
```

## Customizing for Your Project

1. Update `databricks.yml` with your job/notebook names
2. Replace `notebooks/notebook1.ipynb` and `notebooks/notebook2.ipynb` with your notebooks
3. Modify the workspace `host` and `root_path` as needed

## Project Structure

```
├── databricks.yml           # Main DABs configuration
├── notebooks/
│   ├── notebook1.ipynb      # First notebook
│   └── notebook2.ipynb      # Second notebook (runs after first)
├── dashboards/
│   └── dashboard_example.lvdash.json  # Demo dashboard
├── apps/
│   └── demo_app/
│       ├── app.py                     # Streamlit app
│       └── app.yaml                   # App configuration
└── scripts/
    ├── deploy.sh           # Automated deployment
    └── cleanup.sh          # Automated cleanup
```

That's it! 🚀 