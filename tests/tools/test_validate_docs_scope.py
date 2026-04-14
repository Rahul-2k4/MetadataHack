from tools.validate_docs_scope import find_disallowed_markdown, is_allowed_doc


def test_allows_docs_folder_markdown() -> None:
    assert is_allowed_doc("docs/demo-script.md") is True


def test_blocks_unrelated_markdown() -> None:
    assert is_allowed_doc("notes/random.md") is False


def test_reports_disallowed_markdown_list() -> None:
    paths = [
        "docs/index.md",
        "projects/main-submission/README.md",
        "notes/random.md",
        "assets/diagram.md",
    ]
    assert find_disallowed_markdown(paths) == ["notes/random.md"]
