def test_bake_project(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'skeletor'
    assert result.project.isdir()


def test_email(cookies):
    result = cookies.bake(extra_context={'name': 'Namey McNameFace'})
    assert result.exit_code == 0

    email = 'nameymcnameface'
    module_init = result.project.join('skeletor/__init__.py').read()
    assert email in module_init


def test_github_url(cookies):
    result = cookies.bake(extra_context={'name': 'Namey McNameFace'})
    assert result.exit_code == 0

    url = 'https://github.com/nameymcnameface/skeletor'
    module_init = result.project.join('skeletor/__init__.py').read()
    assert url in module_init