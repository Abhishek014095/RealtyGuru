def test_bing(driver):
    driver.get("https://www.bing.com")
    assert "Bing" in driver.title
