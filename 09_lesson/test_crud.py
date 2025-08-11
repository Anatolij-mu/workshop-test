from models import Student, Course


def test_create_student(db_session):
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(
        email="ivan@example.com").first()
    assert student is not None
    assert student.name == "Иван Иванов"
    assert student.is_active is True

    db_session.delete(student)
    db_session.commit()


def test_update_course(db_session):
    new_course = Course(
        title="Математика", description="Базовый курс математики")
    db_session.add(new_course)
    db_session.commit()

    course = db_session.query(Course).filter_by(title="Математика").first()
    course.description = "Продвинутый курс математики"
    db_session.commit()

    updated_course = db_session.query(Course).filter_by(
        title="Математика").first()
    assert updated_course.description == "Продвинутый курс математики"

    db_session.delete(updated_course)
    db_session.commit()


def test_soft_delete_student(db_session):
    new_student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(
        email="petr@example.com").first()
    student.is_deleted = True
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(
        email="petr@example.com").first()
    assert deleted_student.is_deleted is True

    active_students = db_session.query(Student).filter_by(
        is_deleted=False).all()
    assert deleted_student not in active_students

    db_session.delete(deleted_student)
    db_session.commit()
