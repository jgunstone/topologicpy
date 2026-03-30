import pytest

try:
    import honeybee_energy
    import openstudio
except ImportError as e:
    print("honeybee-energy is not installed. Please install it to run this test.")


@pytest.mark.skipif(
    not pytest.importorskip("openstudio", reason="openstudio is not installed"),
    reason="openstudio is not installed",
)
def test_set_energy_model_log_level():
    # Not implemented yet

    try:
        openstudio.Logger.instance().standardOutLogger().setLogLevel(openstudio.Fatal)
        assert True
    except Exception as e:
        print("Failed to set OpenStudio log level.")
        assert False
