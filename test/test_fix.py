from src.generator import format_table_cell

def test_format_table_cell_trailing_newline():
    # Case with trailing newline
    val = "line 1\nline 2\n"
    # Old split("\n") would give ["line 1", "line 2", ""]
    # New splitlines() gives ["line 1", "line 2"]
    out = format_table_cell(val)
    assert out == "| line 1\n| line 2"

def test_format_table_cell_no_trailing_newline():
    val = "line 1\nline 2"
    out = format_table_cell(val)
    assert out == "| line 1\n| line 2"

def test_format_table_cell_code_trailing_newline():
    val = "line 1\nline 2\n"
    out = format_table_cell(val, is_code=True)
    assert out == "| ``line 1``\n| ``line 2``"
