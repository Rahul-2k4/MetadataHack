from tools.validate_docs_scope import is_allowed_doc


def test_allows_docs_folder_markdown() -> None:
    assert is_allowed_doc("docs/demo-script.md") is True


def test_blocks_unrelated_markdown() -> None:
    assert is_allowed_doc("notes/random.md") is False
