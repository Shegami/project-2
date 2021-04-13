from django.test import TestCase
from todo.models import NotCompletedTasks, CompletedTasks
from datetime import date
from todo.views import delete_task, task_up_down, task_completed


class HomeTest(TestCase):
    def test_home_response(self):
        result = self.client.get('/')
        TestCase.assertEqual(self, result.status_code, 200)


class GetTasksTest(TestCase):
    def test_list_response(self):
        result = self.client.get('/get/')
        TestCase.assertEqual(self, result.status_code, 200)


class CreateTaskTest(TestCase):
    def test_list_response(self):
        result = self.client.get('/create/')
        TestCase.assertEqual(self, result.status_code, 200)


class CreateModelTest(TestCase):
    def setUp(self):
        NotCompletedTasks.objects.create(
            name='TEST'
        )

    def test_create_model(self):
        model = NotCompletedTasks.objects.get(pk=1)
        name = model.name
        priority = model.priority
        order = model.order
        create_date = model.create_date
        self.assertEqual(name, 'TEST')
        self.assertEqual(order, 1)
        self.assertEqual(priority, 1)
        self.assertEqual(create_date, date.today())


class EditModelTest(TestCase):
    def setUp(self):
        NotCompletedTasks.objects.create(
            name='TEST'
        )

    def test_edit_task_response(self):
        result = self.client.get('/edit/1')
        TestCase.assertEqual(self, result.status_code, 200)


class DeleteModelTest(TestCase):
    def setUp(self):
        NotCompletedTasks.objects.create(
            name='TEST'
        )

    def test_delete_model(self):
        model = NotCompletedTasks.objects.filter(pk=1).exists()
        self.assertEqual(model, True)
        delete_task(request=None, task_id=1)
        model = NotCompletedTasks.objects.filter(pk=1).exists()
        self.assertEqual(model, False)


class TaskUpTest(TestCase):
    def setUp(self):
        NotCompletedTasks.objects.create(name='TEST')
        NotCompletedTasks.objects.create(name='TEST2')
        NotCompletedTasks.objects.create(name='TEST3')

    def test_task_up(self):
        task_to_move = NotCompletedTasks.objects.get(pk=2)
        task_to_down = NotCompletedTasks.objects.get(pk=1)
        self.assertEqual(task_to_move.order, 2)
        self.assertEqual(task_to_down.order, 1)
        task_up_down(request=None, task_id=2, button='up')
        task_to_move = NotCompletedTasks.objects.get(pk=2)
        task_to_down = NotCompletedTasks.objects.get(pk=1)
        self.assertEqual(task_to_move.order, 1)
        self.assertEqual(task_to_down.order, 2)


class TaskDownTest(TestCase):
    def setUp(self):
        NotCompletedTasks.objects.create(name='TEST')
        NotCompletedTasks.objects.create(name='TEST2')
        NotCompletedTasks.objects.create(name='TEST3')

    def test_task_down(self):
        task_to_move = NotCompletedTasks.objects.get(pk=2)
        task_to_up = NotCompletedTasks.objects.get(pk=3)
        self.assertEqual(task_to_move.order, 2)
        self.assertEqual(task_to_up.order, 3)
        task_up_down(request=None, task_id=2, button='down')
        task_to_move = NotCompletedTasks.objects.get(pk=2)
        task_to_up = NotCompletedTasks.objects.get(pk=3)
        self.assertEqual(task_to_move.order, 3)
        self.assertEqual(task_to_up.order, 2)


class CompleteTaskTest(TestCase):
    def setUp(self):
        NotCompletedTasks.objects.create(
            name='TEST'
        )

    def test_complete_task(self):
        model = NotCompletedTasks.objects.filter(pk=1).exists()
        self.assertEqual(model, True)
        task_completed(request=None, task_id=1)
        model = CompletedTasks.objects.filter(pk=1).exists()
        self.assertEqual(model, True)
