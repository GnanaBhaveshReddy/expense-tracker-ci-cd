from db import add_expense,get_expenses,init_db

def test_add_expense():
    init_db()
    add_expense('Test',100,'2025-11-05')
    data = get_expenses()
    assert len(data) > 0
