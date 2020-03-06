from unittest.mock import patch
import package.tool as tool


@patch('sys.argv', ['tool'])
def test_cli_usage(capsys):
    """Test if command_line_runner shows help when called without parameters."""
    tool.command_line_runner()
    out, err = capsys.readouterr()
    assert 'usage: tool [-h]' in out


def test_parser_asset_title():
    args = tool.get_parser().parse_args('asset'.split())
    assert args.asset == ['asset']




