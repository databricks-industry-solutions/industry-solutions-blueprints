#!/bin/bash

# Databricks Asset Bundle Deployment Script
# This script automates the deployment of your DABs project

set -e  # Exit on any error

echo "🚀 Starting Databricks Asset Bundle Deployment..."
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if databricks CLI is installed
if ! command -v databricks &> /dev/null; then
    print_error "Databricks CLI is not installed or not in PATH"
    echo "Please install it with: pip install databricks-cli"
    exit 1
fi

print_success "Databricks CLI found"

# Load environment variables from .env file if it exists
if [ -f ".env" ]; then
    print_status "Loading environment variables from .env file..."
    export $(grep -v '^#' .env | xargs)
    print_success "Environment variables loaded"
else
    print_status "No .env file found - using system environment variables"
fi

# Step 1: Validate the bundle
print_status "Validating bundle configuration..."
if [ -z "$DATABRICKS_WAREHOUSE_ID" ]; then
    print_warning "DATABRICKS_WAREHOUSE_ID not set - dashboard deployment will be skipped"
    print_status "To deploy dashboards, set DATABRICKS_WAREHOUSE_ID in your environment"
    print_status "Get warehouse ID from: Databricks → SQL Warehouses → Copy warehouse ID"
    if databricks bundle validate; then
        print_success "Bundle validation passed (without dashboard)"
    else
        print_error "Bundle validation failed"
        exit 1
    fi
else
    if databricks bundle validate --var="warehouse_id=$DATABRICKS_WAREHOUSE_ID"; then
        print_success "Bundle validation passed (with dashboard)"
    else
        print_error "Bundle validation failed"
        exit 1
    fi
fi

# Step 2: Deploy the bundle
print_status "Deploying bundle to Databricks workspace..."
if [ -n "$DATABRICKS_WAREHOUSE_ID" ]; then
    if databricks bundle deploy --var="warehouse_id=$DATABRICKS_WAREHOUSE_ID"; then
        print_success "Bundle deployed successfully (with dashboard)"
    else
        print_error "Bundle deployment failed"
        exit 1
    fi
else
    if databricks bundle deploy; then
        print_success "Bundle deployed successfully (notebooks only)"
    else
        print_error "Bundle deployment failed"
        exit 1
    fi
fi

# Step 3: Show deployment summary
print_status "Getting deployment summary..."
if [ -n "$DATABRICKS_WAREHOUSE_ID" ]; then
    databricks bundle summary --var="warehouse_id=$DATABRICKS_WAREHOUSE_ID"
else
    databricks bundle summary
fi

# Step 4: Ask if user wants to run the demo job
echo ""
read -p "Do you want to run the demo job now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Running demo job..."
    if [ -n "$DATABRICKS_WAREHOUSE_ID" ]; then
        if databricks bundle run demo_workflow --var="warehouse_id=$DATABRICKS_WAREHOUSE_ID"; then
            print_success "Demo job completed successfully!"
        else
            print_warning "Demo job failed - check the Databricks UI for details"
        fi
    else
        if databricks bundle run demo_workflow; then
            print_success "Demo job completed successfully!"
        else
            print_warning "Demo job failed - check the Databricks UI for details"
        fi
    fi
else
    print_status "Skipping job execution"
fi

echo ""
echo "=================================================="
print_success "Deployment script completed!"
echo ""
echo "📋 What was deployed:"
echo "   • Bundle: dbx-dabs-demo"
echo "   • Location: /Workspace/Shared/dbx-dabs-demo/"
echo "   • Job: Databricks Demo Deployment Example - Two Simple Notebooks"
echo "   • Notebooks: notebook1.ipynb → notebook2.ipynb"
echo "   • Dashboard: Demo Dashboard"
echo "   • App: demo-app (Streamlit)"
echo ""
echo "🔗 Useful commands:"
if [ -n "$DATABRICKS_WAREHOUSE_ID" ]; then
    echo "   • View summary: databricks bundle summary --var=\"warehouse_id=\$DATABRICKS_WAREHOUSE_ID\""
    echo "   • Run job: databricks bundle run demo_workflow --var=\"warehouse_id=\$DATABRICKS_WAREHOUSE_ID\""
    echo "   • Destroy bundle: databricks bundle destroy --var=\"warehouse_id=\$DATABRICKS_WAREHOUSE_ID\""
else
    echo "   • View summary: databricks bundle summary"
    echo "   • Run job: databricks bundle run demo_workflow"
    echo "   • Destroy bundle: databricks bundle destroy"
fi
echo ""
print_success "Happy coding! 🎉" 