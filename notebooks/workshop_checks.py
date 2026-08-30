"""Shared checking functions for the workshop notebooks.

The answer keys and feedback live here rather than in the exercise cells. The
notebooks call ``run_checks(name, locals())`` so students can run the checks
without seeing the expected values in the notebook source.
"""


class Check:
    def _result(self, passed, success, hint):
        if passed:
            print(f"✅ {success}")
        else:
            print("✗ Not correct. Open the hint if needed.")
        return passed

    def equal(self, actual, expected, success="Correct.", hint="Value does not match the expected result."):
        try:
            passed = actual == expected
            if hasattr(passed, "all"):
                passed = bool(passed.all())
        except Exception:
            passed = False
        return self._result(bool(passed), success, hint)

    def shape(self, actual, expected, success="Shape is correct.", hint="Shape is incorrect."):
        return self._result(tuple(actual.shape) == tuple(expected), success, hint)

    def columns(self, frame, expected, success="Columns are correct.", hint="Inspect frame.columns and select with a list of names."):
        return self._result(list(frame.columns) == list(expected), success, hint)

    def choice(self, actual, expected, explanations):
        normalised = str(actual).strip().upper()
        hint = explanations.get(normalised, "Choose one of the listed letters.")
        return self._result(normalised == expected.upper(), "Correct.", hint)


check = Check()

