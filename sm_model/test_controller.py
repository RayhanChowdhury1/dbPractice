class TestController:
    @pytest.fixture(scope="class",autouse=True
                    )
    def test_set_current_user(self):
        assert False

    def test_get_user_names(self):
        assert False

    def test_get_posts(self):
        assert False
