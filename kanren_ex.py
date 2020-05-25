from kanren import run
from kanren.util import unique
from unification import reify


def goalify(func, expected_result=True):
    def goalify_goal_constructor(*args):
        """Construct a goal for this relation."""

        def goalify_goal(S):
            """
            This is the goal that's generated.

            Parameters
            ----------
            S: Mapping
                The miniKanren state (e.g. unification mappings/`dict`).

            Yields
            ------
            miniKanren states.

            """
            nonlocal args

            # 2. If you only want to confirm something in/about the state, `S`, then
            # simply `yield` it if the condition(s) are met:
            args_rf = reify(args, S)

            if func(*args_rf) == expected_result:
                yield S
            else:
                # If the condition isn't met, end the stream by returning/not
                # `yield`ing anything.
                return

        # Finally, return the constructed goal.
        return goalify_goal

    return goalify_goal_constructor


def run_all(vars_, *goals_):
    return run(0, vars_, *goals_, results_filter=unique)


def run_is_true(*goals_):
    return bool(run(1, True, *goals_))


def run_any(vars_, *goals_):
    return run(1, vars_, *goals_)
