# GlobalCorp AI Coding Guidelines

## Backend (Python)
- **Framework:** Always assume we are using `FastAPI`.
- **Typing:** Strict Python 3.10+ type hints are mandatory for all function signatures.
- **Documentation:** Every function must have a comprehensive Google-style docstring.
- **Logging:** NEVER use the built-in `print()` function. Always assume a custom logger is available via `from core.logger import get_logger` and instantiate it with `logger = get_logger(__name__)`.
- **API Responses:** All API endpoints must return a standardized JSON structure: `{"status": "success|error", "data": <payload>, "message": "<info>"}`.

## Frontend (React/JavaScript)
- **Styling:** Always use Tailwind CSS utility classes for styling. NEVER use inline `style={{}}` attributes or external CSS files.
- **Architecture:** Always use functional components with React Hooks. Never use Class components.
- **State:** Use descriptive variable names for `useState` (e.g., `isModalOpen`, not `open`).