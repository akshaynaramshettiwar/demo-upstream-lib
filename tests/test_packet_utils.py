def test_parse_packet():
    from upstream_lib.packet_utils import parse_packet
    result = parse_packet({"src": "1.1.1.1", "dst": "2.2.2.2"})
    assert result["src"] == "1.1.1.1"
