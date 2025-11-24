# Django ToDo Application

A full-featured web-based ToDo application built with Django, featuring complete CRUD operations, due date management, and task completion tracking.

## Features

- **Create Todos** - Add new tasks with title, description, and optional due dates
- **Edit Todos** - Update existing tasks at any time
- **Delete Todos** - Remove tasks with confirmation prompt
- **Mark as Complete** - Toggle completion status with one click
- **Due Date Management** - Assign and track due dates for tasks
- **Visual Indicators** - Color-coded borders for task status (pending, completed, overdue)
- **Responsive Design** - Bootstrap 5 UI works on all devices
- **Admin Interface** - Django admin panel for advanced task management

## Technologies Used

- **Python 3.12** - Programming language
- **Django 5.2.8** - Web framework
- **SQLite** - Database
- **Bootstrap 5** - Frontend framework
- **uv** - Python package manager
- **HTML/CSS** - Frontend templating

## Project Structure

```
AI-Dev-Course-ToDo-project/
├── todoproject/          # Django project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── todos/               # Todos application
│   ├── models.py        # Todo model definition
│   ├── views.py         # View functions for CRUD operations
│   ├── forms.py         # TodoForm for data validation
│   ├── urls.py          # App URL patterns
│   ├── admin.py         # Admin interface configuration
│   ├── tests.py         # Comprehensive test suite (24 tests)
│   └── templates/       # HTML templates
│       └── todos/
│           ├── base.html              # Base template
│           ├── todo_list.html         # List view
│           ├── todo_form.html         # Create/Edit form
│           └── todo_confirm_delete.html  # Delete confirmation
├── manage.py            # Django management script
└── db.sqlite3          # SQLite database

```

## Installation

### Prerequisites

- Python 3.12+
- uv package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Dev-Course-ToDo-project
   ```

2. **Install Django using uv**
   ```bash
   uv add django
   ```

3. **Run database migrations**
   ```bash
   uv run python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**
   ```bash
   uv run python manage.py createsuperuser
   ```

## Running the Application

### Start the development server

```bash
uv run python manage.py runserver
```

Or on a specific port:
```bash
uv run python manage.py runserver 8001
```

### Access the application

- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Testing

The project includes comprehensive test coverage with 24 tests covering models, forms, views, and integration workflows.

### Run all tests
```bash
uv run python manage.py test
```

### Run tests with verbose output
```bash
uv run python manage.py test todos --verbosity=2
```

### Test Coverage

- **Model Tests (6)**: Todo model creation, defaults, ordering, timestamps
- **Form Tests (4)**: Form validation, required fields, optional fields
- **View Tests (14)**: CRUD operations, redirects, error handling, 404s
- **Integration Tests (2)**: Complete workflows, multiple todos

All tests passing ✓

## Usage

### Creating a Todo

1. Click "Create New Todo" button
2. Fill in the title (required)
3. Add description (optional)
4. Set due date (optional)
5. Click "Create"

### Editing a Todo

1. Click "Edit" button on any todo
2. Modify fields as needed
3. Click "Edit" to save changes

### Marking as Complete

- Click "Complete" button to mark as done
- Click "Reopen" to mark as pending again

### Deleting a Todo

1. Click "Delete" button
2. Confirm deletion on the confirmation page

## Database Schema

### Todo Model

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key (auto-generated) |
| title | CharField(200) | Task title (required) |
| description | TextField | Task description (optional) |
| due_date | DateTimeField | Due date and time (optional) |
| is_completed | BooleanField | Completion status (default: False) |
| created_at | DateTimeField | Creation timestamp (auto) |
| updated_at | DateTimeField | Last update timestamp (auto) |

## API Endpoints

| URL | View | Method | Description |
|-----|------|--------|-------------|
| `/` | todo_list | GET | Display all todos |
| `/create/` | todo_create | GET/POST | Show form / Create todo |
| `/edit/<id>/` | todo_edit | GET/POST | Show form / Update todo |
| `/delete/<id>/` | todo_delete | GET/POST | Show confirmation / Delete todo |
| `/toggle/<id>/` | todo_toggle | GET | Toggle completion status |

