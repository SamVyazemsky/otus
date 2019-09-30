class TestSuit:
    def test_1(self, app):
        app.test_smth()
        assert True

    def test_2(self, app):
        app.test_smth()
        assert True