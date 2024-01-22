# -*- coding: utf-8 -*-
"""Natural language processing functions for the OpenAI API."""

import re
import string

import Levenshtein
import spacy


nlp = spacy.load("en_core_web_sm")


def clean_prompt(prompt: str) -> str:
    """
    Clean up the prompt by adding spaces before capital letters.
    Example: converts "WhoIsLawrenceMcDaniel" to "Who Is Lawrence McDaniel"
    """
    retval = []
    for word in prompt.split():
        word = word.translate(str.maketrans("", "", string.punctuation))
        doc = nlp(word)
        words = re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", word)).split()
        words = (
            ["".join(re.findall("[a-zA-Z]+", w)) for w in words]
            if not any(ent.label_ in ["PERSON", "ORG"] for ent in doc.ents)
            else [word.title()]
        )
        retval.extend(words)
    retval = " ".join(retval)
    return retval


def lower_case_splitter(string_of_words: str) -> list:
    """Split a string on spaces and return a list of lowercase words."""
    return [word.lower() for word in string_of_words.split()]


def simple_search(prompt: str, refers_to: str) -> bool:
    """Check if the prompt contains the target string."""
    prompt_words = lower_case_splitter(prompt)
    token_count = len(refers_to.split())
    found_count = 0
    for token in lower_case_splitter(refers_to):
        if token in prompt_words:
            found_count += 1
        if found_count >= token_count:
            return True
    return False


def within_levenshtein_distance(prompt: str, refers_to: str, threshold: int = 3) -> bool:
    """Check if the prompt is within the given Levenshtein distance of the target string."""
    words = lower_case_splitter(prompt)
    names = [word for word in words if word.istitle()]
    for name in names:
        distance = Levenshtein.distance(refers_to, name)
        if distance <= threshold:
            return True
    return False


def does_refer_to(prompt: str, refers_to: str, threshold=3) -> bool:
    """Check if the prompt refers to the given string."""

    prompt = clean_prompt(prompt)

    if simple_search(prompt, refers_to):
        return True

    if within_levenshtein_distance(prompt, refers_to, threshold):
        return True

    # bust. we didn't find the target string in the prompt
    return False