## Development

### Making Model Changes

1. Modify models in `todos/models.py`
2. Create migrations:
   ```bash
   uv run python manage.py makemigrations
   ```
3. Apply migrations:
   ```bash
   uv run python manage.py migrate
   ```

### Adding New Features

1. Update models if needed
2. Create/update views in `todos/views.py`
3. Add URL patterns in `todos/urls.py`
4. Create templates in `todos/templates/todos/`
5. Write tests in `todos/tests.py`
6. Run tests to verify

## Troubleshooting

### Port already in use

If port 8000 is occupied:
```bash
# Use a different port
uv run python manage.py runserver 8001

# Or find and kill the process using port 8000
lsof -i :8000
kill <PID>
```

### Database issues

```bash
# Delete database and start fresh
rm db.sqlite3
uv run python manage.py migrate
```

## Future Enhancements & Roadmap

The following world-class features are planned for future releases to transform this into a production-ready, enterprise-grade task management system:

### Version 2.0 - User Management & Security

- **User Authentication**
  - User registration and login system
  - Email verification
  - Password reset functionality
  - Social authentication (Google, GitHub, Microsoft)
  - Two-factor authentication (2FA)

- **Multi-user Support**
  - Personal todo lists for each user
  - User profiles with avatars
  - User preferences and settings

- **Security Enhancements**
  - CSRF protection (already implemented)
  - SQL injection prevention (Django ORM)
  - XSS protection
  - Rate limiting for API endpoints
  - HTTPS enforcement

### Version 2.5 - Advanced Organization

- **Categories & Tags**
  - Create custom categories (Work, Personal, Shopping, etc.)
  - Multiple tags per todo
  - Tag-based filtering and search
  - Color-coded categories

- **Priority Levels**
  - High, Medium, Low, Critical priority levels
  - Visual priority indicators
  - Sort by priority
  - Auto-prioritization based on due dates

- **Subtasks & Checklists**
  - Break down todos into smaller subtasks
  - Track subtask completion progress
  - Nested subtasks (unlimited depth)
  - Checklist templates

- **Projects & Workspaces**
  - Group related todos into projects
  - Multiple workspaces for different contexts
  - Project progress tracking
  - Project templates

### Version 3.0 - Smart Features & Automation

- **Search & Advanced Filtering**
  - Full-text search across title and description
  - Filter by status, priority, category, date range
  - Saved search queries
  - Smart search with AI suggestions

- **Recurring Tasks**
  - Daily, weekly, monthly, yearly recurrence
  - Custom recurrence patterns
  - Skip or modify specific occurrences
  - End date for recurring tasks

- **Notifications & Reminders**
  - Email notifications for due dates
  - SMS reminders (via Twilio)
  - Push notifications (web push API)
  - Customizable reminder times (1 hour, 1 day, 1 week before)
  - Digest emails (daily/weekly summary)

- **AI-Powered Features**
  - Smart due date suggestions based on task complexity
  - Auto-categorization using NLP
  - Priority recommendations
  - Time estimation for tasks
  - Natural language input ("Remind me to call John tomorrow at 3pm")

### Version 3.5 - Collaboration & Sharing

- **Team Collaboration**
  - Share todos with other users
  - Assign tasks to team members
  - Comments and discussions on todos
  - @mentions in comments
  - Activity feed and notifications

- **Permissions & Roles**
  - Owner, Editor, Viewer roles
  - Custom permission levels
  - Team management
  - Workspace sharing

- **Real-time Collaboration**
  - Live updates using WebSockets
  - See who's viewing/editing tasks
  - Collaborative editing
  - Conflict resolution

### Version 4.0 - Enhanced UX & Visualization

- **Multiple View Modes**
  - List view (current)
  - Kanban board (drag-and-drop)
  - Calendar view
  - Timeline/Gantt chart
  - Matrix view (Eisenhower Matrix)

- **Rich Text Editor**
  - Markdown support for descriptions
  - Code syntax highlighting
  - Embedded images and videos
  - File attachments (PDF, images, documents)
  - Voice notes

