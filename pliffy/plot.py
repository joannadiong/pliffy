from typing import NamedTuple, Tuple, Union, Literal

from pliffy import estimate


class _ABD(NamedTuple):
    """Helper namedtuple used by PlotInfo"""
    a: Union[str, int] = None
    b: Union[str, int] = None
    diff: Union[str, int] = None


class PlotInfo(NamedTuple):
    """Information used to generate plot

    Includes sensible defaults to reduce need for user input
    """
    colors: _ABD = _ABD(a="black", b="black", diff="black")
    symbol_size_summary: _ABD = _ABD(a=3, b=3, diff=3)
    symbol_size_subject: _ABD = _ABD(a=1, b=1, diff=1)
    symbols: _ABD = _ABD(a="o", b="o", diff="^")
    x_values: _ABD = _ABD(a=1, b=2, diff=3)
    horiz_line_to_diffs: bool = False
    join_ab_means: bool = True
    ax1_y_range: Tuple = None
    ax2_y_range: Tuple = None
    ax1_y_ticks: Tuple = None
    ax2_y_ticks: Tuple = None
    ab_sub_label: str = None
    bottom_box: bool = False
    alpha: float = 0.7


class PliffyData(NamedTuple):
    """Data and details required from user

    See :function:`pliffy.estimates.calc` parameters for details.
    """
    a: list = None
    b: list = None
    design: Literal["paired", "unpaired"] = "unpaired"
    measure_units: str = "au"
    ci_percentage: int = 95


def plot(pliffy_data: PliffyData, plot_info: PlotInfo = PlotInfo()):
    """Main user interfact to generate plot
    """
    estimates_diff, diff_vals = estimate.calc(pliffy_data)

