
The TemplateFlow Archive is organized in a [BIDS-like structure](https://bids-specification.readthedocs.io/en/derivatives/).
However, it deviates from the standard at times (e.g., the `tpl` key replaces `sub`).
Here we outline the most common names that are found in TemplateFlow.

Common key names using in TemplateFlow:

Key | Entity | Description
--- | :-: | ---
`tpl` | Template identifier | A unique name of the template, matching those of BIDS.
`res` | Resolution | See `template_description.json` within each template for more information about what the index specifies.
`atlas` | Atlas | Name of an atlas.
`desc` | Description | Additional information about the file to differentiate it from other files.

TemplateFlow uses all the valid suffices of BIDS, but the most commonly found in the Archive are:

Suffix | Description
--- | ---
`dseg` | discrete segmentation
`pseg` | probability segmentation
`mask` | binary mask
`xfm` | transform file
`T2w` | T2 weighted image
`T1w` | T1 weighted image

Common file-formats used in TemplateFlow:

Extension | Description
--- | ---
`.nii.gz` | Image
`.tsv`    | Tabular information
`.json`   | Meta-information
`.h5`     | Transform file


Thus a template with the following name:
`tpl-test_res-high_atlas-myatlas_desc-200nodes_dseg.nii.gz` would be a
NIfTI image containing the discrete segmentation of `myatlas` that
contains `200nodes`. The template identifier is `test`.
The resolution information will be found in the `template_description.json`
file under the entry `high`.