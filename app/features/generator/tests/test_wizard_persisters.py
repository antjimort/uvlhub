from werkzeug.datastructures import MultiDict

from app.features.generator.wizard import (
    _apply_step2_levels,
    _apply_step3_tree,
    _apply_step4_constraints,
    _apply_step5_attributes,
)


def test_apply_step2_type_enables_arithmetic():
    params = {}
    form = MultiDict({"type_level": "on"})

    _apply_step2_levels(params, form)

    assert params["BOOLEAN_LEVEL"] is True
    assert params["TYPE_LEVEL"] is True
    assert params["ARITHMETIC_LEVEL"] is True


def test_apply_step3_normalizes_relation_distribution():
    params = {"GROUP_CARDINALITY": False, "FEATURE_CARDINALITY": False}
    form = MultiDict(
        {
            "num_features_min": "10",
            "num_features_max": "20",
            "max_tree_depth": "5",
            "dist_optional": "2",
            "dist_mandatory": "2",
            "dist_alternative": "2",
            "dist_or": "2",
        }
    )

    _apply_step3_tree(params, form)

    total = (
        params["DIST_OPTIONAL"]
        + params["DIST_MANDATORY"]
        + params["DIST_ALTERNATIVE"]
        + params["DIST_OR"]
        + params["DIST_GROUP_CARDINALITY"]
    )
    assert total == 1.0


def test_apply_step4_disables_arithmetic_probs_when_arithmetic_off():
    params = {
        "ARITHMETIC_LEVEL": False,
        "TYPE_LEVEL": False,
        "STRING_CONSTRAINTS": False,
        "MAX_FEATURES": 20,
    }
    form = MultiDict(
        {
            "num_constraints_min": "1",
            "num_constraints_max": "5",
            "extra_constraint_repr": "1",
            "vars_per_ctc_min": "1",
            "vars_per_ctc_max": "5",
            "prob_not": "0.3",
            "prob_and": "1",
            "prob_or": "0",
            "prob_implies": "0",
            "prob_equiv": "0",
            "ctc_dist_boolean": "1",
        }
    )

    _apply_step4_constraints(params, form)

    assert params["PROB_SUM"] == 0.0
    assert params["PROB_EQUALS"] == 0.0
    assert params["CTC_DIST_BOOLEAN"] == 1.0
    assert params["CTC_DIST_INTEGER"] == 0.0


def test_apply_step5_random_attrs_normalizes_distribution():
    params = {"ARITHMETIC_LEVEL": True, "TYPE_LEVEL": True}
    form = MultiDict(
        {
            "random_attributes": "on",
            "min_attributes": "1",
            "max_attributes": "4",
            "dist_boolean_atr": "1",
            "dist_integer_atr": "1",
            "dist_real_atr": "1",
            "dist_string_atr": "1",
        }
    )

    _apply_step5_attributes(params, form)

    total = (
        params["ATTR_DIST_BOOLEAN"]
        + params["ATTR_DIST_INTEGER"]
        + params["ATTR_DIST_REAL"]
        + params["ATTR_DIST_STRING"]
    )

    assert total == 1.0


def test_apply_step3_normalizes_relation_distribution_with_group_cardinality():
    params = {"GROUP_CARDINALITY": True, "FEATURE_CARDINALITY": False}
    form = MultiDict(
        {
            "num_features_min": "10",
            "num_features_max": "20",
            "max_tree_depth": "5",
            "dist_optional": "1",
            "dist_mandatory": "1",
            "dist_alternative": "1",
            "dist_or": "1",
            "dist_group_cardinality": "1",
            "group_cardinality_min": "1",
            "group_cardinality_max": "4",
        }
    )

    _apply_step3_tree(params, form)

    total = (
        params["DIST_OPTIONAL"]
        + params["DIST_MANDATORY"]
        + params["DIST_ALTERNATIVE"]
        + params["DIST_OR"]
        + params["DIST_GROUP_CARDINALITY"]
    )

    assert total == 1.0
    assert params["DIST_GROUP_CARDINALITY"] > 0.0
    assert params["GROUP_CARDINALITY_MIN"] == 1
    assert params["GROUP_CARDINALITY_MAX"] == 4


def test_apply_step5_masks_unavailable_attribute_types_when_levels_are_off():
    params = {"ARITHMETIC_LEVEL": False, "TYPE_LEVEL": False}
    form = MultiDict(
        {
            "random_attributes": "on",
            "min_attributes": "1",
            "max_attributes": "4",
            "dist_boolean": "1",
            "dist_integer": "1",
            "dist_real": "1",
            "dist_string": "1",
        }
    )

    _apply_step5_attributes(params, form)

    assert params["ATTR_DIST_BOOLEAN"] == 1.0
    assert params["ATTR_DIST_INTEGER"] == 0.0
    assert params["ATTR_DIST_REAL"] == 0.0
    assert params["ATTR_DIST_STRING"] == 0.0