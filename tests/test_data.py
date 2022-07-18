from govsic.data.sections import SECTIONS


def get_all_section_domains():
    return [
        d
        for section in SECTIONS.values()
        for d in section.domain
    ]


def test_section_lut_length():
    assert len(SECTIONS) == 21

def test_section_lut_domain_uniqueness():
    domains = get_all_section_domains()
    assert len(domains) == len(set(domains))

def test_section_lut_domain_coverage():
    domains = get_all_section_domains()
    full = sum(range(domains[0], domains[-1]))

    chunks = [
        domains[i:i+2]
        for i in range(0, len(domains), 2)
    ]
    ranges = [range(c[0], c[1] + 1) for c in chunks]
    individual = sum(v for r in ranges for v in list(r)) - 99999

    assert full == individual
