import pytest


@pytest.mark.skipif(
    not pytest.importorskip("openstudio", reason="openstudio is not installed"),
    reason="openstudio is not installed",
)
def test_set_energy_model_log_level():
    # Not implemented yet
    import openstudio

    try:
        openstudio.Logger.instance().standardOutLogger().setLogLevel(openstudio.Fatal)
        assert True
    except Exception as e:
        print("Failed to set OpenStudio log level.")
        assert False
