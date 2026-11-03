from app import app, tasks


def test_health():
    assert app.test_client().get("/health").data == b"ok"


def test_add_and_delete():
    tasks.clear()
    c = app.test_client()
    c.post("/add", data={"title": "Learn EKS"})
    assert len(tasks) == 1
    c.get("/delete/0")
    assert len(tasks) == 0


def test_mark_done():
    tasks.clear()
    c = app.test_client()
    c.post("/add", data={"title": "Push to ECR"})
    c.get("/done/0")
    assert tasks[0].done is True