- **Themes & Customization**
  - Dark mode / Light mode
  - Custom color themes
  - Font size adjustments
  - Layout customization
  - Accessibility features (high contrast, screen reader support)

- **Drag & Drop**
  - Reorder todos
  - Move between categories/projects
  - Bulk operations

### Version 4.5 - Analytics & Insights

- **Productivity Dashboard**
  - Completion rate statistics
  - Time tracking per task
  - Productivity trends (daily, weekly, monthly)
  - Heatmap of activity
  - Goal tracking

- **Reports & Export**
  - Generate PDF reports
  - Export to CSV, JSON, Excel
  - Import from other todo apps (Todoist, Trello, Asana)
  - Backup and restore functionality

- **Time Management**
  - Pomodoro timer integration
  - Time estimates vs actual time
  - Time blocking
  - Focus mode (hide distractions)

### Version 5.0 - API & Integrations

- **RESTful API**
  - Django REST Framework integration
  - API authentication (JWT tokens)
  - Rate limiting
  - API documentation (Swagger/OpenAPI)
  - Webhooks for external integrations

- **Third-party Integrations**
  - Google Calendar sync
  - Slack notifications
  - Trello import/export
  - GitHub issues integration
  - Zapier/Make.com automation
  - Email-to-task (create todos via email)

- **Mobile Applications**
  - Progressive Web App (PWA)
  - Native iOS app (React Native/Flutter)
  - Native Android app
  - Offline mode with sync
  - Mobile notifications

### Version 5.5 - Enterprise Features

- **Advanced Analytics**
  - Team productivity metrics
  - Burndown charts
  - Velocity tracking
  - Resource allocation
  - Custom reporting

- **Workflow Automation**
  - Custom automation rules
  - Trigger-based actions
  - Status workflows
  - Approval processes
  - SLA tracking

- **Enterprise Security**
  - SSO (Single Sign-On)
  - LDAP/Active Directory integration
  - Audit logs
  - Data encryption at rest
  - Compliance (GDPR, SOC2)
  - Role-based access control (RBAC)

### Version 6.0 - Next-Generation Features

- **Voice & AI Assistants**
  - Voice commands (create, edit, complete todos)
  - Integration with Alexa, Google Assistant
  - AI task suggestions based on habits
  - Smart scheduling (find optimal time slots)
  - Predictive task completion

- **Gamification**
  - Achievement badges
  - Productivity streaks
  - Leaderboards (team competition)
  - Points and rewards system
  - Habit tracking

- **Advanced AI**
  - Context-aware suggestions
  - Automatic task breakdown
  - Smart deadline recommendations
  - Meeting notes to tasks conversion
  - Email to tasks (AI-powered extraction)

- **Blockchain & Web3** (experimental)
  - Decentralized task storage
  - NFT achievements
  - Token-based rewards
  - DAO-based team management

### Technical Improvements (Ongoing)

- **Performance Optimization**
  - Database query optimization
  - Caching (Redis)
  - CDN for static files
  - Lazy loading
  - Pagination improvements

- **Infrastructure**
  - Docker containerization
  - Kubernetes orchestration
  - CI/CD pipeline (GitHub Actions)
  - Automated testing (100% coverage goal)
  - Load balancing
  - Database sharding for scale

- **Code Quality**
  - Type hints (Python typing)
  - Code coverage > 90%
  - Linting (Ruff, Black)
  - Security scanning
  - Performance monitoring (Sentry)

## Implementation Priority

**Phase 1 (3-6 months)**: User authentication, categories/tags, priority levels, search/filter

**Phase 2 (6-12 months)**: Recurring tasks, notifications, subtasks, collaboration

**Phase 3 (12-18 months)**: API, mobile apps, integrations, analytics

**Phase 4 (18-24 months)**: AI features, enterprise features, advanced visualization

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Ensure all tests pass
6. Submit a pull request

## Author

Created as part of the AI-Dev-Zoomcamp

## Acknowledgments

- Built with Django framework
- UI styled with Bootstrap 5
- Managed with uv package manager
