from src.engine.verifier import is_valid_http_status
def test_status():
    assert is_valid_http_status(200)
    assert not is_valid_http_status(404)
