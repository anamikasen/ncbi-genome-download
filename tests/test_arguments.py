"""Test the argument parsing."""
from ncbi_genome_download.core import argument_parser


def test_formats():
    """Test the -F/--format option works as expected."""
    args = ['-F', 'genbank', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.file_format == 'genbank'

    args = ['--format', 'fasta', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.file_format == 'fasta'

    args = ['--format', 'genbank,fasta', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.file_format == 'genbank,fasta'


def test_assembly_levels():
    """Test the -l/--assembly-level option works as expected."""
    args = ['-l', 'complete', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.assembly_level == 'complete'

    args = ['--assembly-level', 'chromosome', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.assembly_level == 'chromosome'

    args = ['--assembly-level', 'complete,chromosome', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.assembly_level == 'complete,chromosome'


def test_assembly_accessions():
    """Test the -A/--assembly-accessions option works as ecpected."""
    args = ['-A', 'GCF_000203835.1', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.assembly_accessions == 'GCF_000203835.1'

    args = ['--assembly-accessions', 'GCF_000203835.1,GCF_000444875.1', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.assembly_accessions == 'GCF_000203835.1,GCF_000444875.1'

    args = ['--assembly-accessions', 'some/path/here.txt', 'bacteria']
    parser = argument_parser()
    ns = parser.parse_args(args=args)
    assert ns.assembly_accessions == 'some/path/here.txt'
