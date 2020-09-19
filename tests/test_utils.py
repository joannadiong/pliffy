import pytest

from pliffy import utils


def test_abd_default():
    abd = utils.ABD()
    assert (abd.a, abd.b, abd.diff) == (None, None, None)


def test_abd_asignement():
    abd = utils.ABD(1, 2, 'milk')
    assert (abd.a, abd.b, abd.diff) == (1, 2, 'milk')


def test_abd_attribute_error():
    abd = utils.ABD()
    with pytest.raises(
            AttributeError,
            match="can't set attribute",):
        abd.a = 1


def test_pliffy_info_defaults(pliffy_info_abd_default):
    actual = utils.PliffyInfoABD()
    assert actual._asdict() == pliffy_info_abd_default


def test_pliffy_info_set_data(pliffy_info_abd_custom):
    actual = utils.PliffyInfoABD(
        data_a=[1, 2, 3, 4, 5],
        data_b=[11, 22, 33, 44, 55],
        ci_percentage=99,
        design="paired",
        measure_units="Amplitude (Volts)",
        xtick_labels=utils.ABD(a="Biceps", b="Triceps", diff="Effect"),
        decimals=4,
        plot_name="arm",
        save=True,
        save_path="/home/martin/Desktop/",
        save_type="svg",
        dpi=600,
        marker=utils.ABD(a="*", b="v", diff="."),
        marker_color=utils.ABD(a="tab:red", b="tab:blue", diff="tab:green"),
        summary_marker_size=utils.ABD(a=6, b=4, diff=2),
        raw_marker_size=utils.ABD(a=6, b=5, diff=3),
        raw_marker_transparency=0.1,
        paired_data_joining_lines=False,
        paired_data_line_color="grey",
        paired_data_line_width=2,
        paired_line_transparency=0.3,
        paired_data_plot_raw_diff=False,
        ci_line_width=2,
        fontsize=12,
        show=False,
    )
    assert actual._asdict() == pliffy_info_abd_custom