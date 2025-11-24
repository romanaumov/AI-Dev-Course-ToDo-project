from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Todo
from .forms import TodoForm


class TodoModelTests(TestCase):
    """Test cases for the Todo model"""

    def test_create_todo_with_all_fields(self):
        """Test creating a todo with all fields populated"""
        due_date = timezone.now() + timedelta(days=1)
        todo = Todo.objects.create(
            title="Test Todo",
            description="Test Description",
            due_date=due_date,
            is_completed=False
        )
        self.assertEqual(todo.title, "Test Todo")
        self.assertEqual(todo.description, "Test Description")
        self.assertEqual(todo.due_date, due_date)
        self.assertFalse(todo.is_completed)

    def test_create_todo_with_only_title(self):
        """Test creating a todo with only required field (title)"""
        todo = Todo.objects.create(title="Minimal Todo")
        self.assertEqual(todo.title, "Minimal Todo")
        self.assertEqual(todo.description, "")
        self.assertIsNone(todo.due_date)
        self.assertFalse(todo.is_completed)

    def test_todo_default_is_completed_false(self):
        """Test that is_completed defaults to False"""
        todo = Todo.objects.create(title="Test")
        self.assertFalse(todo.is_completed)

    def test_todo_str_returns_title(self):
        """Test that __str__ method returns the title"""
        todo = Todo.objects.create(title="My Todo")
        self.assertEqual(str(todo), "My Todo")

    def test_todo_ordering(self):
        """Test that todos are ordered by created_at descending (newest first)"""
        todo1 = Todo.objects.create(title="First")
        todo2 = Todo.objects.create(title="Second")
        todo3 = Todo.objects.create(title="Third")

        todos = Todo.objects.all()
        self.assertEqual(todos[0], todo3)
        self.assertEqual(todos[1], todo2)
        self.assertEqual(todos[2], todo1)

    def test_todo_timestamps(self):
        """Test that created_at and updated_at are set automatically"""
        todo = Todo.objects.create(title="Test")
        self.assertIsNotNone(todo.created_at)
        self.assertIsNotNone(todo.updated_at)


class TodoFormTests(TestCase):
    """Test cases for the TodoForm"""

    def test_valid_form_with_all_fields(self):
        """Test form with all fields is valid"""
        form_data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'due_date': '2025-12-31T23:59'
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_valid_form_with_only_title(self):
        """Test form with only required field is valid"""
        form_data = {'title': 'Test Todo'}
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_without_title(self):
        """Test form without title is invalid"""
        form_data = {'description': 'Description only'}
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_due_date_optional(self):
        """Test that due_date is optional"""
        form_data = {'title': 'Test', 'due_date': ''}
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())


class TodoViewTests(TestCase):
    """Test cases for Todo views"""

    def setUp(self):
        """Set up test client and sample data"""
        self.client = Client()
        self.todo1 = Todo.objects.create(
            title="Test Todo 1",
            description="Description 1"
        )
        self.todo2 = Todo.objects.create(
            title="Test Todo 2",
            description="Description 2",
            is_completed=True
        )

    def test_todo_list_view_get(self):
        """Test that todo list view displays all todos"""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo 1")
        self.assertContains(response, "Test Todo 2")
        self.assertEqual(len(response.context['todos']), 2)

    def test_todo_create_view_get(self):
        """Test that create view displays the form"""
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create')
        self.assertIsInstance(response.context['form'], TodoForm)

    def test_todo_create_view_post_valid(self):
        """Test creating a todo with valid data"""
        data = {
            'title': 'New Todo',
            'description': 'New Description',
            'due_date': '2025-12-31T23:59'
        }
        response = self.client.post(reverse('todo_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())

    def test_todo_create_view_post_invalid(self):
        """Test creating a todo with invalid data shows errors"""
        data = {'description': 'No title'}
        response = self.client.post(reverse('todo_create'), data)
        self.assertEqual(response.status_code, 200)  # No redirect
        self.assertFalse(Todo.objects.filter(description='No title').exists())

    def test_todo_edit_view_get(self):
        """Test that edit view displays form with existing data"""
        response = self.client.get(reverse('todo_edit', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit')
        self.assertEqual(response.context['form'].instance, self.todo1)

    def test_todo_edit_view_post_valid(self):
        """Test updating a todo with valid data"""
        data = {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'due_date': ''
        }
        response = self.client.post(
            reverse('todo_edit', args=[self.todo1.pk]),
            data
        )
        self.assertEqual(response.status_code, 302)  # Redirect
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated Todo')

    def test_todo_delete_view_get(self):
        """Test that delete view shows confirmation"""
        response = self.client.get(reverse('todo_delete', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo1.title)
        self.assertContains(response, 'Delete')

    def test_todo_delete_view_post(self):
        """Test deleting a todo"""
        todo_pk = self.todo1.pk
        response = self.client.post(reverse('todo_delete', args=[todo_pk]))
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertFalse(Todo.objects.filter(pk=todo_pk).exists())

    def test_todo_toggle_view(self):
        """Test toggling todo completion status"""
        # Toggle to completed
        response = self.client.get(reverse('todo_toggle', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertTrue(self.todo1.is_completed)

        # Toggle back to incomplete
        response = self.client.get(reverse('todo_toggle', args=[self.todo1.pk]))
        self.todo1.refresh_from_db()
        self.assertFalse(self.todo1.is_completed)

    def test_edit_nonexistent_todo_returns_404(self):
        """Test that editing non-existent todo returns 404"""
        response = self.client.get(reverse('todo_edit', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_todo_returns_404(self):
        """Test that deleting non-existent todo returns 404"""
        response = self.client.get(reverse('todo_delete', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_toggle_nonexistent_todo_returns_404(self):
        """Test that toggling non-existent todo returns 404"""
        response = self.client.get(reverse('todo_toggle', args=[9999]))
        self.assertEqual(response.status_code, 404)


class TodoIntegrationTests(TestCase):
    """Integration tests for complete workflows"""

    def setUp(self):
        """Set up test client"""
        self.client = Client()

    def test_complete_todo_workflow(self):
        """Test complete workflow: create -> edit -> toggle -> delete"""
        # Create a todo
        create_data = {
            'title': 'Integration Test Todo',
            'description': 'Testing full workflow',
            'due_date': '2025-12-31T23:59'
        }
        response = self.client.post(reverse('todo_create'), create_data)
        self.assertEqual(response.status_code, 302)

        # Verify todo exists
        todo = Todo.objects.get(title='Integration Test Todo')
        self.assertFalse(todo.is_completed)

        # Edit the todo
        edit_data = {
            'title': 'Updated Integration Test',
            'description': 'Updated description',
            'due_date': ''
        }
        response = self.client.post(reverse('todo_edit', args=[todo.pk]), edit_data)
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated Integration Test')

        # Toggle to completed
        response = self.client.get(reverse('todo_toggle', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)

        # Delete the todo
        response = self.client.post(reverse('todo_delete', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(pk=todo.pk).exists())

    def test_multiple_todos_display(self):
        """Test that multiple todos are displayed correctly"""
        # Create multiple todos
        Todo.objects.create(title="Todo 1", is_completed=False)
        Todo.objects.create(title="Todo 2", is_completed=True)
        Todo.objects.create(title="Todo 3", is_completed=False)

        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['todos']), 3)
        self.assertContains(response, "Todo 1")
        self.assertContains(response, "Todo 2")
        self.assertContains(response, "Todo 3")
