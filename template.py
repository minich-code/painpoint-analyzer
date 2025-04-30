import os
from pathlib import Path

# Define the project name
project_name = "complaint-insights"

# List of files and directories to be created
list_of_files = [
    # CI/CD with GitHub Actions
    Path(".github") / "workflows" / ".gitkeep",  # Placeholder to keep workflows directory
    Path(".github") / "workflows" / "deploy.yml",  # Workflow for deploying to Vercel
    Path(".github") / "workflows" / "test.yml",  # Workflow for running tests

    # Backend (Python with FastAPI for Vercel deployment)
    Path("api/src/main.py"),  # Entrypoint for FastAPI app
    Path("api/src/routes/upload.py"),  # Endpoint for uploading CSV/TXT files
    Path("api/src/routes/analyze.py"),  # Endpoint for LLM complaint analysis
    Path("api/src/routes/report.py"),  # Endpoint for generating reports
    Path("api/src/services/llm_analyzer.py"),  # Integrates with LLM API for analysis
    Path("api/src/services/categorizer.py"),  # Dynamically clusters complaints into categories
    Path("api/src/services/memory_manager.py"),  # Manages dynamic memory with Supabase (pgvector)
    Path("api/src/utils/file_parser.py"),  # Parses various file formats (CSV/TXT)
    Path("api/src/utils/report_generator.py"),  # Generates PDF reports using reportlab
    Path("api/src/config/settings.py"),  # Environment variables and settings
    Path("api/src/config/database.py"),  # Database connection configuration
    Path("api/requirements.txt"),  # Python dependencies
    Path("api/vercel.json"),  # Vercel configuration for Python backend

    # Frontend (Next.js)
    Path("frontend/app/upload/page.tsx"),  # UI for uploading complaints
    Path("frontend/app/dashboard/page.tsx"),  # Dynamic dashboard with charts and summaries
    Path("frontend/app/auth/login/page.tsx"),  # User login UI
    Path("frontend/app/auth/register/page.tsx"),  # User registration UI
    Path("frontend/app/layout.tsx"),  # Root layout for consistent UI (e.g., navbar)
    Path("frontend/app/page.tsx"),  # Home page with app overview

    # Frontend Components by Feature
    Path("frontend/components/upload/FileUploader.tsx"),  # File upload with drag-and-drop
    Path("frontend/components/upload/FilePreview.tsx"),  # Preview uploaded files
    Path("frontend/components/dashboard/DynamicChart.tsx"),  # Charts for visualizing complaints
    Path("frontend/components/dashboard/SummaryTable.tsx"),  # Table for categorized complaints
    Path("frontend/components/dashboard/CategoryBreakdown.tsx"),  # Breakdown of complaint categories
    Path("frontend/components/common/Navbar.tsx"),  # Navigation bar with user menu
    Path("frontend/components/common/Button.tsx"),  # Reusable button component
    Path("frontend/components/common/Card.tsx"),  # Card component for UI elements

    # Frontend Libraries and Config
    Path("frontend/lib/api.ts"),  # API client for calling backend endpoints
    Path("frontend/lib/auth.ts"),  # NextAuth.js setup for authentication
    Path("frontend/styles/globals.css"),  # Global styles using Tailwind
    Path("frontend/public/favicon.ico"),  # Favicon for the site
    Path("frontend/public/logo.svg"),  # Logo for the application

    # Shared utilities
    Path("shared/types/complaint_types.ts"),  # TypeScript types for complaints, categories
    Path("shared/types/complaint_types.py"),  # Python type hints for complaints, categories
    Path("shared/constants/constants.ts"),  # Frontend constants (e.g., API routes)
    Path("shared/constants/constants.py"),  # Backend constants (e.g., severity levels)

    # Storage configurations
    Path("storage/supabase/client.ts"),  # Supabase client for frontend (memory storage)
    Path("storage/supabase/client.py"),  # Supabase client for backend (memory storage)
    Path("storage/vercel_blob/client.ts"),  # Vercel Blob client for file uploads (frontend)

    # Reports and Sample Data
    Path("reports/sample_report.pdf"),  # Sample PDF report
    Path("reports/sample_data.csv"),  # Sample complaint data for testing

    # Tests
    Path("tests/backend/test_analyzer.py"),  # Tests LLM analysis and categorization
    Path("tests/backend/test_memory.py"),  # Tests memory updates
    Path("tests/frontend/test_dashboard.tsx"),  # Tests dashboard rendering
    Path("tests/frontend/test_upload.tsx"),  # Tests file upload functionality

    # Root configuration files
    Path(".env"),  # Example environment variables
    Path(".gitignore"),  # Files/folders to ignore in Git
    Path("next.config.mjs"),  # Next.js configuration
    Path("package.json"),  # Node dependencies for Next.js frontend
    Path("README.md"),  # Project overview and setup instructions
    Path("tailwind.config.js"),  # Tailwind CSS configuration
    Path("tsconfig.json"),  # TypeScript configuration
    Path("vercel.json"),  # Vercel configuration for frontend
]

# Loop through each file in the list to create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)

    # Split the filepath into a directory and filename
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass

print(f"Project structure for '{project_name}' created successfully!")