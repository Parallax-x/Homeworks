import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=10)
    responce = client.get('/api/v1/courses/1/')
    data = responce.json()
    assert data['id'] == courses[0].id


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    responce = client.get('/api/v1/courses/')
    data = responce.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)
    ids = [course.id for course in courses]
    responce = client.get(f'/api/v1/courses/?id={ids[1]}')
    res = responce.json()
    assert res[0]['id'] == courses[1].id


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    responce = client.get('/api/v1/courses/', {'name': courses[0].name})
    res = responce.json()
    assert res[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    res = client.post('/api/v1/courses/', {'name': 'Python'})
    assert res.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    ids = [course.id for course in courses]
    res = client.patch(f'/api/v1/courses/{ids[1]}/', {'name': 'Test_name'})
    data = res.json()
    assert res.status_code == 200
    assert data['name'] == Course.objects.get(id=ids[1]).name


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    ids = [course.id for course in courses]
    res = client.delete(f'/api/v1/courses/{ids[0]}/')
    assert res.status_code == 204
    assert Course.objects.count() == count - 1