_CHECK_SOURCES = {
    '01_lexical_decision_pandas_cell_6': 'check.shape(trials, (1659, 28), hint="Read the CSV at data_path with pandas.")',
    '01_lexical_decision_pandas_cell_11': 'check.equal(n_trials, 1659, hint="The first element of trials.shape is the number of rows.")\ncheck.equal(n_participants, 21, hint="Count unique values in Subject with .nunique().")\ncheck.equal(n_words, 79, hint="Count unique values in Word with .nunique().")',
    '01_lexical_decision_pandas_cell_16': 'check.columns(\n    analysis_columns,\n    ["Subject", "Word", "RT", "NativeLanguage", "Correct", "Frequency", "Length", "Class"],\n)\ncheck.equal(len(analysis_columns), 1659, hint="Column selection should retain every trial.")',
    '01_lexical_decision_pandas_cell_21': 'check.equal(n_correct, 1594, hint="Use value_counts() or compare Correct with \'correct\'.")\ncheck.equal(n_incorrect, 65, hint="Use value_counts() or compare Correct with \'incorrect\'.")\ncheck.equal(set(correct_trials["Correct"]), {"correct"}, hint="Filter rows where Correct equals \'correct\'.")',
    '01_lexical_decision_pandas_cell_29': 'check.equal(\n    round(float(correct_trials["RT_ms"].median()), 1),\n    571.0,\n    hint="Use np.exp(correct_trials[\'RT\']).",\n)',
    '01_lexical_decision_pandas_cell_34': 'check.equal(round(float(median_rt.loc["English"]), 1), 541.5, hint="Group correct_trials by NativeLanguage and take the median of RT_ms.")\ncheck.equal(round(float(median_rt.loc["Other"]), 1), 616.5, hint="Group correct_trials by NativeLanguage and take the median of RT_ms.")',
    '01_lexical_decision_pandas_cell_42': 'check.equal(len(word_summary), 79, hint="Group by Word, Frequency, and Length.")\ncheck.columns(word_summary, ["Word", "Frequency", "Length", "mean_rt_ms"])',
    '02_eeg_arrays_cell_6': 'check.shape(eeg, (14980, 15), hint="The completed DataFrame should have 14 channels and one label column.")\ncheck.equal(str(eeg["eyeDetection"].dtype).startswith("int"), True, hint="Convert eyeDetection to integers.")',
    '02_eeg_arrays_cell_11': 'check.choice(\n    answer_shape,\n    "B",\n    {\n        "A": "That counts only features and forgets the target column.",\n        "B": "",\n        "C": "pandas uses rows × columns, not columns × rows.",\n    },\n)',
    '02_eeg_arrays_cell_16': 'check.shape(X, (14980, 14), hint="Drop the eyeDetection label from the feature table.")\ncheck.equal(y.name, "eyeDetection", hint="Select the label as a Series with one column name.")',
    '02_eeg_arrays_cell_24': 'check.shape(signals, (14980, 14))\ncheck.shape(o1_excerpt, (100,), hint="Select rows 0:100 and one channel column.")',
    '02_eeg_arrays_cell_29': 'check.equal(eyes_open.shape[1], 14, hint="Use a Boolean row mask; retain every channel.")\ncheck.equal(eyes_closed.shape[1], 14, hint="Use a Boolean row mask; retain every channel.")\ncheck.equal(len(eyes_open) + len(eyes_closed), len(signals), hint="Every sample should belong to exactly one state.")',
    '02_eeg_arrays_cell_34': 'check.shape(open_channel_means, (14,), hint="Rows are samples. Which axis should disappear?")\ncheck.shape(closed_channel_means, (14,), hint="Rows are samples. Which axis should disappear?")',
    '02_eeg_arrays_cell_46': 'check.shape(pseudo_epochs, (100, 14, 140), hint="First reshape to (100, 140, 14), then transpose the final two axes.")',
    '03_model_workflow_cell_6': 'check.shape(trials, (1659, 30))\ncheck.equal(int(trials["is_correct"].sum()), 1594)\ncheck.equal(round(float(trials["RT_ms"].median()), 1), 570.0)',
    '03_model_workflow_cell_11': 'check.shape(participants, (21, 6))\ncheck.columns(participants, ["Subject", "NativeLanguage", "mean_rt_ms", "accuracy", "mean_frequency", "mean_length"])',
    '03_model_workflow_cell_16': 'check.shape(X, (21, 4))\ncheck.shape(y, (21,))\ncheck.equal(set(y), {"English", "Other"})',
    '03_model_workflow_cell_21': 'check.shape(X_train, (14, 4))\ncheck.shape(X_test, (7, 4))\ncheck.equal(set(y_train), {"English", "Other"})',
    '03_model_workflow_cell_26': 'check.shape(predictions, (7,))\ncheck.equal(set(predictions).issubset({"English", "Other"}), True)',
    '03_model_workflow_cell_31': 'check.shape(matrix, (2, 2))\ncheck.equal(int(matrix.sum()), 7)\ncheck.equal(n_correct_predictions, int((predictions == y_test).sum()))',
    '04_nlp_text_features_cell_7': 'check.shape(counts, (6, 24))\ncheck.equal(len(terms), 24)\ncheck.equal("attention" in terms, True)',
    '04_nlp_text_features_cell_12': 'check.equal(document_lengths.tolist(), [5, 5, 5, 5, 5, 5])\ncheck.equal(reaction_counts.tolist(), [0, 1, 0, 0, 0, 1])',
    '04_nlp_text_features_cell_17': 'check.shape(tfidf, (6, 24))\ncheck.shape(similarities, (6, 6))\ncheck.equal(bool(np.allclose(np.diag(similarities), 1.0)), True)',
    '04_nlp_text_features_cell_22': 'check.shape(document_vectors, (6, 4))',
    '00_python_warmup_predict': 'check.choice(answer_1, "B", {"A": "Assignment gives two names to the same list.", "B": "", "C": "Appending to a list is allowed."})',
    '00_python_warmup_arithmetic': 'check.equal(total, 42, success="The total is correct.", hint="Multiply price by quantity.")',
    '00_python_warmup_string': 'check.equal(clean_word, "python", success="The string is cleaned.", hint="Strip whitespace, then change the case.")',
    '00_python_warmup_function': 'passed = check.equal(is_even(8), True, success="The even case works.", hint="Use the remainder after division by two.")\nif passed:\n    check.equal(is_even(7), False, success="The odd case works.", hint="Odd numbers have remainder one.")',
    '00_python_warmup_list': 'check.equal(squares, [1, 4, 9, 16], success="The squares are correct.", hint="Use range(1, 5); the stop value is excluded.")',
    '00_python_warmup_dictionary': 'check.equal(course, "Python", success="The dictionary value is correct.", hint="Use person[\\"course\\"].")',
}


def run_checks(name, namespace):
    """Run one notebook's hidden answer checks against its current variables."""
    try:
        source = _CHECK_SOURCES[name]
    except KeyError as exc:
        raise ValueError(f"Unknown workshop check: {name}") from exc
    exec(source, {"check": check}, namespace)
