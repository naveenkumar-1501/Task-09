import pytest
from Login import SwagLabs
from Login import Data

#Setup the SwagLabs instance for reuse
@pytest.fixture(scope="module")
def setup_login():
    naveen = SwagLabs()
    naveen.login()
    yield naveen
    naveen.shutdown()

# POSITIVE TEST CASE: Validate Login
def test_positive_login(setup_login):
    naveen = setup_login
    assert naveen.fetch_url() == Data().DASHBOARD_URL
    print(f'SUCCESS : LogIn successful to Dashboard {Data().DASHBOARD_URL} ')

# NEGATIVE TEST CASE: Validate Login
def test_negative_login(setup_login):
    naveen = setup_login
    assert naveen.fetch_url() != "https://www.saucedemo.com/incorrect-login"
    print(f'SUCCESS : Negative test case passed !')

# POSITIVE TEST CASE : Validate URL
def test_positive_url(setup_login):
    naveen = setup_login
    assert naveen.fetch_url() == Data().DASHBOARD_URL
    print(f"SUCCESS : {Data().DASHBOARD_URL} is the valid URL")

# POSITIVE TEST CASE : Validate Title
def test_positive_title(setup_login):
    naveen = setup_login
    test_title = "Swag Labs"
    assert naveen.fetch_title() == test_title
    print(f"SUCCESS : {test_title} is valid Title")

# NEGATIVE TEST CASE : Validate URL
def test_negative_url(setup_login):
    naveen = setup_login
    test_url = "https://www.google.in/"
    assert naveen.fetch_url() != test_url
    print(f"SUCCESS : {test_url} is not the valid URL")

# NEGATIVE TEST CASE : Validate Title
def test_negative_title(setup_login):
    naveen = setup_login
    test_title = "Kingsman"
    assert naveen.fetch_title() != test_title
    print(f"SUCCESS : {test_title} is not a valid Title")

# NEW TEST CASE: Extract Page Content and Save to Text File
def test_extract_and_save_page_content(setup_login):
    naveen = setup_login
    page_content = naveen.extract_page_content()
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_content)
    print("SUCCESS: Webpage content has been saved to Webpage_task_11.txt")