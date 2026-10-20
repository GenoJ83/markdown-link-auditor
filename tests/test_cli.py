from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['docs/', '--check-external'])
    assert args.path == 'docs/'
    assert args.check_external
