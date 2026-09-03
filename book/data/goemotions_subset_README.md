# GoEmotions workshop subset

`goemotions_workshop.csv` contains 1,000 examples sampled from the filtered training
split of GoEmotions: 250 single-label examples from each of `anger`, `fear`, `joy`, and
`sadness`.

The subset was generated deterministically with
`scripts/build_goemotions_subset.py`. Comments between 5 and 35 whitespace-separated
words were retained. A conservative keyword and URL screen was applied to reduce
unsuitable classroom content. Screening cannot guarantee that every reader will find
every example comfortable; instructors should review the file for their own context.

The `source_id` column preserves the original GoEmotions example identifier. The
`example_id` column is local to this workshop subset.

## Source and licence

GoEmotions was created by Demszky et al. (2020) and contains Reddit comments annotated
for emotion categories.

- Dataset: <https://github.com/google-research/google-research/tree/master/goemotions>
- Paper: <https://aclanthology.org/2020.acl-main.372/>
- Licence: CC BY 4.0

Please retain this attribution when redistributing the subset.
