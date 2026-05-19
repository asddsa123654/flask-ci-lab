def test_hello_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_hello_message(client):
    response = client.get('/')
    data = response.get_json()
    assert data['message'] == 'Hello, DevOps!'

def test_health_status_code(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_health_response(client):
    response = client.get('/health')
    data = response.get_json()
    assert 'status' in data
    assert data['status'] == 'healthy'

def test_info_default_values(client):
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['version'] == '1.0.0'
    assert data['environment'] == 'development'

def test_info_custom_env(client, monkeypatch):
    monkeypatch.setenv('APP_VERSION', '2.5.0')
    monkeypatch.setenv('ENVIRONMENT', 'production')
    response = client.get('/info')
    data = response.get_json()
    assert data['version'] == '2.5.0'
    assert data['environment'] == 'production'

def test_not_found(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_method_not_allowed(client):
    response = client.post('/')
    assert response.status_code == 405

def test_echo_success(client):
    response = client.get('/api/echo?message=hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['echo'] == 'hello'
    assert data['length'] == 5

def test_echo_missing_param(client):
    response = client.get('/api/echo')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'message parameter is required'

def test_echo_empty_string(client):
    response = client.get('/api/echo?message=')
    assert response.status_code == 200
    data = response.get_json()
    assert data['echo'] == ''
    assert data['length'] == 0
